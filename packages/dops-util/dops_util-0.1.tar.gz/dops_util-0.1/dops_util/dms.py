#from .global_var import *
from dops_util import *



def checking_provision_dms(acc='All'):
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout=open(cost_dir+'dms_list_' +date+'.txt','w')

    fout.write("{:15}, {:20}, {:15},{:8},{:24},{:15},{:10},{:24}\n".format('Account','AccountName','AvailabilityZone','Last_3_Month_Average_CPU','InstanceClass',
                                                                    'InstanceStatus','AllocatedStorage','InstanceIdentifier'))



    print("################Checking DMS Instance  ################")
    Account_Session.initialize_all()
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Checking Instances  on account : ' + account + ' ============================\n\n\n'))

            ## Define the connection
            #ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
            ec2_client = sessinfo['session'].client('dms', region_name="us-east-1")
            ec2_resource = sessinfo['session'].resource('cloudwatch', region_name="us-east-1")
            cw=CloudWatchWrapper(ec2_resource)



            response = ec2_client.describe_replication_instances()

            for ep in response['ReplicationInstances']:
                #cp_metric=cw.get_metric_statistics(namespace, name, start, end, period, stat_types):

                dimension=[

                    {
                        'Name': 'ReplicationInstanceIdentifier',
                        'Value': ep['ReplicationInstanceIdentifier']
                    }
                ]
                cpu_average_util=cw.get_metric_statistics('AWS/DMS','CPUUtilization', starttime, endtime, 7200, 'Average',dimension,unit=1000000000)
                #cpu_max_util=cw.get_metric_statistics('AWS/DMS','CPUUtilization', starttime, endtime, 7200, 'Maximum','ReplicationInstanceIdentifier','samasekali')
                #print('dd ',cpu_metric)
                #cpu_max_util=get_cw_metric(ec2_client,ep['ReplicationInstanceIdentifier'],starttime,endtime,name_space='AWS/DMS',type='ReplicationInstanceIdentifier')

                out_format="{:15},{:30},{:15},{:8},{:24},{:15},{:10},{:24}".format(account,sessinfo['name'],ep['AvailabilityZone'],cpu_average_util,
                                                                              ep['ReplicationInstanceClass'], ep['ReplicationInstanceStatus'],ep['AllocatedStorage'],
                                                                              ep['ReplicationInstanceIdentifier'])
                print(out_format)
                fout.write(out_format + '\n')

    except Exception as err :
        print((traceback.format_exc()))
        print(("Finding  Provision DMS Instance  " + str(err)))


