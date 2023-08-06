from dops_util import *
from .connect import *

def list_org_accounts():
     print("################Listing Sema4 AWS account ################")

     fout=open(cost_dir+'account_list' + '_'+date+'.txt','w')
     endtime=datetime.datetime.utcnow()
     starttime=endtime - datetime.timedelta(hours=int(2160))
     fout.write("{:20},{:30},{:15},{:20},{:20},{:40} \n".format('Account','AccountName','Account_Status','Join_Method','Account_Join_Date','Account_Email'))

     conn_sess=Account_Session()
     conn_sess.get_org_account()
     #print(conn_sess.account_org_all)
     for account in conn_sess.account_org_all:
          out_format="{:20},{:30},{:15},{:20},{:20},{:40}".format(account['Id'],account['Name'],account['Status'],account['JoinedMethod'],account['JoinedTimestamp'].strftime("%Y-%m-%d"),account['Email'])

          #print (account['Id'],account['Name'],account['Status'],account['JoinedMethod'],account['JoinedTimestamp'].strftime("%Y-%m-%d"),account['Email'])
          print(out_format)
          fout.write(out_format + '\n')


