#from dops_util.cw import *
#from dops_util.connect import *
from dops_util.global_var import *
from dops_util.connect import *
import botocore

def list_workspaces(account=all):
    regions=['us-east-1','eu-central-1','ap-south-1','ca-central-1']
    print ("Listing all Workspaces on all accounts ")

    Account_Session.initialize_all()
    fout=open(cost_dir+'list_workspace' + '_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))


    fout.write("{:15}, {:20}, {:30},{:20},{:30},{:15},{:20},{:20},{:10},{:10},{:10},{:10},{:6},{:6},{:12}\n".format('Account','AccountName','UserName','State','ComputerName','IP Address','ComputeTypeName'
                                                                                        ,'BundleId','RunningMode','RootGB','UserVolGB','Subnet_Id','UserVol_Enc','RootVol_Enc','Region'))


    for account,sessinfo in Account_Session.SESS_DICT.items():
        for region in regions:
            print(('\n\n\n====================Finding AWS Workspaces on account : ' + account + ' on region ' + region + ":" + sessinfo['name'] + ' ============================\n\n\n'))

            sc_client = sessinfo['session'].client('workspaces', region_name=region)
            #ec2_resource = sessinfo['session'].resource('cloudwatch', region_name="us-east-1")

            try:
                paginator = sc_client.get_paginator('describe_workspaces')
                for response in paginator.paginate():
                    for resp in response['Workspaces']:
                        #print(resp['UserName'],',',resp['PasswordLastUsed'])
                        print (str(resp))




                        out_format="{:15}, {:20}, {:30},{:20},{:30},{:15},{:20},{:20},{:10},{:10},{:10},{:10},{:6},{:6},{:12}".format(account,sessinfo['name'],resp['UserName'],
                                                                                       resp['State'],resp.get('ComputerName','NA'),resp.get('IpAddress','NA'),
                                                                                  resp['WorkspaceProperties']['ComputeTypeName'],resp['BundleId'],
                                                                                                          resp['WorkspaceProperties']['RunningMode'],
                                                                                                                resp['WorkspaceProperties']['RootVolumeSizeGib'],
                                                                                                                resp['WorkspaceProperties']['UserVolumeSizeGib'],
                                                                                                                  resp.get('SubnetId','NA'),
                                                                                                                  str(resp.get('UserVolumeEncryptionEnabled','NA')),
                                                                                                                  str(resp.get('RootVolumeEncryptionEnabled','NA')),
                                                                                                                                      region)


                        print(out_format)
                        fout.write(out_format + '\n')



            except Exception as err:
                print((traceback.format_exc()))
                print(("list_workspaces " + str(err)))



def list_vpc():
    print("Listing VPC and subnet info on all accounts ")

    Account_Session.initialize_all()
    fout=open(cost_dir+'list_vpc' + '_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:20},{:20},{:20},{:10} \n".format('Account','AccountName','VPC ID','CIDR Block','State','Default VPC'))


    for account,sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding List Of VPC   on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n'))
        sc_client = sessinfo['session'].client('ec2', region_name="us-east-1")

        try:
            paginator = sc_client.get_paginator('describe_vpcs')
            for response in paginator.paginate():

                resp = response['Vpcs']
                if resp:
                    for rp in resp:

                        out_format="{:15},{:20},{:20},{:20},{:20},{:10}".format(account,sessinfo['name'],rp['VpcId'],
                                                                                     rp['CidrBlock'],rp['State'],str(rp['IsDefault']))


                        print(out_format)
                        fout.write(out_format + '\n')

                else:
                    print('No vpcs found')
        except:
            print("Error getting VPC info")
            raise



def list_s3(account='all'):

    Account_Session.initialize_all()
    fout=open(cost_dir+'list_s3' + '_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:15},{:15}\n".format('Account','AccountName','Bucket Name','Bucket Life Cycle'))



    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding S3 Information On account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        s3_res = sessinfo['session'].resource('s3', region_name="us-east-1")
        s3_cl = sessinfo['session'].client('s3', region_name="us-east-1")

        bucket_list = s3_res.buckets.all()
        for bucket_obj in bucket_list:
            try:
                print ("getting info bucket ",bucket_obj.name)
                response = s3_cl.get_bucket_lifecycle(
                    Bucket=bucket_obj.name
                )
                print (response['Rules'][0]['ID'])
                ##response = s3_cl.get_bucket_encryption(
                ##    Bucket=bucket_obj.name
                ##    #ExpectedBucketOwner='string'
                ##)
                ##response = s3_cl.get_bucket_location(
                ##    Bucket=bucket_obj.name
                #    #ExpectedBucketOwner='string'
                #)
                print (str(response))
                #print (bucket_obj.name,str(lcycle_list),s3_std_class)
                print (bucket_obj.name,response['Rules'][0]['ID'])
                #fout.write("{:15},{:20},{:15},{:15}\n".format('Account','AccountName','Bucket Name','Bucket Life Cycle'))

                out_format="{:15},{:20},{:15},{:15}".format(account,sessinfo['name'],bucket_obj.name,response['Rules'][0]['ID'])



                print(out_format)
                fout.write(out_format + '\n')




            except botocore.exceptions.ClientError as err:
                    if "NoSuchLifecycleConfiguration" in str(err) or 'AccessDenied' in str(err):
                        print (str(err))
                        print ("continue")
                        pass
                    else:
                        raise



def list_instances():


    print("Listing Instances on All Accounts ")

    Account_Session.initialize_all()
    fout=open(cost_dir+'list_instances' + '_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:30},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:25},{:15},{:15},{:15},{:15},{:7}\n".format('Account','AccountName',
                                                          'InstanceId','ImageId','InstanceType',
                                                         'KeyName','StateTransitionReason',
                                                            'PublicIpAddress','PrivateIpAddress','VpcId','State',
                                                            'Architecture','Platform','LaunchTime','Lifecycle Tag','Owner','Department','FundNo','Run Schedule'))




    for account,sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding List Of Instances on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n'))
        sc_client = sessinfo['session'].client('ec2', region_name="us-east-1")


        try:
            paginator = sc_client.get_paginator('describe_instances')
            for response in paginator.paginate():
                #print('eddddd',str(response))
                i=0

                if response['Reservations']:
                    lenr=len(response['Reservations'])
                    for i in range(0, lenr):
                        instance_reserv = response['Reservations'][i]['Instances']
                        if instance_reserv:
                            for resp in instance_reserv:
                                lifecycle = 'No Lifecycle Tag'
                                ownertag = "No Owner Tag"
                                departmenttag = "No Department Tag"
                                fundnotag = "No Fund Number Tag"
                                runschedule ="Not Run Schedule Tag"
                                if resp.get('Tags','NA')!='NA':
                                    for tag in resp['Tags']:
                                        tmp=str(tag['Key']).casefold()
                                        if (str(tag['Key']).casefold()).find('life'.casefold())!=-1 or (str(tag['Key']).casefold()).find('lifecycle'.casefold())!=-1:
                                            lifecycle=tag['Value']
                                        if (str(tag['Key']).casefold()).find('owner'.casefold())!=-1:
                                            ownertag=tag['Value']
                                            ownertag=ownertag.replace(",","&")
                                        if (str(tag['Key']).casefold()).find('department'.casefold())!=-1:
                                            departmenttag=tag['Value']
                                            departmenttag=departmenttag.replace(",","&")
                                        if (str(tag['Key']).casefold()).find('fund'.casefold())!=-1:
                                           fundnotag=tag['Value']
                                           fundnotag=fundnotag.replace(",","&")
                                        if (str(tag['Key']).casefold()).find('runschedule'.casefold())!=-1 or (str(tag['Key']).casefold()).find('run schedule'.casefold())!=-1:
                                           runschedule=tag['Value']
                                           runschedule=runschedule.replace(",","&")

                                #print(str(resp))
                                #fout.write(str(resp))

                                out_format="{:15},{:30},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:7}".format(account,sessinfo['name'],
                                resp['InstanceId'],resp['ImageId'],resp['InstanceType'],
                                resp.get('KeyName','NA'),
                                resp.get('StateTransitionReason','NA'),
                                resp.get('PublicIpAddress','NA'),
                                resp.get('PrivateIpAddress','NA'),
                                #,resp['State'],resp['StateTransitionReason'])
                                resp.get('VpcId','NA'),
                                resp['State']['Name'],
                                resp.get('Architecture','NA'),
                                resp.get('Platform','NA'),(str(resp.get('LaunchTime','NA'))),lifecycle,ownertag,departmenttag,fundnotag,runschedule)

                                #out_format="{:15},{:30},{:15}".format(resp['StateTransitionReason'],
                                #           resp['VpcId'],resp.get('Architecture','NA'))

                            #fout.write(str(resp))

                                #fout.write(str(resp))
                                print(out_format)
                                fout.write(out_format + '\n')


                    else:
                            print('No Instance Found')
        except:
            print("Error getting Instance")
            raise




def list_users(subaccount='all'):


    Account_Session.initialize_all()
    fout=open(cost_dir+'list_user' + '_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:15},{:25},{:20},{:6},{:20},{:20},{:20},{:20},{:20},{:20},{:20},{:20},{:20}\n".format('Account','AccountName','User Name','Creation Date','Password Last Used','AdministratorAccess','Access Key 1',
                                'Access Key 2',
                                'Access Key 1 Status',
                                'Access Key 2 Status',
                                'Access Key 1 Date Created',
                                'Access Key 2 Date Created',
                                'Access Key 1 Last Used',
                                'Access Key2 Last Used','UserGroups'))


    for account,sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding List Of User on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n'))
        sc_client = sessinfo['session'].client('iam', region_name="us-east-1")

        try:
            paginator = sc_client.get_paginator('list_users')
            for response in paginator.paginate():
                for resp in response['Users']:
                    paginator2 = sc_client.get_paginator('list_access_keys')
                    accesskey1="NA"
                    accesskey2="NA"
                    accesskey1_status="NA"
                    accesskey2_status="NA"
                    accesskey1_created = "NA"
                    accesskey2_created = "NA"
                    accesskey1_lastused="NA"
                    accesskey2_lastused="NA"
                    AdministratorAccess='False'
                    UserGroups=""
                    for keys in paginator2.paginate(UserName=resp['UserName']):
                        if (len(keys['AccessKeyMetadata'])) == 1:

                            accesskey1 = keys['AccessKeyMetadata'][0]['AccessKeyId']
                            accesskey1_status = keys['AccessKeyMetadata'][0]['Status']
                            accesskey1_created = keys['AccessKeyMetadata'][0]['CreateDate'].strftime(
                                    "%Y-%m-%d %H:%M")
                            tmp = sc_client.get_access_key_last_used(AccessKeyId=keys['AccessKeyMetadata'][0]['AccessKeyId'])
                            if tmp['AccessKeyLastUsed'].get('LastUsedDate', 'NA') != 'NA':
                                accesskey1_lastused = tmp['AccessKeyLastUsed']['LastUsedDate'].strftime( "%Y-%m-%d %H:%M")
                        elif (len(keys['AccessKeyMetadata'])) == 2:

                            accesskey1 = keys['AccessKeyMetadata'][0]['AccessKeyId']
                            accesskey2 = keys['AccessKeyMetadata'][1]['AccessKeyId']
                            accesskey1_status = keys['AccessKeyMetadata'][0]['Status']
                            accesskey2_status = keys['AccessKeyMetadata'][1]['Status']
                            accesskey1_created = keys['AccessKeyMetadata'][0]['CreateDate'].isoformat()#.strftime("%Y-%m-%d %H:%M")
                            accesskey2_created = keys['AccessKeyMetadata'][1]['CreateDate'].isoformat()#.strftime("%Y-%m-%d %H:%M")
                            tmp = sc_client.get_access_key_last_used(AccessKeyId=keys['AccessKeyMetadata'][0]['AccessKeyId'])
                            if tmp['AccessKeyLastUsed'].get('LastUsedDate', 'NA') != 'NA':
                                accesskey1_lastused = tmp['AccessKeyLastUsed']['LastUsedDate'].isoformat()#.strftime("%Y-%m-%d %H:%M")
                            tmp2 = sc_client.get_access_key_last_used(AccessKeyId=keys['AccessKeyMetadata'][1]['AccessKeyId'])
                            if tmp2['AccessKeyLastUsed'].get('LastUsedDate', 'NA') != 'NA':
                                accesskey2_lastused = tmp2['AccessKeyLastUsed']['LastUsedDate'].isoformat()#.strftime("%Y-%m-%d %H:%M")

                    #print (str(resp))
                                #print(resp['UserName'],',',resp['PasswordLastUsed'])
                    #out_format="{:15},{:20},{:15},{:25},{:20}".format(account,sessinfo['name'],resp['UserName'],str(resp['CreateDate']),resp.get('PasswordLastUsed','never used'))
                    if resp.get('PasswordLastUsed','NA') != 'NA':
                        pwd_last_used=resp['PasswordLastUsed'].strftime("%Y-%m-%d %H:%M")
                    else:
                        pwd_last_used='NA'
                    policies = sc_client.get_paginator('list_attached_user_policies')
                    for policy in policies.paginate(UserName=resp['UserName']):
                        for pol in policy['AttachedPolicies']:
                            #print(pol['PolicyName'])
                            if pol['PolicyName'] == "AdministratorAccess":
                                AdministratorAccess ='True'

                    groups_attached = sc_client.get_paginator('list_groups_for_user')
                    for groups in groups_attached.paginate(UserName=resp['UserName']):
                        if groups['Groups']:
                           first_group=True
                           for group in groups['Groups']:
                                if first_group==True:
                                    UserGroups=group['GroupName']
                                    first_group=False
                                else:
                                    UserGroups=UserGroups+' & '+ group['GroupName']
                                group_policies = sc_client.get_paginator('list_attached_group_policies')
                                for group_policy in group_policies.paginate(GroupName=group['GroupName']):
                                    #print(group_policy)
                                    for attached_policy in group_policy['AttachedPolicies']:
                                       #print(attached_policy['PolicyName'])
                                        if attached_policy['PolicyName']=='AdministratorAccess':
                                            AdministratorAccess='True'
                                            break
                        else:
                            UserGroups="None"

                    print(UserGroups)
                    out_format="{:15},{:20},{:15},{:25},{:20},{:6},{:20},{:20},{:20},{:20},{:20},{:20},{:20},{:20},{:20}".format(account,sessinfo['name'],resp['UserName'],str(resp['CreateDate'].strftime("%Y-%m-%d %H:%M")),pwd_last_used,
                                                                                                                      AdministratorAccess,
                                                                                                                      accesskey1,
                                                                                                                      accesskey2,
                                                                                                                      accesskey1_status,
                                                                                                                      accesskey2_status,
                                                                                                                      accesskey1_created,
                                                                                                                      accesskey2_created,
                                                                                                                      accesskey1_lastused,
                                                                                                                      accesskey2_lastused,UserGroups)
                                                                                                                      #PasswordLastUsed

                    print(out_format)
                    fout.write(out_format + '\n')




        except:
            print("Error getting")
            raise







def list_natgateway():
    print ("Finding Nat Gateway IP address" )



    fout=open(cost_dir+'list_natgateway' + '_info_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:30},{:15},{:15},{:15} \n".format('Account','AccountName','Nat Gateway Public IP','Subnet Id','VPC ID'))



    Account_Session.initialize_all()
    try:

        for account,sessinfo in Account_Session.SESS_DICT.items():
            print("checking nat gateway on account : "  + account)
            client=sessinfo['session'].client('ec2',region_name="us-east-1")
            natgatewaylist=client.describe_nat_gateways()['NatGateways']
            for natg in natgatewaylist:


                #fout.write("{:15},{:30},{:15},{:15},{:15} \n".format('Account','AccountName','Nat Gateway Public IP','Subnet Id','VPC ID'))
                out_format="{:15},{:30},{:15},{:15},{:15}".format(account,sessinfo['name'],natg['NatGatewayAddresses'][0]['PublicIp'],natg['SubnetId'],natg['VpcId'])

                print(out_format)
                fout.write(out_format + '\n')


                #print "Nat-Gaweway IP " + natg['NatGatewayAddresses'][0]['PublicIp '] + ' On VPC :  ' + natg['VpcId']
                #print("Nat " + str(natg['NatGatewayAddresses'][0]['PublicIp']),natg['SubnetId'],natg['VpcId'])
                #Nat [{u'PublicIp': '3.223.101.188', u'NetworkInterfaceId': 'eni-0c5d59863fe1e78cd', u'AllocationId': 'eipalloc-0bfb8fcd5b89c4517', u'PrivateIp': '10.70.76.134'}]



    except Exception as err:
        print(str(err))
        raise


def return_value(dict, key):
    for d in dict:
        if d['Key'] == key:
            return d['Value']
    return "unknown"


def list_all_account_vpn():
    print (" ls")

    fout = open(cost_dir + 'list_all_account_vpn' + '_info_' + date + '.txt', 'w')
    endtime = datetime.datetime.utcnow()
    starttime = endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30}\n"
               .format('Account', 'AccountName', 'AWS VPN NAME', 'Customer Gateway','AWS VPN ID', 'Tunnel state','Tunnel 1 Endpoint', 'Tunnel 1 Status', 'Tunnel 1 status change',
                       'Tunnel 2 Endpoint', 'Tunnel 2 Status', 'Tunnel 2 status change'))

    Account_Session.initialize_all()
    try:

        for account, sessinfo in Account_Session.SESS_DICT.items():
            print("Fetching VPN details on  : " + account)
            ec2 = sessinfo['session'].client('ec2', region_name="us-east-1")
            num_connections = 0
            tunnels = ec2.describe_vpn_connections()['VpnConnections']
            for tunnel in tunnels:
                if tunnel['State'] == 'available':
                    num_connections += 1
                    active_tunnels = 0
                    if tunnel['VgwTelemetry'][0]['Status'] == 'UP':
                        active_tunnels += 1
                    if tunnel['VgwTelemetry'][1]['Status'] == 'UP':
                        active_tunnels += 1

                    print("AWS VPN Name:", return_value(tunnel['Tags'], 'Name'))
                    VPN_Name = return_value(tunnel['Tags'], 'Name')
                    #print("  AWS VPN ID: " + tunnel['VpnConnectionId'])

                    response = ec2.describe_customer_gateways(
                        CustomerGatewayIds=[
                            tunnel['CustomerGatewayId'],
                        ])
                    cgw = response['CustomerGateways'][0]['IpAddress']
                    print("  Customer Gateway IP: " + response['CustomerGateways'][0]['IpAddress'])
                    #print("  AWS VPN State:  " + tunnel['State'])
                    Route = tunnel['Routes']
                    hh = []
                    for x in Route:
                        for k, v in x.items():
                            hh.append('  ' + k + ': ' + v + '  ')
                    print("\n".join(hh))
                    Time = tunnel['VgwTelemetry']
                    subtitle = []
                    for value in Time:
                        subtitle.append(value['LastStatusChange'])
                    #print("      Tunnel 1 Endpoint: " + tunnel['VgwTelemetry'][0]['OutsideIpAddress'])
                    #print("      Tunnel 1 Status: " + tunnel['VgwTelemetry'][0]['Status'])
                    print("      Status Change 1: ", str(subtitle[0]))
                    #print("      Tunnel 2 Endpoint: " + tunnel['VgwTelemetry'][1]['OutsideIpAddress'])
                    #print("      Tunnel 2 Status: " + tunnel['VgwTelemetry'][1]['Status'])
                    print("      Status Change 2: ",str(subtitle[1]))
                                #print(" ")


                out_format = "{:15},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30},{:30}".\
                            format(account, sessinfo['name'], VPN_Name, cgw, tunnel['VpnConnectionId'], tunnel['State'], tunnel['VgwTelemetry'][0]['OutsideIpAddress'], tunnel['VgwTelemetry'][0]['Status'],
                                   str(subtitle[0]), tunnel['VgwTelemetry'][1]['OutsideIpAddress'], tunnel['VgwTelemetry'][1]['Status'], str(subtitle[1]))

                print(out_format)
                fout.write(out_format + '\n')

    except Exception as err:
        print(str(err))
        raise

