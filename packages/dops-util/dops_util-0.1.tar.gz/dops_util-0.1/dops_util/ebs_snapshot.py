
from dops_util import *
from .ami import  *



def safeStr(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    #except: return ""


def convert_tag(var):
    tempat=''
    if var:
        for seq in var:
            for i,y in list(seq.items()):
                tempat = tempat  + " " + safeStr(y)
            tempat = tempat + ' : '
    return safeStr(tempat)



def delete_aging_snapshot_in_a_subaccount(args):
    v_except=[]
    print(("Checking Snaphost Exception Not To Be Deleted in file " + snapshot_except))
    if os.path.isfile(snapshot_except) and os.stat(snapshot_except).st_size != 0:
        f_except=open(snapshot_except,'r')
        for v in f_except:
            v_except.append(v.strip())
    else:
        print(('File Snapshot Exception ' + ebs_except + ' Does Not Exist or It is empty'))
    print(('Snapshot in Exception List  ' + str(v_except)))

    del_batch=[]
    datenow=datetime.datetime.now(utc)

    Account_Session.build_sess_subaccount(args[0])
    sess=Account_Session.SESS_DICT[args[0]]
    ec2 = sess['session'].resource('ec2', region_name="us-east-1")
    ec2_sess = sess['session'].client('ec2', region_name="us-east-1")
    ct =  sess['session'].client('cloudtrail', region_name="us-east-1")
    if args[4] == 'not_validate_ami':
        validate_ami=False
    else:
        validate_ami=True

    resp=ec2.snapshots.filter(OwnerIds=['self'])
    array_all_list=get_aging_snapshot(ec2,ec2_sess,ct,resp,args[0],sess['name'],v_except,validate_ami)
    # print("Array All List",str(array_all_list))
    print(('adding Snapshot  into batch to be deleted of snapshot older than ' + str(age) + ' where condition  ' + args[2] + " == " + args[3]))

    for snap_dict in array_all_list:
        try:
            snap=ec2.Snapshot(snap_dict['SnapshotId'])
            tag_lifecycle_value = 'None'
            tag_name_value = 'None'
            if snap.tags:
                for tag in snap.tags:
                    if tag['Key'].lower() == 'lifecycle':
                        tag_lifecycle_value = tag['Value']
                    if tag['Key'].lower() == 'name':
                        tag_name_value = tag['Value']

            if   tag_lifecycle_value.lower() != 'forever':
                if args[1] == 'BATCH_DELETE':
###If volume_orphan is AMI_Sn, it means the snapshot is attached to an AMI and won't be deleted
###the args(2) and args(3) when executed : volume_orphan AMI_Sn , the snapshot will be inserted into del_batch
##args[3] InBetween , No and AMI_Sn
                    if snap_dict[args[2]] == args[3]:
                        if snap.snapshot_id  in v_except:
                            print(("This snapshot " + snap.snapshot_id + " IS in exception, so it WONT be DELETED "))
                        else:
                            print(('adding to del_batch of snapshot ' + snap.snapshot_id + ' where condition  ' + args[2] + " == " + args[3]))
                            #print " MATCH " + str(snap_dict)
                            del_batch.append(snap)
                else:
                    pass
        except Exception as err :
            print(("Deleting Adding int Batch Snapshot to be deleted  " + str(err)))
            raise

    if args[1] == 'BATCH_DELETE':
        print("The following is the Snapshot List to be DELETED in BATCH  : ")

        for snap in del_batch:
            for entry in array_all_list:
                if entry['SnapshotId'] == snap.snapshot_id:
                    desc= (entry['Description'][:70]) if len(entry['Description']) > 70 else entry['Description']
                    snap_tags= (entry['Tags'][:150]) if len(entry['Tags']) > 150 else entry['Tags']
                    vol_tags = (entry['volume_tags'][:150]) if len(entry['volume_tags']) > 150 else entry['volume_tags']
                    ami_tags = (entry['ami_tags'][:150]) if len(entry['ami_tags']) > 150 else entry['ami_tags']
                    ami_desc = (entry['ami_desc'][:70]) if len(entry['ami_desc']) > 70 else entry['ami_desc']

                    print(("{:24} {:14} {:25} {:8}  {:14} {:11} {:30} {:14} {:9} {:12} {:10}".format ('SnapshotId','StartTime','Sn_Vol_ID','S_V_Sz',
                                                                                                      'Vol_Cr_Time','Vol_Orphan','AMI_ID','Last_Used_AMI','AMI_Size',
                                                                                                      'Cur_EC2_AMI','V_State')))

                    ##print "================================================================================================================================================================================"
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print(("{:24} {:14} {:25} {:8}  {:14} {:11} {:30} {:14} {:9} {:12} {:10}".format (entry['SnapshotId'],entry['StartTime'],entry['VolumeID'],
                                                                                                      entry['Snap_VolumeSize'],entry['volume_ctime'],
                                                                                                      entry['volume_orphan'],entry['AMI'],entry['Last_AMI_Used'],
                                                                                                      entry['ami_size'],entry['current_ec2_ami'],
                                                                                                      entry['volume_state'])))
                    print(("Snap_Name: {:50} ::: Vol_Name: {:50}".format(entry['Snap_Name'],entry['volume_name'])))
                    print(("Snap_Desc: {:70}, AMI_Desc: {:70}".format(desc,ami_desc)))
                    print(("Snap_Tags: {:160}".format(snap_tags)))
                    print(("Vol_Tags : {:160}".format(vol_tags)))
                    print(("Ami_Tags : {:160} \n".format(ami_tags)))


        # print("del batch ",str(del_batch))
        inp=input("Deleting Snapshot older than  " + str(age)  + " where condition " + args[2] + " == " + args[3] + ", enter Y to proceed ... ")
        if inp == 'Y':
            for snap in del_batch:
                try:
                    print(("\nbatch deleting  snapshot " +  str(snap.snapshot_id)))
                    snap.delete()
                except botocore.exceptions.ClientError as e:
                        if e.response['Error']['Code'] == 'InvalidSnapshot.InUse':
                            # Handle the InvalidSnapshot.InUse exception
                            print('Skipping ..., Snapshot {} is currently in use may be by an AMI '.format(snap.id))
                        else:
                            # Handle other exceptions
                            print('An error occurred: {}'.format(e))


        else:
            print("batch delete canceled")





def get_aging_snapshot(ec2,ec2_sess,ct,resp,account,account_name,v_except,validt_ami=True):
    curr_usage_ami_list=[]
    array_all_list=[]

    datebef=datetime.datetime.now() - age
    fout=open(cost_dir+'aging_snapshot_list_'+date + '.txt','w')

    ami_list=get_ami_snap(ec2_sess)
    snap_del_list=[]
    vol_info_list=[]

    volumes = ec2.volumes.all()
    for vol in volumes:
        vol_info_dict={}
        tag_name_value = 'None'
        tag_lifecycle_value = 'None'

        if vol.tags:
            for tag in vol.tags:
                if tag['Key'].lower() == 'lifecycle':
                    tag_lifecycle_value = tag['Value']
                if tag['Key'].lower() == 'name':
                    tag_name_value = tag['Value']
        vol_info_dict.update({'vol_id':vol.volume_id,'vol_type':vol.volume_type,'vol_ctime':vol.create_time.strftime(fdate),'vol_state':vol.state,'vol_size':vol.size,'vol_lifecycle':tag_lifecycle_value,
                              'vol_name':tag_name_value,'vol_tags':convert_tag(vol.tags).strip()})
        vol_info_list.append(vol_info_dict)
        #print "vol info list " + str(vol_info_list)
### Finding AMI used by existing EC@
    curr_ec2_ami=ec2.instances.all()
    for curr_ami in curr_ec2_ami:
        curr_usage_ami_list.append(curr_ami.image_id)

    print(("finding snapshot created " + str(age) + " Ago "))
    for snapshot in resp:
        ami_usage={}
        svi={}
        ami_d={}
        array_dict={}

        if  snapshot.start_time < utc.localize(datebef):
            print(('\n\nfinding if snapshot ' + snapshot.id  + ' part of AMI'))
            if snapshot.id in v_except:
                print(("This snapshot " + snapshot.id + " IS in exception, so it is SKIPPED "))
                break

            ami_id='NA'
            snap_tag_lifecycle_value = 'None'
            snap_tag_name_value = 'None'

            if snapshot.tags:
                for sn_tag in snapshot.tags:
                    if sn_tag['Key'].lower() == 'lifecycle':
                        snap_tag_lifecycle_value = sn_tag['Value']
                    if sn_tag['Key'].lower() == 'name':
                        snap_tag_name_value = sn_tag['Value']



            for ami in ami_list:
                for  dev in ami['BlockDeviceMappings']:
                    #print 'ami ' + ami['ImageId'] + ' block dev is ' + str(dev)
                    if 'ephemeral'  not in dev.get('VirtualName','NA'):
                        #print(('EBS Snapshot to check belong to AMI  ' + str(dev['Ebs']) + 'with ami ' + ami['ImageId']))
                        try:
                            if snapshot.id == dev['Ebs']['SnapshotId']:
                                ami_id=ami['ImageId']
                                print('snapshot ',snapshot.id,' is a part of ami ', ami_id)
                                ###print 'snapshot ' + snapshot.id + ' is owned by ami ' + ami_id
                                break
                        except KeyError as ke:
                            print(("Key Error " + str(ke) + ' on ami ' + ami['ImageId']))
                            pass


            if ami_id == 'NA':
                # print("IN AMI ID NA")
                ami_usage['last_ami_used']='NA'
                ami_d.update({"ami_name":'NA'})
                ami_d.update({"ami_creation":'NA'})
                ami_d.update({"ami_size":'NA'})
                ami_d.update({"ami_state":'NA'})
                ami_d.update({"ami_description":'NA'})
                ami_d.update({"ami_tags":'NA'})
                ami_d.update({"ami_curr_ec2":'NA'})

                ####print 'snapshot ' + snapshot.id + ' is NOT OWNED by AMI'
                svi=get_snapshot_vol(ec2,snapshot,vol_info_list)
                #print "svi " + str(svi)
                snap_del_list.append(snapshot)
### If snapshot is a part of AMI, find the last time AMI has been used
            else:
                image_size=0
                ami_usage=lookup_trail_ami(ct,ami_id)
                image = ec2.Image(ami_id)
                for b_dev in image.block_device_mappings:
                    ###print 'BDEV ' + str(b_dev)
                    if 'ephemeral'  not in b_dev.get('VirtualName','NA'):
                        image_size = image_size + b_dev['Ebs']['VolumeSize']
                if ami_id in  curr_usage_ami_list:
                    curr_usage='Yes'
                else:
                    curr_usage='No'
                ami_d.update({"ami_name":image.name})
                ami_d.update({"ami_creation":image.creation_date})
                ami_d.update({"ami_size":image_size})
                ami_d.update({"ami_state":image.state})
                ami_d.update({"ami_description":safeStr(image.description)})
                ami_d.update({"ami_tags":convert_tag(image.tags).strip()})
                ami_d.update({"ami_curr_ec2":curr_usage})

                svi=get_snapshot_vol(ec2,snapshot,vol_info_list)
##set to AMI_Sn to indicate there is AMI associated with Snapshot
                svi.update({"orphan":"AMI_Sn"})


            array_dict.update({"Account": account,"Account Name":account_name,"SnapshotId":snapshot.id,"state":snapshot.state,
                               "StartTime":snapshot.start_time.strftime(fdate),"VolumeID": snapshot.volume_id,"Snap_VolumeSize":str(snapshot.volume_size),"Snap_Name":snap_tag_name_value,
                               "Description":snapshot.description.replace(',','.'),"Tags":convert_tag(snapshot.tags).strip(),
                               "volume_name":svi['v_name'],"volume_id":svi['v_id'],"volume_type":svi['v_type'],"volume_ctime":svi['v_ctime'],
                               "volume_state": svi['v_state'], "volume_size": str(svi['v_size']), "volume_lifecycle":svi['v_lifecycle'],
                               "volume_orphan":svi['orphan'],"volume_tags":svi['v_tags'],"AMI":ami_id,"Last_AMI_Used":ami_usage['last_ami_used'],
                               'ami_name':ami_d['ami_name'],'ami_creation':ami_d['ami_creation'], "ami_size": str(ami_d['ami_size']),
                               "ami_state":ami_d['ami_state'],"ami_desc": ami_d['ami_description'], "ami_tags":ami_d['ami_tags'],
                               "current_ec2_ami": ami_d['ami_curr_ec2'] } )

            array_all_list.append(array_dict)

            print(("Account," + account + ",Account Name," + account_name +",SnapshotId," + snapshot.id + ",state," + snapshot.state + ",StartTime," + str(snapshot.start_time) +
                  "VolumeID,"  + snapshot.volume_id +",Snap_VolumeSize," + str(snapshot.volume_size)+ ",Snap_Name," + snap_tag_name_value  + ", Description," +
                  snapshot.description.replace(',','.') + ",Tags," + convert_tag(snapshot.tags).strip()  + \
                  ",volume_name," + svi['v_name'] + ",volume_id,"+ svi['v_id'] + ",volume_type," + svi['v_type']+",volume_ctime,"+str(svi['v_ctime'])+",volume_state,"+
                  svi['v_state'] + ",volume_size," + str(svi['v_size']) + ",volume_lifecycle," + svi['v_lifecycle']  +
                  ",volume_orphan," + svi['orphan'] + ",volume_tags," + svi['v_tags']  + \
                  ",AMI," + ami_id + ",Last_AMI_Used,"+ ami_usage['last_ami_used'] + ',ami_name,' + ami_d['ami_name'] + ',ami_creation,' + ami_d['ami_creation'] + \
                  ",ami_size," + str(ami_d['ami_size']) + ",ami_state," + ami_d['ami_state'] + ",ami_desc," + ami_d['ami_description'] + ",ami_tags," + ami_d['ami_tags'] +
                  ",current_ec2_ami," + ami_d['ami_curr_ec2']  ))

            #
            # fout.write(("Account," + account + ",Account Name," + account_name +",SnapshotId," + snapshot.id + ",state," + snapshot.state + ",StartTime," + str(snapshot.start_time) +
            #             "VolumeID,"  + snapshot.volume_id +",Snap_VolumeSize," + str(snapshot.volume_size)+ ",Snap_Name," + snap_tag_name_value  + ", Description," +
            #             snapshot.description.replace(',','.') + ",Tags," + convert_tag(snapshot.tags).strip()  + \
            #             ",volume_name," + svi['v_name'] + ",volume_id,"+ svi['v_id'] + ",volume_type," + svi['v_type']+",volume_ctime,"+str(svi['v_ctime'])+",volume_state,"+
            #             svi['v_state'] + ",volume_size," + str(svi['v_size']) + ",volume_lifecycle," + svi['v_lifecycle']  +
            #             ",volume_orphan," + svi['orphan'] + ",volume_tags," + svi['v_tags']  + \
            #             ",AMI," + ami_id + ",Last_AMI_Used,"+ ami_usage['last_ami_used'] + ',ami_name,' + ami_d['ami_name'] + ',ami_creation,' + ami_d['ami_creation'] + \
            #             ",ami_size," + str(ami_d['ami_size']) + ",ami_state," + ami_d['ami_state'] + ",ami_desc," + ami_d['ami_description'] + ",ami_tags," + ami_d['ami_tags'] +
            #             ",current_ec2_ami," + safeStr(ami_d['ami_curr_ec2']) + '\n').encode('utf8'))
            #

            fout.write((
                                   "Account," + account + ",Account Name," + account_name + ",SnapshotId," + snapshot.id + ",state," + snapshot.state + ",StartTime," + str(
                               snapshot.start_time) +
                                   "VolumeID," + snapshot.volume_id + ",Snap_VolumeSize," + str(
                               snapshot.volume_size) + ",Snap_Name," + snap_tag_name_value + ", Description," +
                                   snapshot.description.replace(',', '.') + ",Tags," + convert_tag(
                               snapshot.tags).strip() +
                                   ",volume_name," + svi['v_name'] + ",volume_id," + svi['v_id'] + ",volume_type," +
                                   svi['v_type'] + ",volume_ctime," + str(svi['v_ctime']) + ",volume_state," +
                                   svi['v_state'] + ",volume_size," + str(svi['v_size']) + ",volume_lifecycle," + svi[
                                       'v_lifecycle'] +
                                   ",volume_orphan," + svi['orphan'] + ",volume_tags," + svi['v_tags'] +
                                   ",AMI," + ami_id + ",Last_AMI_Used," + ami_usage['last_ami_used'] + ',ami_name,' +
                                   ami_d['ami_name'] + ',ami_creation,' + ami_d['ami_creation'] +
                                   ",ami_size," + str(ami_d['ami_size']) + ",ami_state," + ami_d[
                                       'ami_state'] + ",ami_desc," + ami_d['ami_description'] + ",ami_tags," + ami_d[
                                       'ami_tags'] +
                                   ",current_ec2_ami," + (ami_d['ami_curr_ec2']) + '\n'))
            #

    #print 'snapshot list to delete ' + str(snap_del_list)
    if validt_ami:
        val_ami=validate_ami(ec2_sess,array_all_list,datebef,v_except)
        if val_ami:
            print("AMI has been validated")
        else:
            print("AMI Validation  Error")
            exit(1)
    return array_all_list

### function to find if snapshot associated volume still exists
def get_snapshot_vol(ec2,snapshot,vol_info_list):
    snapshot_vol_info={}
##if vol-ffffffff , it means the volume was gone
    if snapshot.volume_id == 'vol-ffffffff':
        snapshot_vol_info.update({"orphan":"Yes"})
        snapshot_vol_info.update({"v_id":'NA'})
        snapshot_vol_info.update({"v_type":'NA'})
        snapshot_vol_info.update({"v_ctime":'NA'})
        snapshot_vol_info.update({"v_state":'NA'})
        snapshot_vol_info.update({"v_size":'NA'})
        snapshot_vol_info.update({"v_lifecycle":'NA'})
        snapshot_vol_info.update({"v_name":'NA'})
        snapshot_vol_info.update({"v_tags":'NA'})
    else:
        vol_exist=False
        for vol in vol_info_list:
            #print 'in checking vol_d ' + vol['vol_id'] + ' and snap volume_id ' + snapshot.volume_id
            if vol['vol_id'] == snapshot.volume_id:
                snapshot_vol_info.update({"orphan":"No"})
                snapshot_vol_info.update({"v_id":snapshot.volume_id})
                snapshot_vol_info.update({"v_type":vol['vol_type']})
                snapshot_vol_info.update({"v_ctime":vol['vol_ctime']})
                snapshot_vol_info.update({"v_state":vol['vol_state']})
                snapshot_vol_info.update({"v_size":vol['vol_size']})
                snapshot_vol_info.update({"v_lifecycle":vol['vol_lifecycle']})
                snapshot_vol_info.update({"v_name":vol['vol_name']})
                snapshot_vol_info.update({"v_tags":vol['vol_tags']})
                vol_exist=True
        if not vol_exist:
            snapshot_vol_info.update({"orphan":"InBetween"})
            snapshot_vol_info.update({"v_id":'NA'})
            snapshot_vol_info.update({"v_type":'NA'})
            snapshot_vol_info.update({"v_ctime":'NA'})
            snapshot_vol_info.update({"v_state":'NA'})
            snapshot_vol_info.update({"v_size":'NA'})
            snapshot_vol_info.update({"v_lifecycle":'NA'})
            snapshot_vol_info.update({"v_name":'NA'})
            snapshot_vol_info.update({"v_tags":'NA'})

    return snapshot_vol_info





def list_snapshot(account='All',ami_snap=False,unencrypted=False,age=0):
    print("################Listing Snapshot ################")


    total_account_sub_dict={}
    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
        fout=open(cost_dir+'snapshot_list_' + account + '_' +  date+'.txt','w')
    else:
        Account_Session.initialize_all()
        fout=open(cost_dir+'snapshot_list_' + date+'.txt','w')

    fout.write("account,account_name,snapshotid,start_time,state,volume_id,owner_id,encrypted,volumesize,description\n")

    ami_snap_list=[]

    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Finding Snapshoton account : ' + account + ' ' + sessinfo['name'] + ' ============================\n\n\n'))
            # Define the connection
            snap_to_delete_list=[]

            ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
            ec2_sess = sessinfo['session'].client('ec2', region_name="us-east-1")
            ec2_sess = sessinfo['session'].client('cloudtrail', region_name="us-east-1")

            # Find all volumes
            # if account == 'All':
            resp=ec2.snapshots.filter(OwnerIds=['self'])
            for snapshot in resp:
                start_time=snapshot.start_time
                delete_time=datetime.datetime.now(utc) - datetime.timedelta(days=age)
                snapshot_desc='NA'
                if 'Task created' in snapshot.description:
                    print ("issue     XXXXXXXX",snapshot.description[:-22])
                    snapshot_desc=snapshot.description[:-22]
                else:
                    snapshot_desc=snapshot.description.replace(',',':')

                to_print=("{},{},{},{},{},{},{},{},{},{}".
                          format(account,sessinfo['name'],snapshot.id,str(snapshot.start_time),snapshot.state,snapshot.volume_id,snapshot.owner_id,str(snapshot.encrypted),
                                 str(snapshot.volume_size),snapshot_desc))
                if delete_time > start_time:


                    #print(("{},{},{},{},{},{},{},{} ".
                    #       format(snapshot.id,str(snapshot.start_time),snapshot.state,snapshot.volume_id,snapshot.owner_id,str(snapshot.encrypted),
                    #           str(snapshot.volume_size),snapshot.description)))
                    print(to_print)
                    fout.write(to_print + '\n')








    except Exception as err :
        print(("List Snapshot  " + str(err)))
        raise


def delete_snapshot(subaccount,description,day='14'):
    print(("################Deleting Snapshot older than {}################".format(days)))
    Account_Session.initialize()
    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Finding Snapshoton account : ' + account + ' ============================\n\n\n'))
            # Define the connection
            ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")

            # Find all volumes
            if  account==subaccount:
                resp=ec2.snapshots.filter(OwnerIds=['self'])
                for snapshot in resp:
                    start_time=snapshot.start_time
                    delete_time=datetime.now - datetime.timedelta(days=day)
                    if delete_time > start_time:
                        print(("snapshotid,{},start_time,{},state,{},volume_id,{},owner_id,{},encrypted,{},volumesize,{},description,{} ".
                               format(snapshot.id,str(snapshot.start_time),snapshot.state,snapshot.volume_id,snapshot.owner_id,str(snapshot.encrypted),
                                      str(snapshot.volume_size),snapshot.description)))



    except Exception as err :
        print(("List Snapshot  " + str(err)))
        raise





