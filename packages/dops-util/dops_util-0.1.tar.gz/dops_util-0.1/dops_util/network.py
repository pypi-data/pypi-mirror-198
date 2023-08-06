from dops_util import *

def list_subnet_route():

    fout = open(cost_dir + "list_subnet_route_info_" + date + ".txt", "w")
    format_date = format = "%Y-%m-%dT%H:%M:%S"
    endtime = datetime.datetime.utcnow()
    starttime = endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:20},{:15},{:20},{:25},{:25},{:15},{:25},{:25},{:25},{:25},{:25},{:15},{:15}\n".format('Account',
                                                                                                  'AccountName','VpcId',
                                                                                                'Route Table ID',
                                                                                      'Target Type',
                                                                                      'TargetId',
                                                                                      'DestinationId',
                                                                                     'DestinationType',
                                                                                            'Origin',
                                                                                            'State',
                                                                                            'SubnetId',
                                                                                            'RouteTableAssociationId',
                                                                                            'Is Associated with Main',
                                                                                                        'Association State','region'))

    print("################ Getting list subnet route Info ################")
    Account_Session.initialize_all()
    try:
        for account,sessinfo in Account_Session.SESS_DICT.items():
            print(('\n\n\n====================Finding List Of Route Tables on account : ' + account + ":" +
                   sessinfo['name'] + ' ============================\n\n\n'))
            regions=['us-east-1','eu-central-1','ap-south-1']
            for region in regions:

                sc_client = sessinfo['session'].client('ec2', region_name=region)

                potentialtargets=['GatewayId', 'NatGatewayId', 'TransitGatewayId', 'InstanceId', 'LocalGatewayId',
                                  'CarrierGatewayId', 'NetworkInterfaceId','VpcPeeringConnectionId']
                potentialDestinations=['DestinationPrefixListId', 'DestinationCidrBlock', 'DestinationIpv6CidrBlock']

                #only current target is returned, calling target that isn't there results in key error, creating list of potential targets
                paginator=sc_client.get_paginator('describe_route_tables')
                for response in paginator.paginate():
                    #looping through route tables
                    resp = response['RouteTables']
                    if resp:
                        for re in resp:
                            current=0;
                            while current < len(re['Routes']):
                                # looping through routes in route tables
                                targetType = ''
                                targetID = ''
                                DestinationType = ''
                                DestinationId = ''
                                for target in potentialtargets:
                                    # finding which target the current route has
                                    try:
                                        targetID = re['Routes'][current][target]
                                        targetType = target
                                    except:
                                        continue
                                for potentialDestination in potentialDestinations:
                                    # finding which target the current route has
                                    try:
                                        DestinationId = re['Routes'][current][potentialDestination]
                                        DestinationType = potentialDestination
                                    except:
                                        continue
                                # if re['Associations'][0]['Main'] == 0:
                                #     # if associated to main route table no subnetID will be returned
                                #     # checking that association to main is false (0) before checking + joining subnetids into list
                                #     subnets = [group['SubnetId'] for group in re['Associations']]
                                #     isMain = False
                                #     sub = ";".join(subnets)
                                # else:
                                #     isMain = True
                                #     sub = "NA"
                                #     # Returning if Main is true
                                sub = ""
                                try:
                                    if re['Associations'][0]['Main'] == 0:
                                        isMain = False
                                    else:
                                       isMain = True

                                except:
                                    print("error getting association to main")
                                for i in range(len(re['Associations'])):
                                    try:
                                        sub = sub+re['Associations'][i]['SubnetId']+";"
                                    except:
                                        sub = sub+""
                                #if re['Associations'][0]['AssociationState']['State']!="associated":
                                try:
                                    associationid=re['Associations'][0]['RouteTableAssociationId']
                                except:
                                    associationid="NA"

                                try:
                                    associationstate=re['Associations'][0]['AssociationState']['State']

                                except:
                                    associationstate="NA"
                                out_format = ("{:15},{:20},{:20},{:15},{:20},{:25},{:25},{:15},{:25},{:25},{:25},{:25},"
                                              "{:25},{:15},{:15}" .format(
                                                  account,
                                                  sessinfo['name'],
                                                  re['VpcId'],
                                                  re['RouteTableId'],
                                                  targetType,
                                                    targetID,
                                                  DestinationId,
                                                  DestinationType,
                                                  re['Routes'][current]['Origin'],
                                                  re['Routes'][current]['State'],
                                                  sub,
                                                  #re['Associations'][0]['RouteTableAssociationId'],
                                                  associationid,
                                                  isMain,
                                                  associationstate,
                                                  region
                                                  #re['Associations']['AssociationState']['State']
                                                    ))

                                print(out_format)
                                fout.write(out_format + '\n')
                                current=current+1

                    # else:
                    #     print("Not found in "+region)
    except:
        print("Error getting Route Tables")
        raise