def unused_secgroup(region,delete=False):
    print("Finding unused Security Group ..")

    print("reg " + region)
    Account_Session.initialize()
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print("checking account : "  + account)
            client=sessinfo['session'].client('ec2')

            regions_dict = client.describe_regions()

            region_list = [region['RegionName'] for region in regions_dict['Regions']]

            # parse arguments


            client=sessinfo['session'].client('ec2')
            ec2 = sessinfo['session'].resource('ec2')
            all_groups = []
            security_groups_in_use = []
            # Get ALL security groups names
            security_groups_dict = client.describe_security_groups()
            security_groups = security_groups_dict['SecurityGroups']
            for groupobj in security_groups:
                if groupobj['GroupName'] == 'default' or groupobj['GroupName'].startswith('d-') or groupobj['GroupName'].startswith('AWS-OpsWorks-'):
                    security_groups_in_use.append(groupobj['GroupId'])
            all_groups.append(groupobj['GroupId'])

            # Get all security groups used by instances
            instances_dict = client.describe_instances()
            reservations = instances_dict['Reservations']
            network_interface_count = 0

            for i in reservations:
                for j in i['Instances']:
                    for k in j['SecurityGroups']:
                        if k['GroupId'] not in security_groups_in_use:
                            security_groups_in_use.append(k['GroupId'])

            # Security Groups in use by Network Interfaces
            #eni_client = boto3.client('ec2', region_name=args.region)
            eni_dict = client.describe_network_interfaces()
            for i in eni_dict['NetworkInterfaces']:
                for j in i['Groups']:
                    if j['GroupId'] not in security_groups_in_use:
                        security_groups_in_use.append(j['GroupId'])

            # Security groups used by classic ELBs
            elb_client = sessinfo['session'].client('elb')
            elb_dict = elb_client.describe_load_balancers()
            for i in elb_dict['LoadBalancerDescriptions']:
                for j in i['SecurityGroups']:
                    print("SEC GROUP In Use " + str())
                    if j not in security_groups_in_use:
                        security_groups_in_use.append(j)

            # Security groups used by ALBs
            elb2_client = sessinfo['session'].client('elbv2')
            elb2_dict = elb2_client.describe_load_balancers()
            for i in elb2_dict['LoadBalancers']:
                #for j in i['SecurityGroups']:
                for j in i.get('SecurityGroups','NA'):
                    if j not in security_groups_in_use:
                        security_groups_in_use.append(j)

            # Security groups used by RDS
            rds_client = sessinfo['session'].client('rds')
            rds_dict = rds_client.describe_db_instances()
            for i in rds_dict['DBInstances']:
                for j in i['VpcSecurityGroups']:
                    if j['VpcSecurityGroupId'] not in security_groups_in_use:
                        security_groups_in_use.append(j['VpcSecurityGroupId'])
            print("SEC GROUP In Use " + str())



            delete_candidates = []
            for group in all_groups:
                if group not in security_groups_in_use:
                    print(str(delete_candidates))
                    delete_candidates.append(group)

            if delete:
                print("We will now delete security groups identified to not be in use.")
                for group in delete_candidates:
                    security_group = ec2.SecurityGroup(group)
                    try:
                        ##security_group.delete()
                        print("DDDDDD")
                    except Exception as e:
                        print(e)
                        print(("{0} requires manual remediation.".format(security_group.group_name)))
            else:
                print("The list of security groups to be removed is below.")
                print("Run this again with `-d` to remove them")
                for group in sorted(delete_candidates):
                    print(("   " + group))

            print("---------------")
            print("Activity Report")
            print("---------------")

            print(("Total number of Security Groups evaluated: {0:d}".format(len(all_groups))))
            print(("Total number of EC2 Instances evaluated: {0:d}".format(len(reservations))))
            print(("Total number of Load Balancers evaluated: {0:d}".format(len(elb_dict['LoadBalancerDescriptions']) +
                                                                            len(elb2_dict['LoadBalancers']))))
            print(("Total number of RDS Instances evaluated: {0:d}".format(len(rds_dict['DBInstances']))))
            print(("Total number of Network Interfaces evaluated: {0:d}".format(len(eni_dict['NetworkInterfaces']))))
            print(("Total number of Security Groups in-use evaluated: {0:d}".format(len(security_groups_in_use))))
            if delete:
                print(("Total number of Unused Security Groups deleted: {0:d}".format(len(delete_candidates))))
            else:

                print(("Total number of Unused Security Groups targeted for removal: {0:d}".format(len(delete_candidates))))

    except Exception as err:
        print("error .." + str(err))
        raise


def eiplistallsub(eip):




    client = boto3.client('organizations')
    for account in paginate(client.list_accounts):
        #print "result  " + str(account['Id'])

        print(account['Id'], account['Name'], account['Arn'])
        ###     #if account['Id'] != rootaccount:
        if account['Id'] != rootaccount and "suspend" not in  account['Status'].lower():

            client_sess = getsession(account)
            #clientcf=client_sess.client('cloudformation')
            sc_client=client_sess.client('ec2', region_name='us-east-1')
            try:
                response = sc_client.describe_addresses()
                #print str(response)
                for addr in  response['Addresses']:
                    #print "addr " + str(addr)
                    print("Public IP : " + addr['PublicIp'])
                    #print("Public IP : " + addr['PublicIP'])
                    print(("Instance ID : " + addr.get('InstanceId','NA')))
                    print(("AssociationId :" + addr.get('AssociationId','NA')))
                    if eip == addr['PublicIp']:
                        print("Found in " + account['Id'])
                        inp=input('continue')
            except Exception as errp:
                print(("Error getting" + str(errp)))







if __name__ == '__main__':
    main()
