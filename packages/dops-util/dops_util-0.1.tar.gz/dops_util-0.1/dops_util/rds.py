#!/usr/bin/env python2
#from dops_util.connect import get_aws_account_id,getsessionv2,Account_Session,role_to_session,getsession,paginate
#from .global_var import *
#from dops_util.rds import *
#from dops_util.connect import *
from dops_util import *
from dops_util.cw import *

def list_rds_snapshot(account='All'):

    print("################Listing RDS ################")
    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
    else:
        Account_Session.initialize_all()
    fout=open(cost_dir+'list_rds_snapshot' + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:15},{:15},{:10},{:10},{:10},{:6},{:12},{:10}\n".format('Account','AccountName','DBSnapshotId','DBInstanceOrClusterId','SnapshotCreateTime',''
                                                            'Engine','Allocated(GB)','Status','SnapshotType','RDS_Type'))


    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding RDS Snapshot on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        rdsc = sessinfo['session'].client('rds', region_name="us-east-1")

        snapshots = rdsc.describe_db_snapshots()

        for snap in snapshots['DBSnapshots']:
            # print('SN',snap['DBSnapshotIdentifier'],
            #
            # snap['DBInstanceIdentifier'],
            # snap.get('SnapshotCreateTime','NA'),
            # snap['Engine'],
            # snap['AllocatedStorage'],
            # snap['Status'],
            # snap['SnapshotType']
            rds_type='non-aurora'
            snap_create_tmp=snap.get('SnapshotCreateTime','NA')
            if str(snap_create_tmp) != 'NA':
                snap_create = snap_create_tmp.strftime('%m-%d-%Y')
            else:
                snap_create = 'NA'
            out_format="{:15},{:20},{:15},{:15},{:10},{:10},{:10},{:6},{:12},{:10}" \
                .format(account,sessinfo['name'],snap['DBSnapshotIdentifier'], snap['DBInstanceIdentifier'],
                        snap_create, snap['Engine'],snap['AllocatedStorage'],snap['Status'],snap['SnapshotType'],rds_type)
            print(out_format)
            fout.write(out_format + '\n')


        snapshot_cl = rdsc.describe_db_cluster_snapshots()
        for snap_cl in snapshot_cl['DBClusterSnapshots']:
            rds_type='aurora'
            # print(snap_cl['DBClusterSnapshotIdentifier'],
            # snap_cl['DBClusterIdentifier'],q
            # snap_cl['SnapshotCreateTime'],
            # snap_cl['Engine'],
            # # snap['EngineMode'],
            # snap_cl['AllocatedStorage'],
            # snap_cl['Status'],
            # snap_cl['SnapshotType']
            cl_create_tmp=snap.get('SnapshotCreateTime','NA')
            if str(cl_create_tmp) != 'NA':
                cl_create = snap_create_tmp.strftime('%m-%d-%Y')
            else:
                cl_create = 'NA'
            out_format="{:15},{:20},{:15},{:15},{:10},{:10},{:10},{:6},{:12},{:10}" \
                .format(account,sessinfo['name'],snap_cl['DBClusterSnapshotIdentifier'], snap_cl['DBClusterIdentifier'],
                      cl_create, snap_cl['Engine'],snap_cl['AllocatedStorage'],snap_cl['Status'],snap_cl['SnapshotType'],rds_type)


            print(out_format)
            fout.write(out_format + '\n')




