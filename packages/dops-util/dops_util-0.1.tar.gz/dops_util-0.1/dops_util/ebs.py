#from .global_var import *
from dops_util import *
from dops_util.dynamo import *

#from costing.costing_src.dops_util.connect import Account_Session


def lookup_trail_ebs(ct_sess,volume):
    print(("Looking up last detached and last attached for volume :" + volume))
    resp=ct_sess.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'ResourceName',
                'AttributeValue':  volume
            },
        ]
    )
    ####print "resp ct " + str(resp['Events'])
    detach=[]
    attach=[]
    for event in resp['Events']:
        ##print "event name " + event['EventName']
        ##print "event time " + event['EventTime'].strftime("%Y-%m-%d %H:%M")

        if event['EventName'] == 'AttachVolume':
            attach.append(event['EventTime'])

        if event['EventName'] == 'DetachVolume':
            detach.append(event['EventTime'])

        ####if event['EventName'] == 'AttachVolume' or  event['EventName'] == 'DetachVolume':
        ####     print "event name " + event['EventName']
        #### print "event time " + event['EventTime'].strftime("%Y-%m-%d %H:%M")
    sorted_attach=sorted(attach)
    sorted_detach=sorted(detach)
    res={}
    if sorted_attach:
        print(("the last attach  " + sorted_attach[-1].strftime("%Y-%m-%d %H:%M")))
        res={"last_attached":sorted_attach[-1].strftime("%Y-%m-%d %H:%M")}
    else:
        res={"last_attached":"No Info"}

    if sorted_detach:
        print(("the last detach  " + sorted_detach[-1].strftime("%Y-%m-%d %H:%M")))
        res.update({"last_detached":sorted_detach[-1].strftime("%Y-%m-%d %H:%M")})
    else:
        res.update({"last_detached":"No Info"})

    return res

def checking_provision_disk(iotype, available=False,delete=False,sf_id='NA'):
    print("################Checking EBS Provision IO allocation ################")
    Account_Session.get_account_list()
    lng=len(Account_Session.ACCLIST)
    recon=0
    inst_dict={}
    fout=open(cost_dir+'ebs_list_'+iotype + '_' + date+'.txt','w')
    fout.write("Account,Created,AZ,VolumeID, VolumeType ,State ,Size,IOPS , IsEncrypted,SnapshotID , kms_key_id,"
               "last_attached,last_detached,Lifecycle,Name, \n")