def list_all_ip(type="ALL"):

    format_date = format = "%Y-%m-%dT%H:%M:%S"
    endtime = datetime.datetime.utcnow()
    starttime = endtime - datetime.timedelta(hours=int(2160))

    if type != 'All':
        Account_Session.build_sess_subaccount(type)
        fout = open(cost_dir + "list_all_ip_info_" + type + '_' +  date + ".txt", "w")

    else:
        fout = open(cost_dir + "list_all_ip_info_" + date + ".txt", "w")
        Account_Session.initialize_all()

    print("################ Getting IPs Info ################")
    # Account_Session.get_account_list()


    fout.write("{:15},{:20},{:17},{:17},{:15},{:10},{:10},{:20},{:6},{:30},{:20},{:40}\n".format('Account','AccountName','PrivateIp','Public_Ip',
                                                                                   'InterfaceType','NetworkInterfaceId','Status','SubnetId',
                                                                                   'SourceDestCheck','Security_Group','Vpc_Id','Description'))


    for account,sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding List Of All IP    on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n'))
        sc_client = sessinfo['session'].client('ec2', region_name="us-east-1")

        try:
            paginator = sc_client.get_paginator('describe_network_interfaces')
            for response in paginator.paginate():
                for ni in response["NetworkInterfaces"]:
                    #print (str(ni))
                    #interface_id = network_interface["NetworkInterfaceId"]
                    #interface_typ
                    sec_group=[ group['GroupId'] for group in ni['Groups']]
                    #print (";". join(sec_group))
                    sg= ";". join(sec_group)
                    public_ip='NA'
                    if ni.get('Association','NA') != 'NA':
                        #print('assso   ',ni['Association']['PublicIp'])
                        public_ip=ni['Association']['PublicIp']
                        print ('pub ip ',public_ip)
                    # print ("DDD ",ni['Description'])
                    #out_format="{:15},{:20},{:15},{:15}".format(account,sessinfo['name'],ni[0]['GroupName']['GroupId'],ni['InterfaceType'],ni['NetworkInterfaceId'])
                    out_format="{:15},{:20},{:17},{:17},{:15},{:10},{:10},{:20},{:6},{:30},{:20},{:40}".format(account,sessinfo['name'],ni['PrivateIpAddress'],public_ip,
                                                                            ni['InterfaceType'],ni['NetworkInterfaceId'],ni['Status'],ni['SubnetId'],
                                                                            str(ni['SourceDestCheck']),sg,ni['VpcId'],ni['Description'])
                    print (out_format)
                    fout.write(out_format + '\n')


    # '''
#                     if "Association" in network_interface:
#                         if is_sema4_account_id(network_interface["Association"]["IpOwnerId"]):
#                             eip = network_interface["Association"]["PublicIp"]
#                             # owner_id = network_interface["Association"]["IpOwnerId"]
#                             owner_id = network_interface["OwnerId"]
#                             attachment_status = network_interface["Attachment"]["Status"]
#                             if network_interface["Status"] == "in-use":
#                                 print(
#                                     f"--> This EIP [{eip}] is [{attachment_status}] and in use in [{owner_id}] = [{aws_account_number}], interface-id {interface_id}"
#                                 )
#                             else:
#                                 interface_id = network_interface["NetworkInterfaceId"]
#                                 print(
#                                     f"---STATUS is NOT IN-USE--- {str(interface_id)}")
#                                 print(
#                                     f"-->>> This EIP [{eip}] is [{attachment_status}] and is NOT in use in [{owner_id}]= [{aws_account_number}], interface-id {interface_id}"
#                                 )
#                         else:
#                             print(
#                                 "These EIPs should be reviewed manually to see if they're really are EIPs or just owned by Amazon or ELB etc...."
#                             )
#                             eip = network_interface["Association"]["PublicIp"]
#                             print(
#                                 f"------>>>>This EIP {eip} should be reviewed MANUALLY")
#             # print(response)
#
#             # print(("Account,{},Instance ID,{}, Instance Type,{}  , State,{}, Spot_Insta_Req_Id,{},state_reason ,{},capacity_reservation_id ,{},cpu_max_util,{}".format(sessinfo['name'] , inst.instance_id,inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,inst.state_reason.get('Message','NA'),inst.capacity_reservation_id,cpu_max_util)))
#             # fout.write("Account,{},Instance ID,{}, Instance Type,{}  , State,{}, Spot_Insta_Req_Id,{},state_reason ,{},capacity_reservation_id ,{},cpu_max_util,{}\n".format(sessinfo['name'] , int.instance_id,inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,inst.state_reason.get('Message','NA'),inst.capacity_reservation_id,cpu_max_util))
#             # print(("Account,{},Account_Name,{},Instance ID,{},Instance Name,{}, Instance Type,{}  , State,{}, Spot_Insta_Req_Id,{},state_reason ,{},capacity_reservation_id ,{},cpu_max_util_last_3_month,{}".format(account,sessinfo['name'] , inst.instance_id,tag_name_value,inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,'NA',inst.capacity_reservation_id,cpu_max_util)))
#             # fout.write("{},{},{},{},{},{},{} ,{},{},{}\n".format(account,sessinfo['name'] , inst.instance_id,tag_name_value,inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,'NA',inst.capacity_reservation_id,cpu_max_util))
# '''
        except Exception as errp:
            print(("Error getting" + str(errp)))
            raise
