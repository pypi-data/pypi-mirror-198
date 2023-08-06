

#from dops_util.connect import get_aws_account_id,getsessionv2,Account_Session,role_to_session,getsession,paginate
from .global_var import *
##rootaccount="011825642366"
#from .global_var import  *
#from dops_util import *



def get_aws_account_id(session):
    sts = session.client('sts')
    user_arn = sts.get_caller_identity()["Arn"]
    return user_arn.split(":")[4]

def getsessionv2(acc):
    #print "\n\n========================================"
    #print "account id " + acc['Id']
    #print "account name " + acc['Name']
    #print "========================================"
    #if acc['Id']==rootaccount:
    if acc==rootaccount:

        sess=boto3.session.Session()
    else:
        #cred = role_to_session(acc['Id'])
        cred = role_to_session(acc)


        credentials = cred['Credentials']


        sess= boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'])
    ##print "\n\n========================================"
    return sess



class Account_Session:
    account_to_skip = ['403521294875','768902525578','006775277657']
    SESS_DICT={}
    ACCLIST=[]
    ACCLIST_DICT={}
    ROOT='011825642366'
    @staticmethod
    def initialize_all():
        print("Initializing Session to All Subaccounts .. It will take about 2 minutes")
        sess=boto3.session.Session()
        currentacc=get_aws_account_id(sess)
        if currentacc != Account_Session.ROOT:
            print("The session need to start from root account")
            exit(1)
        client = boto3.client('organizations')
        counter=0
        acclistall=[ account  for account in paginate(client.list_accounts) if account['Id'] not in Account_Session.account_to_skip]
        print('acclist all', acclistall)
        #acclist=acclistall[0:20]
        acclist=acclistall[0:(len(acclistall))]
        #####acclist=acclistall[0:(len(acclistall)-80)]

        step=5
        batchno=0
        print(("Running batch of  Batch of " + str(step)))
        ## need to check if introduce bug below
        for cnt in range(int((len(acclist)/step)) + 1):
            batchno += 1
            print(("====== Running Batch No : " + str(batchno) + " =============="))
            pool = ThreadPool(step + 2)
            var=[ v for v in  acclist[(step * cnt):((step*cnt)+step)]  ]
            results = pool.map(Account_Session.__create_sess,var)
            pool.close()
            pool.join()
            #for r in results:
            #    print "result " + str(r)
        return

    @staticmethod
    def initialize(cnt):
        print("Initializing Session to All Subaccounts .. It will take about 20 Seconds")
        sess=boto3.session.Session()
        currentacc=get_aws_account_id(sess)
        if currentacc != Account_Session.ROOT:
            print("The session need to start from root account")
            exit(1)
        client = boto3.client('organizations')
        counter=0
        acclistall=[ account  for account in paginate(client.list_accounts)]
        #for acclist in acclistall:
        #    print "acllll " + str(acclist['Id'])
        #acclist=acclistall[0:20]
        stop = (cnt * acc_step)
        start = (cnt - 1) *  acc_step
        print(("cnt " + str(cnt) + ' stop ' + str(stop) + 'len acclistall ' + str(len(acclistall))))
        #acclist=acclistall[0:(len(acclistall)-1)]
        if stop <= len(acclistall):
            acclist=acclistall[start:stop]
            print(("acc list " + str(len(acclist))))
        else:
            acclist=acclistall[start:(len(acclistall))]
            print(("acc list2 " + str(len(acclist))  + ' acclist ' + str(acclist)))
        step=5
        batchno=0
        print(("Running batch of  Batch of " + str(step)))
        for cnt in range(int((len(acclist)/step)) + 1):
            batchno += 1
            print(("====== Running Batch No : " + str(batchno) + " =============="))
            pool = ThreadPool(step + 2)
            var=[ v for v in  acclist[(step * cnt):((step*cnt)+step)]  ]
            results = pool.map(Account_Session.__create_sess,var)
            pool.close()
            pool.join()
            for r in results:
                print(("result " + str(r)))
        return
    @staticmethod
    def __create_sess(account):
        print(("initializing session to account " + account['Id']))
        if not account['Id'] == Account_Session.ROOT:
            ses=getsessionv2(account['Id'])
        else:
            ses=boto3.session.Session()
        #Account_Session.SESS_LIST.append([ses,account[id],account['Name']])
        Account_Session.SESS_DICT.update({account['Id']:{'session':ses,'name':account['Name']}})
        #if counter > 10:

    @staticmethod
    def build_sess_subaccount(subaccount=None):
        #if not subaccount:
        #    Account_Session.initialize()
        #    return
        accountdict={}
        client = boto3.client('organizations')
        for account in paginate(client.list_accounts):
            accountdict.update({account['Id']:account['Name']})
        print(('creating session for account ' + subaccount))

        ses=getsessionv2(subaccount)
        Account_Session.SESS_DICT.update({subaccount:{'session':ses,'name':accountdict[subaccount]}})
        return  ses

    @staticmethod
    def get_account_list():
        Account_Session.ACCLIST=[]
        Account_Session.ACCLIST_DICT={}
        print("Gather Sema4 Account List ...")
        sess=boto3.session.Session()
        currentacc=get_aws_account_id(sess)
        if currentacc != Account_Session.ROOT:
            print("The session need to start from root account")
            exit(1)
        client = boto3.client('organizations')
        for account in paginate(client.list_accounts):
            ##print('accon ',str(account))
            Account_Session.ACCLIST.append(account['Id'])
            Account_Session.ACCLIST_DICT.update({account['Id']:account['Name']})
        return Account_Session.ACCLIST

    def __init__(self):
        print(" Initialize the Account_Session to a session.")
        client = boto3.client('organizations')
        self.sub_session = client


    def get_org_account(self):
        _account_org_all=[]
        for account in paginate(self.sub_session.list_accounts):
            _account_org_all.append(account)
            #print ('aclisg ',account)
        self.account_org_all=_account_org_all





def role_to_session(accountid):
    #print "account id " + accountid
    sts_client = boto3.client('sts')
    rolearn="arn:aws:iam::" + accountid + ":role/OrganizationAccountAccessRole"
    assumedRoleObject = sts_client.assume_role(
        #RoleArn="arn:aws:iam::011825642366:role/OrganizationAccountAccess",

        #RoleArn="arn:aws:iam::417302553802:role/OrganizationAccountAccessRole",
        RoleArn=rolearn,
        DurationSeconds=3600,
        RoleSessionName="organizational-su"
    )
    return assumedRoleObject

def getsession(acc):
    print("\n\n========================================")
    print(("account id " + acc['Id']))
    print(("account name " + acc['Name']))
    print("========================================")
    cred = role_to_session(acc['Id'])
    credentials = cred['Credentials']


    sess= boto3.Session(
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'])

    return sess



def paginate(method, **kwargs):
    client = method.__self__
    paginator = client.get_paginator(method.__name__)
    for page in paginator.paginate(**kwargs).result_key_iters():
        for result in page:
            yield result

