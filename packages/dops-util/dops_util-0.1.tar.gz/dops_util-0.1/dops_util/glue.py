from dops_util import *
from dops_util.cw import *

def list_glue_dev_endpoints(type='All'):

    fout=open(cost_dir+'list_glue_dev_endpoints'+ date+'.txt','w')
    format_date=format = "%Y-%m-%dT%H:%M:%S"
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("Account,Account_name,Instance ID,Instance Name, Instance Type  , State, Spot_Insta_Req_Id,state_reason,capacity_reservation_id ,cpu_max_util_last_3_month\n")


    print("################Checking EC2 Instance  ################")
    Account_Session.initialize_all()
    # try:
    #     for account,sessinfo in list(Account_Session.SESS_DICT.items()):
    #         print(('\n\n\n====================Checking Instances  on account : ' + account + ' ============================\n\n\n'))
    #
    #
    #
    #         # Define the connection
    #         ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
    #         ec2_client = sessinfo['session'].client('cloudwatch', region_name="us-east-1")
    #
    #
