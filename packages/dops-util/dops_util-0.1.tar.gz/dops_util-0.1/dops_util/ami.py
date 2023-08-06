from dops_util import *

def lookup_trail_ami(ct_sess,ami):
    #print ("AMI  ", str(ami))
    print(("Looking up AMI  usage :" + ami))
    resp=ct_sess.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'ResourceName',
                'AttributeValue':  ami
            },
        ]
    )
    ####print "resp ct " + str(resp['Events'])
    run_instance=[]

    for event in resp['Events']:
        ##print "event name " + event['EventName']
        ##print "event time " + event['EventTime'].strftime("%Y-%m-%d %H:%M")

        if event['EventName'] == 'RunInstances':
            run_instance.append(event['EventTime'])


        ####if event['EventName'] == 'AttachVolume' or  event['EventName'] == 'DetachVolume':
        ####     print "event name " + event['EventName']
        #### print "event time " + event['EventTime'].strftime("%Y-%m-%d %H:%M")
    sorted_run_instance=sorted(run_instance)
    res={}
    if sorted_run_instance:
        print(("the last ami used by ec2  " + sorted_run_instance[-1].strftime("%Y-%m-%d %H:%M")))
        res={"last_ami_used":sorted_run_instance[-1].strftime("%m-%d-%Y")}
    else:
        res={"last_ami_used":"NoInfo"}

    return res



def get_ami_snap(client):
    dict_ami_list=[]
    response = client.describe_images(

        Owners=[
            'self',
        ]
    )
    return response['Images']
'''
    block_dev_dict={}
    for resp in response('Images'):
        for block_dev in resp['BlockDeviceMappings']:
            block_dev_dict.update({'ami_id':resp['ImageId']})
            block_dev_dict.update({'snapshot_id':block_dev['SnapshotId']})
            block_dev_dict.update({'device_name':block_dev['Ebs']['DeviceName']})
            block_dev_dict.update({'virtual_name':block_dev['Ebs']['VirtualName']})
            block_dev_dict.append({'volume_size':block_dev['Ebs']['VolumeSize']})


'''
def check_instance(client):

    response = client.describe_instances()['Reservations']
    ami_used_list=[]
    #print ('hhh',str(response[1]['Instances']))
    if response:
        for group_instance in response:
            ami_used_tmp=[]
            for inst in group_instance['Instances']:
                ami_used_tmp.append(inst['ImageId'])
            ami_used_list.extend(ami_used_tmp)
    #for debugging
    # print('ami list used by existing instances' ,str(ami_used_list))

    return ami_used_list

        #ami_list=[r['Instances']['ImageId'] for r in response ]
        #print ('res ',str)

        #ami_list=[r for r in response ['Instances']]
        #print ('response instances', response[0]['Instances'])

        #ami_list=[r['ImageId'] for r in response ]
        #print('ami list used by existing instances' ,str(ami_list))

def validate_ami(ec2_sess,arr_list,datebef,v_except):
    #arr_list
    cnt1=0
    cnt2=0
    for arr in arr_list:
## AMI_Sn means that the snapshot is AMI's Snashot
        if arr['volume_orphan'] == 'AMI_Sn':
            cnt1 = cnt1 + 1
            ##print " cnt 1 "+ str(cnt1) + ' with '  + arr['SnapshotId']
    ami_list=get_ami_snap(ec2_sess)

    for ami in ami_list:

        if datetime.datetime.strptime(ami['CreationDate'].split('.')[0],'%Y-%m-%dT%H:%M:%S') < datebef:
            for  dev in ami['BlockDeviceMappings']:
                if 'ephemeral'  not in dev.get('VirtualName','NA') and dev['Ebs']['SnapshotId'] not in v_except:
                    cnt2 = cnt2 + 1
                    ##print "cnt2 " + str(cnt2) + ' with ' + dev['Ebs']['SnapshotId']


    if cnt1 == cnt2:
        return True
    else:
        return False