def list_transit_gateway_route_tables():
    fout = open(cost_dir + 'list_transit_gateway_route_tables' + '_info_' + date + '.txt', 'w')
    endtime = datetime.datetime.utcnow()
    starttime = endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:30},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:5}\n".format('Account','region','TransitGatewayRouteTableId',
                                                                    'TransitGatewayId','State',
                                                                    'DefaultAssociationRouteTable',
                                                                    'DefaultPropagationRouteTable','TagsCount','Tags','RouteCount'))
    foutTG = open(cost_dir + 'list_transit_gateway_route_table_routes' + '_info_' + date + '.txt', 'w')
    endtimeTG = datetime.datetime.utcnow()
    starttimeTG = endtimeTG - datetime.timedelta(hours=int(2160))
    foutTG.write("{:35},{:35},{:35},{:35},{:35},{:35},{:35},{:35},{:15}\n".format('Account', 'region',
                                                                                  'TransitGatewayRouteTableId',
                                                                                  'DestinationCidrBlock', 'State',
                                                                                  'ResourceId',
                                                                                  'TransitGatewayAttachmentId',
                                                                                  'ResourceType', 'Type'))
    Account_Session.build_sess_subaccount('346997421618')
    TransitGtwRouteTables=[]
    regions = ['us-east-1', 'ap-south-1', 'eu-central-1']
    for account, sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding List Transit Gateway Route Tables on account : ' + account + ":" + sessinfo[
            'name'] + ' ============================\n\n\n'))

        for region in regions:
            sc_client = sessinfo['session'].client('ec2', region_name=region)
            try:
              paginator=sc_client.get_paginator('describe_transit_gateway_route_tables')
              #print("paginated")
              for responses in paginator.paginate():
                  #print(responses)
                  for response in responses['TransitGatewayRouteTables']:
                      tagCount=len(response['Tags'])
                      tags=""
                      for tag in range(tagCount):
                          tags="Key="+response['Tags'][tag]['Key']+"::Value="+response['Tags'][tag]['Value']+";"
                      Gate = response['TransitGatewayRouteTableId']
                      RouteCount = Transit_Gateway_Routes2(Gate, region, foutTG, account, sessinfo)
                      out_format=("{:15},{:30},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:5}".format(account, region,
                                  response['TransitGatewayRouteTableId'],
                                  response['TransitGatewayId'], response['State'],
                                  response['DefaultAssociationRouteTable'],
                                  response['DefaultPropagationRouteTable'],
                                  tagCount,
                                  tags,
                                  RouteCount
                                  ))
                      print(out_format)
                      fout.write(out_format + '\n')
                      #TransitGtwRouteTables.append(response['TransitGatewayRouteTableId'])




            except:
                print("error")
                raise