###print 'lng' + str(lng) + 'and int' + str(int(lng/acc_step)+1) + ' and int lng per acc_step ' + str(int(lng/acc_step))
    for cnt in range(1,int(lng/acc_step)+2):
        Account_Session.SESS_DICT={}
        Account_Session.initialize(cnt)


        try:
            for account,sessinfo in list(Account_Session.SESS_DICT.items()):
                vol_list_to_dynamo=[]

                print(('\n\n\n====================Finding EBS provision Volume on account : ' + account + ' ============================\n\n\n'))

                try:
                    # Define the connection
                    ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
                    ct =  sessinfo['session'].client('cloudtrail', region_name="us-east-1")

                    # Find all volumes
                    resp = ec2.instances.all()
                    for inst in  resp:
                        if inst.tags:
                            tag_name_value='None'
                            for tag in inst.tags:
                                if tag['Key'].lower() == 'name':
                                    #tag_lifecycle = 'lifecycle'
                                    tag_name_value = tag['Value']
                        inst_dict.update({inst.instance_id:tag_name_value})

                    volumes = ec2.volumes.all()

                    # Loop through all volumes and pass it to ec2.Volume('xxx')
                    for vol in volumes:
                        try:
                            recon=recon + 1
                            if account in spec_session and recon % spec_session_reconnect == 0:
                                print("in spec session ")
                                ec2 = sessinfo['session'].resource('ec2', region_name="us-east-1")
                                ct =  sessinfo['session'].client('cloudtrail', region_name="us-east-1")

                            iv = ec2.Volume(str(vol.id))

                            if iv.volume_type==iotype:
                                tag_lifecycle_value = 'None'
                                tag_name_value='None'
                                if iv.tags:
                                    for tag in iv.tags:
                                        if tag['Key'].lower() == 'lifecycle':
                                            #tag_lifecycle = 'lifecycle'
                                            tag_lifecycle_value = tag['Value']
                                        if tag['Key'].lower() == 'name':
                                            #tag_lifecycle = 'lifecycle'
                                            tag_name_value = tag['Value']

                                if available:

                                    if iv.state=='available':
                                        trail=lookup_trail_ebs(ct,iv.volume_id)

                                        #print "Getting Disk Type : " + iotype + " With 'available' State"
                                        print(("trail " + str(trail)))
                                        print(("Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + str(iv.snapshot_id)  + \
                                              ",last_attached," + trail['last_attached'] + ",last_detached," + trail['last_detached'] + ",Lifecycle," + tag_lifecycle_value + ",Name," + tag_name_value + "\n"))

                                        fout.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},\n".format( sessinfo['name'],str(iv.create_time), str(iv.availability_zone), str(iv.volume_id) ,
                                                                                                             str(iv.volume_type) , str(iv.state), str(iv.size) , str(iv.iops) , str(iv.encrypted),
                                                                                                             str(iv.snapshot_id), str(iv.kms_key_id), trail['last_attached'],trail['last_detached'], tag_lifecycle_value,tag_name_value))

                                        vol_list_to_dynamo.append(iv.volume_id)
                                        # The following next 2 print statements variables apply only in my case.
                                        #print ",InstanceID(" + str(iv.attachments[0]['InstanceId']) + "),InstanceVolumeState(" + str(iv.attachments[0]['State']) + "),DeleteOnTerminationProtection(" + str(iv.attachments[0]['DeleteOnTermination']) + "),Device(" + str(iv.attachments[0]['Device']) + ")",
                                        if iv.attachments:
                                            #print "iv attaccments " + str(iv.attachments[0])
                                            print((",InstanceID : " + str(iv.attachments[0].get('InstanceId','NA'))))
                                            #_list_product_local_or_imported(sessinfo['session'])
                                elif iv.state == 'in-use':
                                    #tag_lifecycle_value = 'None'
                                    #tag_name_value='None'
                                    if iv.tags:
                                        for tag in iv.tags:
                                            if tag['Key'].lower() == 'lifecycle':
                                                #tag_lifecycle = 'lifecycle'
                                                tag_lifecycle_value = tag['Value']
                                            if tag['Key'].lower() == 'name':
                                                #tag_lifecycle = 'lifecycle'
                                                tag_name_value = tag['Value']
                                    #print "Getting Disk Type : " + iotype + " With Any State"
                                    #print "Created(" + str(iv.create_time) + "),AZ(" + str(iv.availability_zone) + "),VolumeID(" + str(iv.volume_id) + "),VolumeType(" + str(iv.volume_type) + "),State(" + str(iv.state) + "),Size(" + str(iv.size) + "),IOPS(" + str(iv.iops) + "),IsEncrypted(" + str(iv.encrypted) + "),SnapshotID(" + str(iv.snapshot_id) + "),KMS_KEYID(" + str(iv.kms_key_id) + ")\n",
                                    instanceid='NA'
                                    if iv.attachments:
                                        #print "iv attaccments " + str(iv.attachments[0])
                                        instanceid= str(iv.attachments[0].get('InstanceId','NA'))
                                        ##print(",InstanceID , " + str(iv.attachments[0].get('InstanceId','NA')))
                                        #_list_product_local_or_imported(sessinfo['session'])

                                    print(("Account," + account + ",Account Name," + sessinfo['name'] +",InstanceId," + instanceid + ",InstanceName," + inst_dict[instanceid] + ",Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + str(iv.snapshot_id) + ",kms_key_id," +  str(iv.kms_key_id)))
                                    #fout.write("Account," +  sessinfo['name'] + ",InstanceId," + instanceid + ",InstanceName," + inst_dict[instanceid] +",Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + str(iv.snapshot_id) + ",kms_key_id," +  str(iv.kms_key_id) + '\n')
                                    #fout.write("Account," +  sessinfo['name'] +",Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + str(iv.snapshot_id) + ",kms_key_id," +  str(iv.kms_key_id) + \
                                    #         ",last_attached," + trail['last_attached']+ ",last_detached," + trail['last_detached']+ ",Lifecycle," + tag_lifecycle_value+ ",Name," + tag_name_value + "\n")
                                    fout.write("Account," + account + ",Account Name," + sessinfo['name'] +",InstanceId," + instanceid + ",InstanceName," + inst_dict[instanceid] +",Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + \
                                               str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + \
                                               str(iv.snapshot_id) + ",kms_key_id," +  str(iv.kms_key_id) + ",Lifecycle," + \
                                               tag_lifecycle_value+ ",Name," + tag_name_value + "\n")
                                    ##put_data(exec_id, vol_list,table_name='batch_output',dynamodb=None):



                        except Exception as err:
                            print((traceback.format_exc()))
                            print(("Finding EBS  " + str(err)))
                            pass
                    if vol_list_to_dynamo and sf_id:
                        print ('inserting dynamo ',sf_id,account,vol_list_to_dynamo)
                        resp_dynamo=put_data(sf_id,account,vol_list_to_dynamo)
                        print('dynamore ret',str(resp_dynamo))

                except Exception as err :
                    print((traceback.format_exc()))
                    print(("Finding EBS Provision Volume  " + str(err)))
                    pass
        ##except InvalidVolume.NotFound:
        ##    print (("Volume is not found ",str(iv.volume_id)))
        ##    pass
        except Exception as err :
            print((traceback.format_exc()))
            print(("Finding EBS Provision  " + str(err)))
            pass


def delete_all_unattached_ebs_from_dynamo(sf_id='NA'):
    account_list=Account_Session.get_account_list()
    for account in account_list:
        print ('retrieving ebs info from  dynamo of account ', account,'with exec_id ',sf_id)

        resp=get_data(sf_id, account)
        print('dynamore ret',str(resp))
        if resp:
            delete_unattached_ebs_subaccount_from_dynamo_db(resp['vol_id'],account)

def delete_unattached_ebs_subaccount_from_dynamo_db(vol_list,subaccount):
    sess=Account_Session.build_sess_subaccount(subaccount)
    ec2 = sess.resource('ec2', region_name="us-east-1")
    ct =  sess.client('cloudtrail', region_name="us-east-1")
    for vol in vol_list:
        #vol_to_del=ec2.volumes(vol)
        print ('deleting in account', subaccount, 'volume ', vol)
        iv = ec2.Volume(vol)
        tag_lifecycle_value = 'None'
        tag_name_value = 'None'
        try:
            if iv.tags:
                for tag in iv.tags:
                    if tag['Key'].lower() == 'lifecycle':
                        #tag_lifecycle = 'lifecycle'
                        tag_lifecycle_value = tag['Value']
                    if tag['Key'].lower() == 'name':
                        #tag_lifecycle = 'lifecycle'
                        tag_name_value = tag['Value']

            if iv.state=='available' and  tag_lifecycle_value.lower() != 'forever':
                print("\n\n--------------------------------------------------------------------------------------------")
                trail=lookup_trail_ebs(ct,iv.volume_id)
                print(("Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + str(iv.snapshot_id) + ",kms_key_id," +  str(iv.kms_key_id) + \
                       ",last_attached," + trail['last_attached'] + ",last_detached," + trail['last_detached'] + ",Lifecycle," + tag_lifecycle_value + ",Name," + tag_name_value ))
                if trail['last_detached'] == 'No Info':
                    trail['last_detached'] = (datenow - datetime.timedelta(days=100)).strftime("%Y-%m-%d %H:%M")

                now = datenow.replace(tzinfo=None) ##offset aware to naive aware time
                if (datenow - iv.create_time >= hour_passed) and (( now - datetime.datetime.strptime(trail['last_detached'], '%Y-%m-%d %H:%M') >= hour_passed)):
                    print(('volume  ' + str(iv.volume_id) + ' Age is  ' + str(datenow - iv.create_time)))
                    print("Deleting this unattached ebs ... ",iv.volume_id)
                    #####iv.delete()
                    print(("Volume: " + str(iv.volume_id)  + " has been DELETED\n"))
                else:
                    print((iv.volume_id,"Created in last  " + str( datenow - iv.create_time)))
                #print "It has never been attach or has not  been unattached or attached for > 90 days, " + "Deleting this unattached ebs ... "

        except botocore.exceptions.ClientError as e:
            if 'InvalidVolume.NotFound' in str(e):
                print(e.__class__,e)
                print ('Volume of ',iv.volume_id,'can not be found')
                pass

            else:
                raise(e)




def delete_all_unattached_ebs_in_a_subaccount(args):
    #print (str(args))
    v_except=[]
    print(("Checking EBS Exception Not To Be Deleted in file " + ebs_except))
    if os.path.isfile(ebs_except) and os.stat(ebs_except).st_size != 0:
        f_except=open(ebs_except,'r')
        for v in f_except:
            v_except.append(v.strip())
    else:
        print(('File EBS Exception ' + ebs_except + ' Does Not Exist or It is empty'))
    print(('EBS in Exception List  ' + str(v_except)))

    del_batch=[]
    datenow=datetime.datetime.now(utc)

    Account_Session.build_sess_subaccount(args[0])
    sess=Account_Session.SESS_DICT[args[0]]
    ec2 = sess['session'].resource('ec2', region_name="us-east-1")
    ct =  sess['session'].client('cloudtrail', region_name="us-east-1")


    # Find all volumes
    volumes = ec2.volumes.all()

    # Loop through all volumes and pass it to ec2.Volume('xxx')
    try:
        for vol in volumes:
            try:
                iv = ec2.Volume(str(vol.id))

                if iv.volume_type==args[1]:
                    tag_lifecycle_value = 'None'
                    tag_name_value = 'None'
                    if iv.tags:
                        for tag in iv.tags:
                            if tag['Key'].lower() == 'lifecycle':
                                #tag_lifecycle = 'lifecycle'
                                tag_lifecycle_value = tag['Value']
                            if tag['Key'].lower() == 'name':
                                #tag_lifecycle = 'lifecycle'
                                tag_name_value = tag['Value']



                    if iv.state=='available' and  tag_lifecycle_value.lower() != 'forever':
                        #print "Getting Disk Type : " + iotype + " With 'available' State"
                        print("\n\n--------------------------------------------------------------------------------------------")
                        trail=lookup_trail_ebs(ct,iv.volume_id)
                        print(("Created," + str(iv.create_time) + " , AZ,"  + str(iv.availability_zone) +",VolumeID," + str(iv.volume_id) + ", VolumeType," + str(iv.volume_type) + ",State," + str(iv.state)  + ",Size," +  str(iv.size) + ",IOPS," + str(iv.iops) + " , IsEncrypted," + str(iv.encrypted)  + ",SnapshotID," + str(iv.snapshot_id) + ",kms_key_id," +  str(iv.kms_key_id) + \
                              ",last_attached," + trail['last_attached'] + ",last_detached," + trail['last_detached'] + ",Lifecycle," + tag_lifecycle_value + ",Name," + tag_name_value ))

                        if args[2] == 'BATCH_DELETE':
                            if datenow - iv.create_time >= hour_passed:
                                print(('adding ' + str(iv.volume_id) + ' into batch to be deleted of volume older than ' + str(hour_passed)))
                                del_batch.append(iv)
                            else:
                                print(("Created in last  " + str( datenow - iv.create_time)))
                                print(('NOT adding ' + str(iv.volume_id) + ' into batch to be deleted'))
                        else:

                            #print "It has never been attach or has not  been unattached or attached for > 90 days, " + "Deleting this unattached ebs ... "
                            print("Deleting this unattached ebs ... ")
                            if args[2] !=  "YES_ALL":
                                inp=eval(input("enter Y to proceed ... "))
                                if inp == 'Y':
                                    if iv.volume_id not in v_except:
                                        iv.delete()
                                        print(("Volume: " + str(iv.volume_id)  + " has been DELETED\n"))
                                    else:
                                        print(('Volume ' + str(iv.volume_id) + ' is NOT Deleted, it is  in EXCEPTION LIST '))
                                else:
                                    print(("Volume: " + str(iv.volume_id)  + " has NOT been deleted\n"))
                            else:
                                ##if trail['last_detached'] == 'No Info' and  trail['last_attached'] == 'No Info':
                                if True:
                                    print(("****** NON INTERACTIVE DELETION  for volume create more than " + str(delta) + " days ago and it has not been attached to EC2 for 90 days *******"))
                                    if datenow - iv.create_time >= delta:
                                        print("It has never been attach or has not  been unattached or attached for > 90 days and create 90 days ago ")
                                        #inp=raw_input("enter Y to proceed ... ")


                                        if iv.volume_id not in v_except:
                                            iv.delete()
                                            print(("Volume: " + str(iv.volume_id)  + " has been DELETED\n"))
                                        else:
                                            print(('Volume ' + str(iv.volume_id) + ' is NOT Deleted, it is  in EXCEPTION LIST'))
                                    else:
                                        print(("volume " + str(iv.volume_id) + " has been created NOT more than " + str(delta) + " days ago"))
                                else:
                                    print("It has NOT been deleted as volume was attached/detached last 90 days")


            except Exception as err:
                print((traceback.format_exc()))
                print(("Finding EBS  " + str(err)))
                print(("error id deleting unattached ebs ", str(err)))

        if args[2] == 'BATCH_DELETE':
            print("\n\n====================================================")
            print('to be deleted ',str(del_batch))
            answer=input("Deleting Volume More Than " + str(hour_passed)  + " Old Volume in batch, enter Y to proceed ... ")
            #answer=input()
            print (answer)
            if answer == 'Y':
                for v in del_batch:
                    print(("\nbatch deleting  volume " +  str(v.volume_id)))
                    if v.volume_id not in v_except:
                        v.delete()
                    else:
                        print(('Volume ' + str(v.volume_id) + ' is NOT Deleted, it is  in EXCEPTION list '))
            else:
                print("batch delete canceled")

    except Exception as err:
        print((traceback.format_exc()))
        print(("Finding EBS have an issue  " + str(err)))
        print(("error batch deleting ebs ", str(err)))


if __name__ == '__main__':
    print("In Main.")
    vol_list=['vol-0ac5a4bfaf6efe9e6','vol-063442a40234cf2a5','vol-0e005ab3a6f36bd9d']
    exec_id='76767676'
    account='680255642622'
    delete_unattached_ebs_subaccount_from_dynamo_db(vol_list,account)




