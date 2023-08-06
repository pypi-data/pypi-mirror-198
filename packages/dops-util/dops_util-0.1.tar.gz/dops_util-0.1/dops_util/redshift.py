#!/usr/bin/env python2
#from dops_util.connect import get_aws_account_id,getsessionv2,Account_Session,role_to_session,getsession,paginate
#from .global_var import *
#from dops_util.rds import *
#from dops_util.connect import *
from dops_util import *
from dops_util.cw import *

def list_redshift(account='All'):
    print("################Listing RedShift ################")
    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
        fout=open(cost_dir+'redshift_list' + '_'+ account + '_' + date+'.txt','w')

    else:
        Account_Session.initialize_all()
        fout=open(cost_dir+'redshift_list' + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:15},{:15},{:10},{:20},{:20},{:6},{:12},{:10},{:10},{:10},{:10},{:10},{:10} \n".format('Account','AccountName','ClusterIdentifier',
                                     'DatabaseName','ClusterCreateTime','Status','NumberOfNodes','Node Type','Last_3M_Cpu','Last_3M_DB_Max_Conn','Lifecycle','Owner','FundNo','Department','Schedule'))



    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding Redshift  on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        rs_cl = sessinfo['session'].client('redshift', region_name="us-east-1")
        ec2_resource = sessinfo['session'].resource('cloudwatch', region_name="us-east-1")

        cw=CloudWatchWrapper(ec2_resource)

        response = rs_cl.describe_clusters(
        )
        #print(response)

        rslist=response['Clusters']
        format_date=format = "%m-%d-%y"


        for rs in rslist:

            #list_inst_member=rs['DBClusterMembers']
            rs_instance_id=[]
            dimension=[                {
                    'Name': 'ClusterIdentifier',
                    'Value': rs['ClusterIdentifier']
                }
            ]

            Lifecycle="Not Tagged"
            Owner="Not Tagged"
            FundNo="Not Tagged"
            Department="Not Tagged"
            Schedule="Not tagged"

            if rs.get('Tags','NA')!='NA':
                for tag in rs['Tags']:
                    if tag['Key'].casefold().find('life'.casefold())!=-1:
                        Lifecycle=tag['Value']
                    elif tag['Key'].casefold().find('owner'.casefold())!=-1:
                        Owner=tag['Value']
                    elif tag['Key'].casefold().find('fund'.casefold())!=-1:
                        FundNo = tag['Value']
                    elif tag['Key'].casefold().find('department'.casefold())!=-1:
                        FundNo = tag['Value']
                    elif tag['Key'].casefold().find('schedule'.casefold())!=-1:
                        Schedule = tag['Value']
            #print (str(rs))
            cpu_max_util=cw.get_metric_statistics('AWS/Redshift','CPUUtilization', starttime, endtime, 7200, 'Average',dimension)
            db_connection_max=cw.get_metric_statistics('AWS/Redshift','DatabaseConnection', starttime, endtime, 7200, 'Maximum',dimension)
            out_format="{:18},{:30},{:50},{:30},{:10},{:20},{:20},{:12},{:12},{:12},{:20},{:20},{:20},{:20},{:10}".format(account,sessinfo['name'],rs['ClusterIdentifier'],rs.get('DBName','NA'),rs['ClusterCreateTime'].strftime(format),
                                                                                           rs['ClusterAvailabilityStatus'],rs['NumberOfNodes'],rs['NodeType'],
                                                                                           cpu_max_util,db_connection_max,Lifecycle,Owner,FundNo,Department,Schedule)
            print(out_format)
            fout.write(out_format + '\n')
            #print (rs['ClusterIdentifier'],rs['DBName'],rs['ClusterCreateTime'].strftime(format),rs['ClusterAvailabilityStatus'],rs['NumberOfNodes'],rs['NodeType'],cpu_max_util,db_connection_max)



if __name__ == '__main__':
    list_redshift('All')