def list_rds_read_replica(account='All'):
    print("################Listing RDS ################")
    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
    else:
        Account_Session.initialize_all()
    fout=open(cost_dir+'rds_list_read_only_replica' + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    fout.write("{:15},{:20},{:15},{:15},{:10},{:20},{:20},{:6},{:12},"
               "{:20},{:6},{:15},{:15},{:6},{:6} \n".format('Account','AccountName','DBClusterIdentifier','DatabaseName','Status','EndPoint',
                                                          'ReaderEndpoint','MultiAZ','EngineVersion','DB_Identifier','Writer','Last_3M_Max_CPU','Last_3M_DB_Max_Conn', 'DBClusterInstanceClass',
                                                          'ReadReplicaIdentifiers'))


    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding RDS Read Only on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        rdsc = sessinfo['session'].client('rds', region_name="us-east-1")
        ec2_resource = sessinfo['session'].resource('cloudwatch', region_name="us-east-1")

        cw=CloudWatchWrapper(ec2_resource)

        response = rdsc.describe_db_clusters()
        rdslist=response['DBClusters']
        rds_to_return=[]

        for rds in rdslist:
            list_inst_member=rds['DBClusterMembers']
            rds_instance_id=[]

            for member in list_inst_member:
               rds_member={}
               if not (member['IsClusterWriter']):
                   dimension=[
                       {'Name':'DBInstanceIdentifier','Value':member['DBInstanceIdentifier']}
                   ]

                   cpu_max_util=cw.get_metric_statistics('AWS/RDS','CPUUtilization', starttime, endtime, 7200, 'Maximum',dimension)
                   db_connection_max=cw.get_metric_statistics('AWS/RDS','DatabaseConnections', starttime, endtime, 7200, 'Maximum',dimension)
                   rds_member.update({'DBInstanceId':member['DBInstanceIdentifier']})
                   rds_member.update({'Writer':str(member['IsClusterWriter'])})
                   rds_member.update({'cpu_3_month':cpu_max_util})
                   rds_member.update({'connection_3_month':db_connection_max})
                   print('rds member ',str(rds_member))
                   rds_instance_id.append(rds_member)
                   rds_to_return.append(rds_member)
                   #print (str(member['IsClusterWriter']))

            for rds_inst in rds_instance_id:
                print ('rdsinsta ',str(rds_inst))
                out_format="{:15},{:20},{:15},{:15},{:10},{:20},{:20},{:6},{:12}," \
                           "{:20},{:6},{:15},{:15},{:6},{:6}".format(account,sessinfo['name'],rds['DBClusterIdentifier'],rds.get('DatabaseName','NA'),
                                                                        rds['Status'],rds['Endpoint'],rds.get('ReaderEndpoint','NA'),str(rds['MultiAZ']),
                                                                        rds['EngineVersion'],rds_inst['DBInstanceId'],rds_inst['Writer'],rds_inst['cpu_3_month'],
                                                                        rds_inst['connection_3_month'],rds.get('DBClusterInstanceClass','NA'),
                                                                        str(rds['ReadReplicaIdentifiers']))

                print(out_format)
                fout.write(out_format + '\n')

    return rds_to_return




def list_rds(type='provisioned',unencrypted=None,subaccount=None):
    print("################Listing RDS ################")
    # Account_Session.initialize_all()
    fout=open(cost_dir+'rds_list_'+ type + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(2160))
    if type=='provisioned':
        fout.write(("Account,Account_Name,DBClusterIdentifier,DBInstanceId, DBInstanceClass, Engine, DBName,Endpoint,DBInstanceStatus,AllocatedStorage,InstanceCreateTime,MultiAZ,LicenseMode,Iops,"
                    "PubliclyAccessible,StorageType,Encrypted,DeletionProtection,CPU_Max_Util_Last_3_Month,DB_Max_Connection_Last_3_Month\n"))
    elif type=='serverless':
        fout.write("Account,Account_Name,DatabaseName,DBClusterIdentifier,Status,Capacity, MinCapacity, MaxCapacity, AutoPause \n")
    elif type=='all':
        if subaccount:
            fout=open(cost_dir+'rds_list_'+ type + '_'+ subaccount + '_' + date+'.txt','w')
        else:
            fout=open(cost_dir+'rds_list_'+ type + '_'+date+'.txt','w')
        fout.write("Account,Account_Name,DatabaseName,DBClusterIdentifier,Status,Capacity, MinCapacity, MaxCapacity, AutoPause \n")





    if subaccount:
        Account_Session.build_sess_subaccount(subaccount)
        # fout = open(cost_dir + "list_all_ip_info_" + type + '_' +  date + ".txt", "w")

    else:
        # fout = open(cost_dir + "list_all_ip_info_" + date + ".txt", "w")
        Account_Session.initialize_all()

    try:
        for account,sessinfo in list(Account_Session.SESS_DICT.items()):
            print(('\n\n\n====================Finding RDS on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n'))

            # Define the connection
            rdsc = sessinfo['session'].client('rds', region_name="us-east-1")
            ec2_client = sessinfo['session'].client('cloudwatch', region_name="us-east-1")


            if type == 'provisioned':
                resp=rdsc.describe_db_instances()
                dbiter=resp['DBInstances']
                #print ("in here {:}".format(str(dbiter)))

                #print str(dbiter)
                if dbiter:
                    #fout.write("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name']))
                    print(("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name'])))

                for db in dbiter:
                    print(db)


                    #if not unencrypted:
                    #if not db['StorageEncrypted']:
                    cpu_max_util=get_cw_metric(ec2_client,db['DBInstanceIdentifier'],starttime,endtime,name_space='AWS/RDS',type='DBInstanceIdentifier')
                    db_max_connection=get_cw_metric(ec2_client,db['DBInstanceIdentifier'],starttime,endtime,name_space='AWS/RDS',type='DBInstanceIdentifier',metric_name='DatabaseConnections',stats='Maximum')


                    print(("Account,{},Account_Name,{},DBClusterIdentifier,{},DBInstanceId,{}, DBInstanceClass,{}, Engine,{}, DBName,{},Endpoint,{},DBInstanceStatus,{},AllocatedStorage,{},InstanceCreateTime,{},MultiAZ,{},LicenseMode,{},Iops,"
                           "{},PubliclyAccessible,{},StorageType,{},Encrypted,{},DeletionProtection,{},CPU_Max_Util_Last_3_Month,{},DB_Max_Connection_Last_3_Month,{}".format(account, sessinfo['name'],db.get('DBClusterIdentifier','NA'),
                                                                                                                                                                              db['DBInstanceIdentifier'],db['DBInstanceClass'],db['Engine'],db.get('DBName','NA'),
                                                                                                                                                                              db['Endpoint']['Address'],db['DBInstanceStatus'],str(db['AllocatedStorage']),
                                                                                                                                                                              str(db['InstanceCreateTime']),db['MultiAZ'],db['LicenseModel'],str(db.get('Iops','NA')),
                                                                                                                                                                      str(db['PubliclyAccessible']),db['StorageType'],str(db['StorageEncrypted']),
                                                                                                                                                                              str(db.get('DeletionProtection','NA')),cpu_max_util,db_max_connection)))
                    fout.write(("{},{},{},{},{},{},{},{},{},{},{},{},{},"  
                                "{},{},{},{},{},{},{}\n".format(account, sessinfo['name'],db.get('DBClusterIdentifier','NA'),db['DBInstanceIdentifier'],db['DBInstanceClass'],db['Engine'],db.get('DBName','NA'),
                                                                db['Endpoint']['Address'],db['DBInstanceStatus'],str(db['AllocatedStorage']),str(db['InstanceCreateTime']),db['MultiAZ'],db['LicenseModel'],str(db.get('Iops','NA')),
                                                                str(db['PubliclyAccessible']),db['StorageType'],str(db['StorageEncrypted']),str(db.get('DeletionProtection','NA')),cpu_max_util,db_max_connection)))


            elif type == 'all':
                resp=rdsc.describe_db_instances()
                dbiter=resp['DBInstances']
                #print ("in here {:}".format(str(dbiter)))

                #print str(dbiter)
                if dbiter:
                    #fout.write("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name']))
                    print(("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name'])))

                for db in dbiter:

                    #if not unencrypted:
                    #if not db['StorageEncrypted']:
                    cpu_max_util=get_cw_metric(ec2_client,db['DBInstanceIdentifier'],starttime,endtime,name_space='AWS/RDS',type='DBInstanceIdentifier')
                    db_max_connection=get_cw_metric(ec2_client,db['DBInstanceIdentifier'],starttime,endtime,name_space='AWS/RDS',type='DBInstanceIdentifier',metric_name='DatabaseConnections',stats='Maximum')


                    print(("Account,{},Account_Name,{},DBInstanceId,{}, DBInstanceClass,{}, Engine,{}, DBName,{},Endpoint,{},DBInstanceStatus,{},AllocatedStorage,{},InstanceCreateTime,{},MultiAZ,{},LicenseMode,{},Iops,"
                           "{},PubliclyAccessible,{},StorageType,{},Encrypted,{},DeletionProtection,{},CPU_Max_Util_Last_3_Month,{},DB_Max_Connection_Last_3_Month,{}".format(account, sessinfo['name'],db['DBInstanceIdentifier'],db['DBInstanceClass'],db['Engine'],db.get('DBName','NA'),
                                                                                                                                                                              db['Endpoint']['Address'],db['DBInstanceStatus'],str(db['AllocatedStorage']),str(db['InstanceCreateTime']),db['MultiAZ'],db['LicenseModel'],str(db.get('Iops','NA')),
                                                                                                                                                                              str(db['PubliclyAccessible']),db['StorageType'],str(db['StorageEncrypted']),str(db.get('DeletionProtection','NA')),cpu_max_util,db_max_connection)))
                    fout.write(("{},{},{},{},{},{},{},{},{},{},{},{},"
                                "{},{},{},{},{},{},{}\n".format(account, sessinfo['name'],db['DBInstanceIdentifier'],db['DBInstanceClass'],db['Engine'],db.get('DBName','NA'),
                                                                db['Endpoint']['Address'],db['DBInstanceStatus'],str(db['AllocatedStorage']),str(db['InstanceCreateTime']),db['MultiAZ'],db['LicenseModel'],str(db.get('Iops','NA')),
                                                                str(db['PubliclyAccessible']),db['StorageType'],str(db['StorageEncrypted']),str(db.get('DeletionProtection','NA')),cpu_max_util,db_max_connection)))
                resp=rdsc.describe_db_clusters()
                dbiter=resp['DBClusters']
                if dbiter:
                    #fout.write("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name']))
                    print(("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name'])))

                for db in dbiter:

                    if db['EngineMode'] == 'serverless':
                        #print (str(db))

                        print(("DatabaseName, {},DBClusterIdentifier, {},Status, {},Capacity, {}, MinCapacity, {}, MaxCapacity, {},AutoPause, {}".
                               format(db.get('DatabaseName','NA'),db['DBClusterIdentifier'],db['Status'],db['Capacity'],db['ScalingConfigurationInfo']['MinCapacity'],
                                      db['ScalingConfigurationInfo']['MaxCapacity'], db['ScalingConfigurationInfo']['AutoPause'])))

                        #fout.write("account,DatabaseName,DBClusterIdentifier,Status,Capacity, MinCapacity, MaxCapacity, AutoPause, \n")
                        fout.write("{},{}, {}, {}, {}, {}, {}, {}, {} \n".
                                   format(account,sessinfo['name'],db.get('DatabaseName','NA'),db['DBClusterIdentifier'],db['Status'],db['Capacity'],db['ScalingConfigurationInfo']['MinCapacity'],
                                          db['ScalingConfigurationInfo']['MaxCapacity'], db['ScalingConfigurationInfo']['AutoPause']))



            elif type == 'serverless':
                resp=rdsc.describe_db_clusters()
                dbiter=resp['DBClusters']
                #print ("in here {:}".format(str(dbiter)))

                #print str(dbiter)
                if dbiter:
                    #fout.write("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name']))
                    print(("\n\nAccount :  {:}  {:}, \n\n".format(account, sessinfo['name'])))

                for db in dbiter:

                    if db['EngineMode'] == 'serverless':
                        #print (str(db))

                        print(("DatabaseName, {},DBClusterIdentifier, {},Status, {},Capacity, {}, MinCapacity, {}, MaxCapacity, {},AutoPause, {}".
                               format(db.get('DatabaseName','NA'),db['DBClusterIdentifier'],db['Status'],db['Capacity'],db['ScalingConfigurationInfo']['MinCapacity'],
                                      db['ScalingConfigurationInfo']['MaxCapacity'], db['ScalingConfigurationInfo']['AutoPause'])))

                        #fout.write("account,DatabaseName,DBClusterIdentifier,Status,Capacity, MinCapacity, MaxCapacity, AutoPause, \n")
                        fout.write("{},{}, {}, {}, {}, {}, {}, {}, {} \n".
                                   format(account,sessinfo['name'],db.get('DatabaseName','NA'),db['DBClusterIdentifier'],db['Status'],db['Capacity'],db['ScalingConfigurationInfo']['MinCapacity'],
                                          db['ScalingConfigurationInfo']['MaxCapacity'], db['ScalingConfigurationInfo']['AutoPause']))



            ##print ("db instance : {:}, Auto Minor Version Upgrade : {:} ,  Maintanance Window : {:}". format(db['DBInstanceIdentifier'],db['AutoMinorVersionUpgrade'],db['PreferredMaintenanceWindow']))
            #fout.write("db instance ,{:}, Auto Minor Version Upgrade ,{:} ,  Maintanance Window ,{:} \n". format(db['DBInstanceIdentifier'],db['AutoMinorVersionUpgrade'],db['PreferredMaintenanceWindow']))
            ####fout.write(" ,{:},{:},{:} \n". format(db['DBInstanceIdentifier'],db['AutoMinorVersionUpgrade'],db['PreferredMaintenanceWindow']))




    except Exception as err:
        print((traceback.format_exc()))
        print(("List RDS   " + str(err)))

if __name__ == '__main__':
    list_rds_read_replica('All')
