import json  # module for converting Python objects to JSON
# decimal module support correctly-rounded decimal floating point arithmetic.
from decimal import Decimal
#import boto3  # import Boto3
import json
from dops_util import *




def load_data(execs, table_name='batch_output', dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb',region_name='us-east-1')

    batch_output_table = dynamodb.Table(table_name)
    # Loop through all the items and load each
    for exec in execs:
        exec_id = (exec['exec_id'])
        # Print device info
        print("Loading  Data execution_id :", exec_id)
        batch_output_table.put_item(Item=exec)



def get_data(device_id, accountid,table_name='batch_output_info', dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb',region_name='us-east-1')
    # Specify the table to read from
    devices_table = dynamodb.Table(table_name)

    try:
        response = devices_table.get_item(
                Key={'exec_id': device_id,'account_id':accountid})
    except Exception as e:
        print(e.response['Error']['Message'])
    else:
        #print ("res ",str(response))
        if response.get('Item','NA') != 'NA':
            return response['Item']

def put_data(exec_id,account,vol_list,table_name='batch_output_info',dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb',region_name='us-east-1')
    # Specify the table
    dynamo_table = dynamodb.Table(table_name)
    response = dynamo_table.put_item(
        # Data to be inserted
        Item={
            'exec_id': exec_id,
            'account_id':account,
            'vol_id': vol_list

        }
    )
    return response

if __name__ == '__main__':
    vol_list=['mahal','murah']
    exec_id='1014'
    account='888'
    device_resp = put_data(exec_id,account,vol_list)
    print("Create item successful.")
    resp=get_data(exec_id,account)
    print("retrieving the table",resp)
    # Print response
    print(device_resp)

# if __name__ == '__main__':
#     device = get_data("10001")
#     if device:
#         print("Get Device Data Done:")
#         # Print the data read
#         print(device['vol_id'])

#
# if __name__ == '__main__':
#     print ('test')
#
#         jfile=open('dynamo.json','r')
#         exec_list = json.load(jfile, parse_float=Decimal)
#         load_data(exec_list)