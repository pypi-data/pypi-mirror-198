#from .global_var import *
from dops_util import *



def list_service_catalog(acc='All'):
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout=open(cost_dir+'service_catalog_' +date+'.txt','w')

    fout.write("{:15}, {:20}, {:15},{:8},{:24},{:15},{:10},{:24}\n".format('Account','AccountName','AvailabilityZone','Last_3_Month_Average_CPU','InstanceClass',
                                                                    'InstanceStatus','AllocatedStorage','InstanceIdentifier'))



    print("################Checking Service Catalog ################")
    Account_Session.initialize_all()
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Checking service catalog on account : ' + account + ' ============================\n\n\n'))

            ## Define the connection
            #ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
            ec2_client = sessinfo['session'].client('servicecatalog', region_name="us-east-1")



            #response = ec2_client.list_portfolios()
            response = ec2_client.list_portfolios()

            for ep in response['PortfolioDetails']:
                print (ep)
                #cp_metric=cw.get_metric_statistics(namespace, name, start, end, period, stat_types):

                #
                # out_format="{:15},{:30},{:15},{:8},{:24},{:15},{:10},{:24}".format(account,sessinfo['name'],ep['AvailabilityZone'],cpu_average_util,
                #                                                               ep['ReplicationInstanceClass'], ep['ReplicationInstanceStatus'],ep['AllocatedStorage'],
                #                                                               ep['ReplicationInstanceIdentifier'])
                # print(out_format)
                # fout.write(out_format + '\n')

    except Exception as err :
        print((traceback.format_exc()))
        print(("Finding  service catalog portfolio " + str(err)))