def list_ami(subaccount='All',delete_ami=False):
    print("################Listing AMI ################")
    total_account_sub_dict={}
    #print(("CreationDate,{},ImageId,{},ImageLocation,{},ImageType,{},Public,{},OwnerId,{},State,{},BlockDeviceMappings,{},Description,{},Name,{} ".
    #       format(image['CreationDate'],image['ImageId'],image['ImageLocation'],image['ImageType'],image['Public'],image['OwnerId'],image['State'],str(image['BlockDeviceMappings']),image.get('Description','NA'),image['Name'])))
    del_ami_list=[]

    fout=open(cost_dir+'ami_list_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))

    out_format_header="{:15},{:20},{:30},{:30},{:15},{:10},{:10},{:20},{:20},{:30},{:30},{:15},{:20} \n". \
    format('Account','AccountName','Creation_Date','Image ID','Lastime_Usage','Used_By_EC2','State','ImageType',\
           'AMI Size','Description','Name','Lifecycle_Tag','Name_Tag')

    # fout.write("{:15},{:20},{:15},{:15},{:15},{:10},{:10},{:20},{:20},{:6},{:12},{:20} \n".
    #          format('Account','AccountName','Creation_Date','Image ID','Lastime_Usage','Image_Used_By_Existing_EC2','State','ImageType',
    #                                                         'Public AMI','Volume Size','Description','Name'))

    fout.write((out_format_header))

    if delete_ami or subaccount != 'All':
        Account_Session.build_sess_subaccount(subaccount)
    else:
        Account_Session.initialize_all()
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Finding AMI account : ' + account + ' ============================\n\n\n'))
            # Define the connection
            ec2 = sessinfo['session'].client('ec2', region_name="us-east-1")
            ect = sessinfo['session'].client('cloudtrail', region_name="us-east-1")
            ami_ec2_usage=check_instance(ec2)
            ## For Debugging
            # print ("AMI EC2 usage", str(ami_ec2_usage))


        # Find all volumes
        #     if subaccount.upper() == 'ALL':
            resp = ec2.describe_images(Owners=['self'])
            for image in resp['Images']:
                # print(str(image))
                del_ami_dict={}
                ami_tag_lifecycle_value='NA'
                ami_tag_name_value='NA'
                ami_used_in_existing_ec2=False
                ami_usage={'last_ami_used':'NoInfo'}
                if check_ami_in_trail:
                    ami_usage=lookup_trail_ami(ect,image['ImageId'])
                else:
                    ami_usage={"last_ami_used":"NoInfo"}
                # print('image id ami usage',image['ImageId'],ami_usage)

                if image.get('Tags','NA') != 'NA':
                    # print('get image tag',image.get('Tags','NA'))
                    for ami_tag in image['Tags']:
                        if ami_tag['Key'].lower() == 'lifecycle':
                            ami_tag_lifecycle_value = ami_tag['Value']
                        if ami_tag['Key'].lower() == 'name':
                            ami_tag_name_value = ami_tag['Value']

                if ami_ec2_usage:
                    if image['ImageId'] in ami_ec2_usage:
                        ami_used_in_existing_ec2=True
                if delete_ami:
                    #####remove condition if AMI used by existing EC2
                    # if ami_usage['last_ami_used'] == 'NoInfo' and not ami_used_in_existing_ec2 and ami_tag_lifecycle_value.lower() != 'forever':
                    if ami_usage['last_ami_used'] == 'NoInfo' and ami_tag_lifecycle_value.lower() != 'forever':
                        del_ami_dict.update({'account':account,
                                            'acc_name': sessinfo['name'],
                                            'ami_created_date':image['CreationDate'],
                                            'ami_id':image['ImageId'],
                                            'last_ami_used':ami_usage['last_ami_used'],
                                            'ami_used_in_existing_ec2':str(ami_used_in_existing_ec2),
                                            'ami_state':image['State'],
                                            'ami_type':image['ImageType'],
                                            'ami_size':str(image['BlockDeviceMappings'][0]['Ebs']['VolumeSize']),
                                             'ami_desc':image.get('Description','NA').replace(',',';'),
                                            'ami_name':image['Name'],
                                             'ami_tag_lifecycle':ami_tag_lifecycle_value,
                                             'ami_tag_name':ami_tag_name_value})


                        del_ami_list.append(del_ami_dict)
                else:


                    #print(("CreationDate,{},ImageId,{},ImageLocation,{},ImageType,{},Public,{},OwnerId,{},State,{},BlockDeviceMappings,{},Description,{},Name,{} ".
                    #       format(image['CreationDate'],image['ImageId'],image['ImageLocation'],image['ImageType'],image['Public'],image['OwnerId'],image['State'],str(image['BlockDeviceMappings']),image.get('Description','NA'),image['Name'])))
                    #VolumeSize will be improved later
                    out_format = "{:15},{:20},{:30},{:30},{:15},{:10},{:10},{:20},{:20},{:30},{:30},{:15},{:20}".format(
                        account,
                        sessinfo['name'], image['CreationDate'], image['ImageId'], ami_usage['last_ami_used'],
                        str(ami_used_in_existing_ec2), image['State'], image['ImageType']
                        , str(image['BlockDeviceMappings'][0]['Ebs']['VolumeSize']),
                        image.get('Description', 'NA').replace(',', ';'), image['Name'], ami_tag_lifecycle_value,
                        ami_tag_name_value)



                    print(out_format)
                    fout.write(out_format + '\n')
        if delete_ami:
            return del_ami_list,out_format_header
            #total_account_sub_dict.update({sessinfo['Name']:total_size_sub})

    except Exception as err :
        print(("List Snapshot  " + str(err)))
        raise
def delete_unused_ami(sub_account):
    ses=Account_Session.build_sess_subaccount(subaccount=sub_account)
    ec2 = ses.resource('ec2', region_name='us-east-1')
    resp=list_ami(sub_account,delete_ami=True)
    print('AMI to be deleted')
    print(resp[1])
    for ami_dict in resp[0]:

        out_format="{:15},{:20},{:30},{:30},{:15},{:10},{:10},{:20},{:20},{:30},{:30},{:15},{:20}".format(ami_dict['account'],
                                                                                               ami_dict['acc_name'],
                                                                                               ami_dict['ami_created_date'],
                                                                                               ami_dict['ami_id'],
                                                                                               ami_dict['last_ami_used'],
                                                                                               ami_dict['ami_used_in_existing_ec2'],
                                                                                               ami_dict['ami_state'],
                                                                                               ami_dict['ami_type'],
                                                                                               ami_dict['ami_size'],
                                                                                               ami_dict['ami_desc'][:20],
                                                                                               ami_dict['ami_name'][:20],
                                                                                               ami_dict['ami_tag_lifecycle'],
                                                                                               ami_dict['ami_tag_name']
                                                                                          )
        print(out_format)


    #inp=eval(input("Deleting AMI Unused by EC2 and has not been used for 3 Month age , enter Y to proceed ... "))
    inp=input("Deleting AMI Unused by EC2 and has not been used for 3 Month age , enter Y to proceed ... ")
    if inp == 'Y':
        for ami_dict in resp[0]:
            print(("\nbatch deleting/deregistering   ami " +  str(ami_dict['ami_id'])))
            ami=ec2.Image(ami_dict['ami_id'])
            ami.deregister()
    else:
        print("batch AMI delete canceled")



