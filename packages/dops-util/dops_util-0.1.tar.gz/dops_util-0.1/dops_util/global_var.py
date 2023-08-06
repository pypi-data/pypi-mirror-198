#!/usr/bin/env python2
##############
import boto3
import traceback
import os
import random
import time
import sys
import argparse
import uuid
import json
import os
import datetime
import pprint
import operator
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import pytz
import math
from botocore.exceptions import ClientError


rootaccount="011825642366"
#repo_home='/Users/IndraHarahap/PycharmProjects/s4-devops-util/'
utc=pytz.UTC
####delta=datetime.timedelta(days=90)  ## Age of EBS deletion for NON Interactive Deletion
delta=datetime.timedelta(days=0)  ## Age of EBS deletion for NON Interactive Deletion
hour_passed=datetime.timedelta(hours=0)     ## Age of ebs volume for batch deletion
age=datetime.timedelta(days=7)   ## Age of ebs snapshot for batch deletion
datenow=datetime.datetime.now(utc)
check_ami_in_trail=True  ## set false to not check 3 month of whether AMI is used
#rootaccount="011825642366"
cost_dir=datetime.datetime.now().strftime('%m%d%Y') + '/csv/'
#sc_client = boto3.client('servicecatalog', region_name='us-east-1')
iam_client = boto3.client('iam', region_name='us-east-1')
session_client = boto3.client('sts')
# import_portfolios = ['port-rx4vc3kthfxfw']
# linux_portfolio_id = 'port-rx4vc3kthfxfw'
application_name = 'Linux Application'
linux_portfolio = 'Linux Portfolio'

#ec2vpcrole=json.dumps({"RoleArn" : "arn:aws:iam:::role/SCEC2LaunchRole"})


date=datetime.datetime.now().strftime('%m%d%Y')
fdate=format = "%m-%d-%Y"
account_id = boto3.client('sts').get_caller_identity()['Account']
print(("Your STS account id is: " +account_id))
acc_step=10
spec_session=[359051777659]
spec_session_reconnect=20
ebs_except='/var/tmp/ebs_exception'
snapshot_except='/var/tmp/snapshot_exception'
##file contain ebs not to be deleted in batch delete


rm_path_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

print(("Resource monitor ", rm_path_dir))

cost_dir_path=os.path.join(rm_path_dir, cost_dir)
#cost_dir_path=os.path.join(repo_home, cost_dir)

if not os.path.isdir(cost_dir_path) :
    os.makedirs(cost_dir_path)
    print(("Csv Output Directory '% s' created" % cost_dir_path))
else:
    print(("Csv Output Directory '% s' " % cost_dir_path))