def Transit_Gateway_Routes2(Gate,region,foutTG,account,sessinfo):

    try:

        sc_client2 = sessinfo['session'].client('ec2', region_name=region)
        print("tgr2")
        routes = sc_client2.search_transit_gateway_routes(TransitGatewayRouteTableId=Gate,
                                                         Filters=[
                                                             {
                                                                 'Name': 'type',
                                                                 'Values': [
                                                                     'propagated', 'static',
                                                                 ]
                                                             }],
                                                                 MaxResults=600,
                                                         )

        for route in routes['Routes']:
            #print("Route", route)
            if route['State']=='blackhole':
                ResourceId="NA"
                TransitGatewayAttachmentId="NA"
                ResourceType="NA"
            else:
                ResourceId = (route['TransitGatewayAttachments'][0].get('ResourceId', 'Not Found'))
                ResourceType = route['TransitGatewayAttachments'][0].get('ResourceType', 'Not Found')
                TransitGatewayAttachmentId = route['TransitGatewayAttachments'][0].get('TransitGatewayAttachmentId','Not Found')
            TGout_format = ("{:35},{:35},{:35},{:35},{:35},{:35},{:35},{:35},{:15}".format(account, region,Gate,route['DestinationCidrBlock'],route['State'],
                                                                                         ResourceId,
                                                                                         TransitGatewayAttachmentId,
                                                                                         ResourceType,route['Type']
                                                                                         ))
            print(TGout_format)
            foutTG.write(TGout_format + '\n')
        return len(routes['Routes'])
    except:
        print("error getting routes")
        return "Error"

def list_security_groups():
    fout=open(cost_dir+'list_security_groups' + '_info_' + date + '.txt', 'w')
    endtime = datetime.datetime.utcnow()
    starttime = endtime - datetime.timedelta(hours=int(2160))
    regions=['us-east-1', 'ap-south-1', 'eu-central-1']
    fout.write("{:15},{:15},{:15},{:45},{:15},{:15},{:15},{:25},{:15}\n".format('Account','Account Name','Region','Description','GroupName','OwnerId','GroupId','Tags','VpcId'))

    Account_Session.initialize_all()
    for account, sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding security groups on account : ' + account + ":" +
               sessinfo['name'] + ' ============================\n\n\n'))
        for region in regions:
            sc_client=sessinfo['session'].client('ec2', region_name=region)
            paginator=sc_client.get_paginator('describe_security_groups')
            for secgroups in paginator.paginate():
                for secgroup in secgroups['SecurityGroups']:
                    TagsList=""
                    try:
                        for tag in range(len(secgroup['Tags'])):
                            TagsList = "Key=" + secgroup['Tags'][tag]['Key'] + "::Value=" + secgroup['Tags'][tag]['Value'] + ";"
                            TagsList=TagsList.replace(',',".")
                    except:
                        #print("no tags")
                        TagsList="None"
                    description =(str(secgroup['Description'])).replace(',',".")
                    groupname=description =(str(secgroup['GroupName'])).replace(',',".")
                    out_format = ("{:15},{:30},{:15},{:45},{:15},{:15},{:15},{:25},{:15}".format(account, sessinfo['name'],
                                                                                       region, description,
                                                                                       groupname,
                                                                                       secgroup['OwnerId'],
                                                                                       secgroup['GroupId'],
                                                                                       TagsList,
                                                                                       secgroup['VpcId']))
                    print(out_format)
                    fout.write(out_format+'\n')

