from dops_util import *
#import boto3
#import json
#import pandas as pd
#from datetime import datetime

client = boto3.client('ce')
_start_time = "2022-09-01"
_end_time="2022-10-06"

## to get the dimension, values
## aws ce  get-dimension-values --time-period Start=2022-09-01,End=2022-09-18 --dimension SERVICE

def get_dimension_value():
    response = client.get_dimension_values(
        #SearchString='string',
        TimePeriod={
        'Start': _start_time,
        'End': _end_time
         },
        #Dimension='SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|
        # 'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|
        # 'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION'|
        # 'AGREEMENT_END_DATE_TIME_AFTER'|'AGREEMENT_END_DATE_TIME_BEFORE'|'INVOICING_ENTITY',
        Dimension='USAGE_TYPE'

    )
    print ('dimension value ',str(response))

# aws cli to test
# aws ce get-cost-and-usage \
#   --time-period Start=2022-09-01,End=2022-10-15 \
#   --granularity DAILY \
#   --metrics "BlendedCost" \
#   --group-by Type=DIMENSION,Key=INSTANCE_TYPE Type=DIMENSION,Key=DATABASE_ENGINE \
#   --filter file://filters.json
# filters.json as below
# {
#     "Dimensions": {
#         "Key": "SERVICE",
#         "Values": [
#             "Amazon Relational Database Service"
#         ]
#     }
# }


def list_cost_usage(type='RDS',length=720,account='All'):
    ### To get dimension value
    ####get_dimension_value()

    # fout=open(cost_dir + 'Last_' + str((length/24)) + '_Days_Cost_Usage_' + type.upper()+ '_'+date+'.txt','w')
    if type.upper() == 'RDS':
        service_type='Amazon Relational Database Service'
        # fout.write("{:30},{:15},{:15}\n".format('RDS Instance_Type','Cost_Type','Cost_Usage'))

    elif type.upper() == 'RDS_SERVERLESS':
        service_type='Amazon Relational Database Service'
        # fout.write("{:30},{:15},{:15}\n".format('Project Tag','Cost_Type','Cost_Usage'))


    elif type.upper() == 'EC2':
        service_type = 'Amazon Elastic Compute Cloud - Compute'
        # fout.write("{:30},{:15},{:15}\n".format('Instance_Type','Cost_Type','Cost_Usage'))

    elif type.upper() == 'SUPPORT_DEV':
        service_type = "AWS Support (Developer)"
        # fout.write("{:30},{:15},{:15}\n".format('Support Type','Cost_Type','Cost_Usage'))

    elif type.upper() == 'SUPPORT_BUSINESS':
        service_type = 'AWS Support (Business)'
        print ("Collecting  Cost Usage for ",type)

    elif type.upper() == 'CONFIG':
        service_type = 'AWS Config'
        print ("Collecting  Cost Usage for ",type)

    elif type.upper() == 'CLOUDWATCH':
        service_type = 'AmazonCloudWatch'
        print ("Collecting  Cost Usage for ",type)
    fout_account=open(cost_dir + 'Last_' + str((length/24)) + '_Days_Cost_Usage_Per_Account_'  + type.upper()+ '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(length))
    fout_account.write("{:30},{:15},{:15},{:10}\n".format('Account','AccountName','Cost_Type','Cost_Usage'))
    try:
        Account_Session.get_account_list()
        collection_tally_dict={}
        account_dict={}
        account_rds_serverless_dict={}
        for aws_account_number in Account_Session.ACCLIST:
            _start_time = starttime.strftime("%Y-%m-%d")
            _end_time=endtime.strftime("%Y-%m-%d")
            if type.upper() == 'RDS' or type.upper() == 'EC2' or type.upper() == 'SUPPORT_DEV' or type.upper() == 'SUPPORT_BUSINESS' or \
                    type.upper() == 'CONFIG' or type.upper() == 'CLOUDWATCH':
                response = get_costs(_start_time, _end_time, aws_account_number,service_type)
                tally_costs(response, collection_tally_dict,type, account_dict, aws_account_number, account_rds_serverless_dict)
            if type.upper() == 'RDS_SERVERLESS':
               response = get_costs(_start_time, _end_time, aws_account_number,service_type,rds_serverless=True)
               tally_costs(response, collection_tally_dict, type, account_dict, aws_account_number, account_rds_serverless_dict)

        if type.upper() != 'SUPPORT_DEV' and type.upper() != 'SUPPORT_BUSINESS' and type.upper() != 'CONFIG':  ## SUPPORT_DEV and SUPPORT_BUSINESS only tally on Account Level
            sorted_items=(sorted(collection_tally_dict.items(), reverse=True, key = lambda kv:(kv[1], kv[0])))
            for item in sorted_items:
               print (str(item[0]),str(item[1]))
               out_format="{:30},{:15},{:10.0f}".format(item[0],type,item[1])
               print(out_format)
               fout.write(out_format + '\n')

        sorted_items=(sorted(account_dict.items(), reverse=True, key = lambda kv:(kv[1], kv[0])))
        for item in sorted_items:
            if type.upper() == 'SUPPORT_DEV' or type.upper() == 'SUPPORT_BUSINESS' or type.upper() == 'CONFIG' or type.upper() == 'CLOUDWATCH':
                out_format="{:30},{:15},{:15},{:10}".format(item[0],Account_Session.ACCLIST_DICT[item[0]],type,item[1])
            else:
                out_format="{:30},{:15},{:15},{:10.0f}".format(item[0],Account_Session.ACCLIST_DICT[item[0]],type,item[1])
            print(out_format)
            fout_account.write(out_format + '\n')
    except Exception as e:
            print("Error occured => "+str(e))
            raise


def get_costs(start_time, end_time, aws_account_number,type,rds_serverless=False):
    extra_filter={}
    granularity='DAILY'
    filter_1={'Dimensions': {
        'Key': 'LINKED_ACCOUNT',
        'Values': [
            aws_account_number, # ROOT ACCOUNT => 011825642366
        ],
        'MatchOptions': [
            'EQUALS',
        ]
    }
    }
    filter_2= {
    'Dimensions': {
        'Key': 'SERVICE',
        'Values': [
            type
        ],
        'MatchOptions': [
            'EQUALS',
        ]
    }
    }

    if type =='Amazon Relational Database Service' and not rds_serverless:
        group_by= [

            {
                'Type': 'DIMENSION',
                'Key': 'INSTANCE_TYPE'
            },

          {
            'Type': 'DIMENSION',
             'Key': 'DATABASE_ENGINE',
         }
        ]
        filter=[filter_1,filter_1]
    elif type == 'Amazon Elastic Compute Cloud - Compute':
        print ("in bhere ")
        group_by= [

            {
                'Type': 'DIMENSION',
                'Key': 'INSTANCE_TYPE'
            }
        ]
        filter=[filter_1,filter_2]
    elif type == "AWS Support (Developer)" or type == "AWS Support (Business)":
        granularity='MONTHLY'
        group_by= [

            {
                'Type': 'DIMENSION',
                'Key': "LINKED_ACCOUNT"
            }
        ]
        #group_by=[]
        filter=[filter_1,filter_2]
    elif type == "AWS Config" or type == "AmazonCloudWatch":
        granularity='MONTHLY'
        group_by= [

            {
                'Type': 'DIMENSION',
                'Key': "LINKED_ACCOUNT"
            }
        ]
        #group_by=[]
        filter=[filter_1,filter_2]
    elif rds_serverless:
        print ("in route serviless")
        extra_filter=   {
            'Dimensions': {
                'Key': 'USAGE_TYPE',
                'Values': [
                    'Aurora:ServerlessUsage'
                ],
                'MatchOptions': [
                    'EQUALS',
                ]
            }
        }
        filter=[filter_1,filter_2,extra_filter]


        group_by=[
            {
        'Type': 'TAG',
        'Key': 'Project'
         }
        ]
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_time,
            'End': end_time
        },
        #Granularity='DAILY',
        Granularity=granularity,
        Filter={
         'And':filter,
        },
        GroupBy=group_by,
        ##GroupBy=group_by,
        Metrics=[
            'BLENDED_COST',
        ],
    )
    return response


