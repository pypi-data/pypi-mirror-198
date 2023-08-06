#from .global_var import *
from dops_util import *
from dops_util.cw import *

def check_instance_type(type='All'):
    format_date=format = "%Y-%m-%dT%H:%M:%S"
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    # fout.write("Account,Account_name,Instance ID,Instance Name, Instance Type  , State, Spot_Insta_Req_Id,state_reason,capacity_reservation_id ,cpu_max_util_last_3_month\n")
    # fout.write("Account,Account_name,Instance ID,Instance Name,LifeCycle,Instance Type  , State, Spot_Insta_Req_Id,state_reason,capacity_reservation_id ,cpu_max_util_last_3_month,image_id,ebs_attached,ebs_total_size\n")


    if type != 'All':
        Account_Session.build_sess_subaccount(type)
        fout=open(cost_dir+'ec2_list_'+ type + '_' + date+'.txt','w')

    else:
        fout=open(cost_dir+'ec2_list_'+ date+'.txt','w')
        Account_Session.initialize_all()

    fout.write("Account,Account_name,Instance ID,Instance Name,LifeCycle,Instance Type  , State, Spot_Insta_Req_Id,state_reason,capacity_reservation_id ,cpu_max_util_last_3_month,image_id,ebs_attached,ebs_total_size\n")

    print("################Checking EC2 Instance  ################")
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Checking Instances  on account : ' + account + ' ============================\n\n\n'))



            # Define the connection
            ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
            ec2_client = sessinfo['session'].client('cloudwatch', region_name="us-east-1")

            volume_iterator = ec2.volumes.all()
            ebs_array={}
            for vol in volume_iterator:

                ebs_tmp={'type':vol.volume_type,'size':vol.size,'state':vol.state}
                # print("VOL IN",vol.volume_id,vol.volume_type,vol.size,vol.state)
                ebs_array.update({vol.volume_id:ebs_tmp})

            response = ec2.instances.all()
            for inst in  response:
                ebs_usage=inst.block_device_mappings
                ebs_attached=[]
                ebs_total_size=0
                for ebs in ebs_usage:

                    ebs_vol_id=ebs['Ebs']['VolumeId']
                    print("EBS",ebs['DeviceName'],ebs_vol_id,
                          ebs_array[ebs_vol_id]['type'],ebs_array[ebs_vol_id]['size'],ebs_array[ebs_vol_id]['state'])
                    ebs_total_size += ebs_array[ebs_vol_id]['size']
                    ebs_attached_tmp=[ebs['DeviceName'],ebs_vol_id,
                                             ebs_array[ebs_vol_id]['type'],ebs_array[ebs_vol_id]['size'],
                                             ebs_array[ebs_vol_id]['state']]
                    ebs_attached.append(ebs_attached_tmp)
                ebs_attached_flat = [str(item) for sublist in ebs_attached for item in sublist]
                # print('ebs attaced app',ebs_attached_flat,";".join(ebs_attached_flat))

                ebs_attached_flat_join = ";".join(ebs_attached_flat)

                # print('ebs attaced app',ebs_attached_flat_join)
                if inst.tags:
                    tag_lifecycle_value = 'None'
                    tag_name_value='None'
                    for tag in inst.tags:
                        if tag['Key'].lower() == 'lifecycle':
                            #tag_lifecycle = 'lifecycle'
                            tag_lifecycle_value = tag['Value']
                        if tag['Key'].lower() == 'name':
                            #tag_lifecycle = 'lifecycle'
                            tag_name_value = tag['Value']

                if type == 'spot':
                    if inst.spot_instance_request_id:
                        print(("Instance ID, {}, Instance Type, {}  , State, {}, Spot_Insta_Req_Id, {},state_reason , {},capacity_reservation_id ,{}".format( inst.instance_id,inst.instance_type,inst.state,inst.spot_instance_request_id,inst.state_reason,inst.capacity_reservation_id)))
                elif type == 'standard':
                    if not inst.spot_instance_request_id:
                        cpu_max_util=get_cw_metric(ec2_client,inst.instance_id,starttime,endtime)
                        print(("Instance ID,{}, Instance Type,{}  , State,{}, Spot_Insta_Req_Id,{},state_reason ,{},capacity_reservation_id ,{},cpu_max_util".format( inst.instance_id,inst.instance_type,inst.state,inst.spot_instance_request_id,inst.state_reason,inst.capacity_reservation_id,cpu_max_util)))
                else:
                    cpu_max_util=get_cw_metric(ec2_client,inst.instance_id,starttime,endtime)
                    if not cpu_max_util:
                        cpu_max_util='0.111111'
                    # print(("Account,{},Account_Name,{},Instance ID,{},Instance Name,{}, Instance Type,{}  , State,{}, Spot_Insta_Req_Id,{},state_reason ,{},capacity_reservation_id ,{},cpu_max_util_last_3_month,{}".format(account,sessinfo['name'] , inst.instance_id,tag_name_value,inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,'NA',inst.capacity_reservation_id,cpu_max_util)))
                    # fout.write("{},{},{},{},{},{},{} ,{},{},{}\n".format(account,sessinfo['name'] , inst.instance_id,tag_name_value,inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,'NA',inst.capacity_reservation_id,cpu_max_util))
                    print(("Account,{},Account_Name,{},Instance ID,{},Instance Name,{},LifeCycle,{},Instance Type,{}  ,"
                           " State,{}, Spot_Insta_Req_Id,{},state_reason ,{},capacity_reservation_id ,{},"
                           "cpu_max_util_last_3_month,{},image_id,{},ebs_attached,{},ebs_total_size,{}".format(account,sessinfo['name'] ,
                            inst.instance_id,tag_name_value,tag_lifecycle_value,inst.instance_type, inst.state.get('Name','NA'),
                            inst.spot_instance_request_id,'NA',inst.capacity_reservation_id,cpu_max_util,inst.image_id,ebs_attached_flat_join,ebs_total_size)))
                    fout.write("{},{},{},{},{},{},{} ,{},{},{},{},{},{}\n".format(account,sessinfo['name'] , inst.instance_id,tag_name_value,tag_lifecycle_value,
                                                                               inst.instance_type,inst.state.get('Name','NA'),inst.spot_instance_request_id,
                                                                               'NA',inst.capacity_reservation_id,cpu_max_util,ebs_attached_flat_join,ebs_total_size))



    except Exception as errp:
        print(("Error getting" + str(errp)))
        raise