def list_security_group_rules():
    fout = open(cost_dir + 'list_security_group_rules' + '_info_' + date + '.txt', 'w')
    endtime = datetime.datetime.utcnow()
    starttime = endtime - datetime.timedelta(hours=int(2160))
    regions = ['us-east-1', 'ap-south-1', 'eu-central-1']
    fout.write("{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:35},{:35},{:35},{:35},{:35},{:35},"
               "{:35},{:35}\n".format(
                 'Account','Account Name','Region','SecurityGroupRuleId','GroupId','GroupOwnerId','IsEgress',
                 'IpProtocol','FromPort','ToPort','CIDR','CIDR Type','Prefix List ID','Referenced Group Id',
                 'Referenced Group Peering Status',
                 'Referenced Group User Id','Referenced Group VPC Id','Referenced Group VPC Peering Id'))

    Account_Session.initialize_all()
    for account, sessinfo in Account_Session.SESS_DICT.items():
        print(('\n\n\n====================Finding security group rules on account : ' + account + ":" +
               sessinfo['name'] + ' ============================\n\n\n'))
        for region in regions:
            try:
                sc_client = sessinfo['session'].client('ec2', region_name=region)
                paginator = sc_client.get_paginator('describe_security_group_rules')
                for response in paginator.paginate():
                    for rule in response['SecurityGroupRules']:
                        ReferencedGroupInfoGroupId = "NA"
                        VpcPeeringConnectionId = "NA"
                        UserId = "NA"
                        VpcId = "NA"
                        PrefixListId = "NA"
                        CIDR="NA"
                        iptype="NA"
                        PeeringStatus="NA"
                        try:
                            iptype = "IPv4"
                            CIDR=rule['CidrIpv4']

                        except:
                            try:
                                type = "IPv6"
                                CIDR=rule['CidrIpv6']

                            except:
                                CIDR="Not Found"
                                iptype="Not Found"
                        try:
                            if rule['ReferencedGroupInfo']:
                                refGroup=True
                        except:
                            refGroup=False
                        if refGroup:
                            ReferencedGroupInfoGroupId= rule['ReferencedGroupInfo'].get('GroupId', "NA")
                            VpcPeeringConnectionId=rule['ReferencedGroupInfo'].get('VpcPeeringConnectionId', "NA")
                            UserId= rule['ReferencedGroupInfo'].get('UserId', "NA")
                            VpcId= rule['ReferencedGroupInfo'].get('VpcId', "NA")
                            PrefixListId= rule['ReferencedGroupInfo'].get('PrefixListId', "NA")
                            PeeringStatus=rule['ReferencedGroupInfo'].get('PeeringStatus','NA')

                        f_out=("{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:15},{:35},{:35},{:35},{:35},{:35},{:35},{:35},{:35}".format(
                            account,sessinfo['name'],
                                region,
                                rule['SecurityGroupRuleId'],
                                rule['GroupId'],
                                rule['GroupOwnerId'],
                                rule['IsEgress'],
                                rule['IpProtocol'], rule['FromPort'],
                                rule['ToPort'],CIDR,
                                iptype,
                                PrefixListId,ReferencedGroupInfoGroupId,
                                PeeringStatus,
                                UserId,
                                VpcId,
                                VpcPeeringConnectionId
                        ))
                        print(f_out)
                        fout.write(f_out+'\n')
            except:
                print("ERROR")


def list_elastic_ip(acc='All'):
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout=open(cost_dir+'elasticip_' +date+'.txt','w')


    fout.write("{:15}, {:20}, {:20},{:24},{:24},{:20},{:24}\n".format('Account','AccountName','Public_IP','AllocationId','AssociationId',
                                                                       'Network Int ID','PrivateIP'))


    #print (eip['PublicIp'],eip['AllocationId'],eip.get('AssociationId','NA'),eip.get('NetworkInterfaceId','NA'),eip.get('PrivateIpAddress','NA'))




    print("################Checking Elastic IP ################")
    Account_Session.initialize_all()
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Checking Elastic IP on account : ' + account + ' ============================\n\n\n'))

            ## Define the connection
            #ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
            ec2_client = sessinfo['session'].client('ec2', region_name="us-east-1")



            #response = ec2_client.list_portfolios()
            response = ec2_client.describe_addresses()

            for eip in response['Addresses']:
                #cdprint (eip['PublicIp'],eip['AllocationId'],eip.get('AssociationId','NA'),eip.get('NetworkInterfaceId','NA'),eip.get('PrivateIpAddress','NA'))
                #cp_metric=cw.get_metric_statistics(namespace, name, start, end, period, stat_types):
                out_format="{:15}, {:20}, {:20},{:24},{:24},{:20},{:24}".format (account,sessinfo['name'],eip['PublicIp'],eip['AllocationId'],eip.get('AssociationId','NA'),eip.get('NetworkInterfaceId','NA'),eip.get('PrivateIpAddress','NA'))

                #fout.write("{:15}, {:20}, {:20},{:8},{:24},{:15},{:10},{:24}\n".format('Account','AccountName','Public_IP','AllocationId','AssociationId',
                                                                                      # 'Network Int ID','PrivateIP'))


            #
                # out_format="{:15},{:30},{:15},{:8},{:24},{:15},{:10},{:24}".format(account,sessinfo['name'],ep['AvailabilityZone'],cpu_average_util,
                #                                                               ep['ReplicationInstanceClass'], ep['ReplicationInstanceStatus'],ep['AllocatedStorage'],
                #                                                               ep['ReplicationInstanceIdentifier'])
                print(out_format)
                fout.write(out_format + '\n')

    except Exception as err :
        print((traceback.format_exc()))
        print(("Finding  elastic ip  " + str(err)))