def tally_costs(response, instance_tally_dict, type, account_dict, aws_account_number, account_rds_serverless_dict):
    #list_instance_types_groups=response["ResultsByTime"]
    account_dict[aws_account_number]=0
    account_total=0
    account_rds_serverless_dict[aws_account_number]=0
    #print ('resp account :',aws_account_number, str(response["ResultsByTime"]))
    print ('resp account :',aws_account_number, str(response))

    if type.upper() == 'SUPPORT_DEV' or type.upper() == 'SUPPORT_BUSINESS' or type.upper() == 'CONFIG' or type.upper() == 'CLOUDWATCH':
        support_cost=[]
        for instance_type_group in response["ResultsByTime"]:
            instance_type_group_list = instance_type_group["Groups"]
            for entry in instance_type_group_list:
                #print('support cost time_period ',str(entry['TimePeriod']['Start']),entry['Total']['BlendedCost']['Amount'])
                if entry["Metrics"]["BlendedCost"]["Amount"] !=0:
                #if entry['Total']['BlendedCost']['Amount'] != '0':
                    support_cost.append(entry["Metrics"]["BlendedCost"]["Amount"])
        if not support_cost:
            support_cost.append('0')

        print('Last support cost :'," ".join(support_cost))
        account_dict[aws_account_number]=" ".join(support_cost)

    else:

        for instance_type_group in response["ResultsByTime"]:
            instance_type_group_list = instance_type_group["Groups"]
            for instance_type in instance_type_group_list:
                key1= instance_type["Keys"][0].lower()
                if type.upper() != 'RDS':
                    key2=''
                elif type.upper() == 'RDS':
                    key2= instance_type["Keys"][1].lower()

                dollar_amount= float(instance_type["Metrics"]["BlendedCost"]["Amount"])
                group_key=key1 + " " + key2
                if key1 !="noinstancetype" and key2 != 'nodatabaseengine' and type.upper() == 'RDS':
                    print ("group kehy ",group_key)
                    if group_key in instance_tally_dict.keys():
                        dollar_amount1 = dollar_amount + float(instance_tally_dict[group_key])
                        instance_tally_dict[group_key]=dollar_amount1
                    else:
                        instance_tally_dict[group_key]=dollar_amount
                    account_dict[aws_account_number]+=dollar_amount

                #elif key1 == "noinstancetype" and not key2 and type.upper() == 'RDS_SERVERLESS':
                elif type.upper() == 'RDS_SERVERLESS':

                    #print ("group kehy rds serverles  ",group_key,' dollar amount ',dollar_amount)
                    if group_key in instance_tally_dict.keys():
                        dollar_amount1 = dollar_amount + float(instance_tally_dict[group_key])
                        instance_tally_dict[group_key]=dollar_amount1
                    else:
                        instance_tally_dict[group_key]=dollar_amount
                        #account_total+=dollar_amount
                    account_dict[aws_account_number]+=dollar_amount




