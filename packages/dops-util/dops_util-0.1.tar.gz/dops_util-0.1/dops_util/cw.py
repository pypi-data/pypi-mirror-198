
#from .global_var import *
from dops_util import *

def get_cw_metric(client,value_id,starttime,endtime,name_space='AWS/EC2',type='InstanceId',metric_name='CPUUtilization',stats='Maximum'):
    ##FOR DEBUGGING
    # print(("collecting cloud watch  metrics " + metric_name))
    #client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
        Namespace=name_space,
        MetricName=metric_name,
        Dimensions=[
            {
                'Name': type,
                'Value': value_id
            },
        ],

        StartTime=starttime,
        EndTime=endtime,
        Period=7200,
        Statistics=[
            stats,
        ],
        #Unit='Percent'
    )
    #if metric_name=='DatabaseConnections':
    #    print str(response)
    cpu_collect=[]
    for k, v in list(response.items()):
        if k == 'Datapoints':
            for y in v:
                if y[stats] or y[stats] == 0.0 :
                    cpu_collect.append(y[stats])
                    #print (" {0:.2f}".format(y['Maximum']))
                #return "{0:.2f}".format(y['Maximum'])
    #print str(cpu_collect)
    if cpu_collect:
        #print "Sorted one " + str(sorted(cpu_collect))
        max_all=sorted(cpu_collect)[-1]
        #print "max_all " + str(max_all)
        return max_all



class CloudWatchWrapper:
    """Encapsulates Amazon CloudWatch functions."""
    def __init__(self, cloudwatch_resource):
        """
        :param cloudwatch_resource: A Boto3 CloudWatch resource.
        """
        self.cloudwatch_resource = cloudwatch_resource

    #def get_metric_statistics(self, namespace, name, start, end, period, stat_types,type,value_id):
    def get_metric_statistics(self, namespace, name, start, end, period, stat_types,dimension=[],unit=None):
        """
        Gets statistics for a metric within a specified time span. Metrics are grouped
        into the specified period.

        :param namespace: The namespace of the metric.
        :param name: The name of the metric.
        :param start: The UTC start time of the time span to retrieve.
        :param end: The UTC end time of the time span to retrieve.
        :param period: The period, in seconds, in which to group metrics. The period
                       must match the granularity of the metric, which depends on
                       the metric's age. For example, metrics that are older than
                       three hours have a one-minute granularity, so the period must
                       be at least 60 and must be a multiple of 60.
        :param stat_types: The type of statistics to retrieve, such as average value
                           or maximum value.
        :return: The retrieved statistics for the metric.
        """
        max_all='NA'
        try:
            metric = self.cloudwatch_resource.Metric(namespace, name)
            stats = metric.get_statistics(
                Dimensions=dimension,
                StartTime=start, EndTime=end, Period=period, Statistics=[stat_types])
            ## Debugging
            # print(    "Got %s statistics for %s.", len(stats['Datapoints']), stats['Label'])
            cpu_collect=[]
            for k, v in stats.items():
                if k == 'Datapoints':
                    for y in v:
                        if y[stat_types] or y[stat_types] == 0.0 :
                            cpu_collect.append(y[stat_types])
                            #print (" {0:.2f}".format(y['Maximum']))
                        #return "{0:.2f}".format(y['Maximum'])
            #print str(cpu_collect)
            if cpu_collect:
                #print "Sorted one " + str(sorted(cpu_collect))
                max_all=sorted(cpu_collect)[-1]
                #print ('cpu coollect ',str(cpu_collect))
                #print "max_all " + str(max_all)

        except Exception as err :
                raise
        else:
                if unit and max_all != 'NA':
                    format_float = "{:.2f}".format(max_all/unit)
                    return format_float
                else:
                    if 'connection' in name.lower() and max_all == 'NA':
                        return 0
                    else:
                        if name=='BucketSizeBytes':
                            return -1
                        else:
                            return max_all

