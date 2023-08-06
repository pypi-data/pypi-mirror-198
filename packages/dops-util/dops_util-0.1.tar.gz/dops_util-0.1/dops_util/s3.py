
#from .global_var import *
from dops_util import *
import botocore

def list_bucket_replication(account='ALL'):
    print("################Getting S3 Bucket Replication ################")
    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
    else:
        Account_Session.initialize_all()
    fout=open(cost_dir+'list_s3_replication' + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(72))

    #fout.write("{:15},{:20},{:80},{:15},{:10} \n".format('Account','AccountName','Bucket_Name','LifeCycle','Standard(GB)'
    fout.write("{:15},{:20},{:50},{:15},{:10},{:10},{:10},{:30},{:15},{:30},{:10},{:10} \n".format('Account','AccountName','Bucket_Name','rule_id',
    'Filter_Prefix','Status','Destination_Bucket','Dest_Bucket_Account','Dest_Bucket_Account_Name','Replication IAM Role','Bucket_Versioning','DelMarkRep_Status'))

    bucket_info_all={}
    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding S3 Bucket info  on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        s3_res = sessinfo['session'].resource('s3', region_name="us-east-1")
        bucket_list = s3_res.buckets.all()
        for s3_bucket in bucket_list:
            #bucket_info_all.update({'bucket_name':s3_bucket.name,'info':{'account':account,'account_name':sessinfo['name']}})
            bucket_info_all.update({s3_bucket.name: {'account':account,'account_name':sessinfo['name']}})
    #print(bucket_info_all)


    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding S3 Replication Config  on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        s3_cl = sessinfo['session'].client('s3', region_name="us-east-1")
        s3_res = sessinfo['session'].resource('s3', region_name="us-east-1")

        bucket_list = s3_res.buckets.all()

        s3_int_tier_list=[]
        for bucket_obj in bucket_list:
            lcycle_list=[]
            s3_std_class='NA'
            try:
                # response = s3_cl.get_bucket_lifecycle(
                #     Bucket=bucket_obj.name
                # )
                config = s3_cl.get_bucket_replication(Bucket=bucket_obj.name)['ReplicationConfiguration']
                bucket_vers=s3_cl.get_bucket_versioning(Bucket=bucket_obj.name)

                #print (str(config['ReplicationConfiguration']))
                #print ('configall ',config)
                #print('Roles --- ',config['Role'])
                for rule in config['Rules']:
                    role=config['Role']
                    filt='NA'
                    if rule.get('Filter','NA') != 'NA':
                        filt=rule['Filter'].get('Prefix','NA')
                    del_marker='NA'
                    if rule.get('DeleteMarkerReplication','NA') != 'NA':
                        del_marker=rule['DeleteMarkerReplication'].get('Status','NA')
                    print (bucket_obj.name,rule," --- ", rule['ID'],filt,rule['Status'],
                           rule['Destination']['Bucket'],bucket_info_all[bucket_obj.name]['account'],
                           bucket_info_all[bucket_obj.name]['account_name'],
                           role,bucket_vers['Status'],
                           del_marker)
                           #rule['Destination']['Account'],
                           #rule['Destination']['StorageClass'],


                    out_format="{:15},{:20},{:50},{:15},{:10},{:10},{:10},{:30},{:15},{:30},{:10},{:10}".format(account,sessinfo['name'],bucket_obj.name,
                                                                                                                           rule['ID'],filt,rule['Status'],
                                                                                                                           rule['Destination']['Bucket'],
                                                                                                                        bucket_info_all[bucket_obj.name]['account'],
                                                                                                                        bucket_info_all[bucket_obj.name]['account_name'],
                                                                                                                           role,bucket_vers['Status'],
                                                                                                                           del_marker)



                    print (out_format)
                    fout.write(out_format + '\n')




            except botocore.exceptions.ClientError:
                #print("Bucket: ",bucket_obj.name," Replication config not enabled. Will enable versioning on source bucket and create a replication config")
                pass
            # GET VERSIONING
            # try:
                #client.get_bucket_versioning(Bucket=bucket)

def  list_s3_int_tier(account='All'):
    print("################Getting S3 Intelligent Tiering Info ################")

    fout=open(cost_dir+'list_s3_int_tier' + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()

    Account_Session.get_account_list()
    lng=len(Account_Session.ACCLIST)
    recon=0
    inst_dict={}
    starttime=endtime - datetime.timedelta(hours=int(72))
    #starttime=endtime - datetime.timedelta(hours=int(720))
    #fout.write("{:15},{:20},{:15},{:8},{:24},{:15},{:10},{:24},{:20},{:20},{:20},{:20},{:20} \n".format('Account','AccountName','DBClusterIdentifier','DatabaseName','Status','EndPoint',
    #                                                                   'ReaderEndpoint','MultiAZ','EngineVersion','DB_Identifier','Writer', 'DBClusterInstanceClass','ReadReplicaIdentifiers'))
    fout.write("{:15},{:20},{:80},{:15},{:10},{:10},{:10},{:10},{:10},"
               "{:10},{:10} \n".format('Account','AccountName','Bucket_Name','LifeCycle','Standard(GB)','Int-FA(GB)','Int-IA(GB)',
                                                            'Int-Archive-Instant-Access(GB)','Int-Archive-Access(GB)','Int-Deep-Archive(GB)','Int-Tiering-Config'
                                                           ))





    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
        last_cnt=2

    else:
        #Account_Session.initialize_all()
        last_cnt= int(lng/acc_step)+2


    for cnt in range(1,last_cnt):
        if last_cnt != 2:
            Account_Session.SESS_DICT={}
            Account_Session.initialize(cnt)
        elif last_cnt == 2:
            print("no collective session connections are  required")




        for account,sessinfo in Account_Session.SESS_DICT.items():
            print('\n\n\n====================Finding S3 Intelligent Tiering  on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
            s3_cl = sessinfo['session'].client('s3', region_name="us-east-1")
            s3_res = sessinfo['session'].resource('s3', region_name="us-east-1")

            cw_res = sessinfo['session'].resource('cloudwatch', region_name="us-east-1")

            cw=CloudWatchWrapper(cw_res)
            bucket_list = s3_res.buckets.all()
            s3_int_tier_list=[]
            for bucket_obj in bucket_list:
                try:
                    print ("getting info bucket ",bucket_obj.name)
                    response = s3_cl.get_bucket_lifecycle(
                        Bucket=bucket_obj.name
                    )
                    print (response['Rules'])
                    if response['Rules'][0]['ID'] == 'IntelligentTiering':
                        s3_int_tier_list.append(bucket_obj.name)
                #except Exception as err:
                #    raise
                except botocore.exceptions.ClientError as err:
                    if "NoSuchLifecycleConfiguration" in str(err) or 'AccessDenied' in str(err):
                        print (str(err))
                        print ("continue")
                        pass
                    else:
                        raise
            print ('int tier bucke ',str(s3_int_tier_list))
            for s3_int_tier in s3_int_tier_list:
                arch_aa='NA'
                arch_daa='NA'
                bucken_dim={'Name':'BucketName','Value':s3_int_tier}
                dimension_STD=[
                    bucken_dim,
                    {
                        'Name': 'StorageType',
                        'Value': 'StandardStorage'
                    }
                ]
                dimension_FA=[
                    bucken_dim,
                    {
                        'Name': 'StorageType',
                        'Value': 'IntelligentTieringFAStorage'
                    }
                ]
                dimension_IA=[
                    bucken_dim,
                    {
                        'Name': 'StorageType',
                        'Value': 'IntelligentTieringIAStorage'
                    }
                ]
                dimension_AIA=[
                    bucken_dim,
                    {
                        'Name': 'StorageType',
                        'Value': 'IntelligentTieringAIAStorage'
                    }
                ]

                response=s3_cl.list_bucket_intelligent_tiering_configurations(Bucket=s3_int_tier)
                if response:
                    #print('rrr',str(response))
                    if not response.get('IntelligentTieringConfigurationList','NA') == 'NA':
                        for resp in response['IntelligentTieringConfigurationList']:
                            print('config ',resp['Status'],str(resp['Tierings']))
                            for arch in resp['Tierings']:
                                if arch['AccessTier'] == 'ARCHIVE_ACCESS':
                                    arch_aa=arch['Days']
                                if arch['AccessTier'] == 'DEEP_ARCHIVE_ACCESS':
                                    arch_daa=arch['Days']
                if arch_aa == 'NA' or arch_daa == 'NA':
                    IntTieringConfig=False
                else:
                    IntTieringConfig=True


                int_tier_std_class=cw.get_metric_statistics('AWS/S3','BucketSizeBytes', starttime, endtime, 7200, 'Average',dimension_STD,unit=1000000000)
                int_tier_fa_class=cw.get_metric_statistics('AWS/S3','BucketSizeBytes', starttime, endtime, 7200, 'Average',dimension_FA,unit=1000000000)
                int_tier_ia_class=cw.get_metric_statistics('AWS/S3','BucketSizeBytes', starttime, endtime, 7200, 'Average',dimension_IA,unit=1000000000)
                int_tier_aia_class=cw.get_metric_statistics('AWS/S3','BucketSizeBytes', starttime, endtime, 7200, 'Average',dimension_AIA,unit=1000000000)
                #print('int_tier ',s3_int_tier,str(int_tier_std_class),str(int_tier_fa_class),str(int_tier_ia_class),int_tier_aia_class,arch_aa,arch_daa)


                out_format="{:15},{:20},{:80},{:15},{:10},{:10},{:10},{:10},{:10},{:10},{:10}".format(account,sessinfo['name'],s3_int_tier,'Intelligent-Tiering',int_tier_std_class,
                                     int_tier_fa_class,int_tier_ia_class,int_tier_aia_class,arch_aa,arch_daa,str(IntTieringConfig))

                print(out_format)
                fout.write(out_format + '\n')

def  list_s3_std_tier(account='All'):
    print("################Getting S3 Metric ################")
    if account.upper() != 'ALL':
        Account_Session.build_sess_subaccount(subaccount=account)
    else:
        Account_Session.initialize_all()
    fout=open(cost_dir+'list_s3_std_tier' + '_'+date+'.txt','w')
    endtime=datetime.datetime.utcnow()
    starttime=endtime - datetime.timedelta(hours=int(72))

    fout.write("{:15},{:20},{:80},{:15},{:10} \n".format('Account','AccountName','Bucket_Name','LifeCycle','Standard(GB)'
                                       ))



    for account,sessinfo in Account_Session.SESS_DICT.items():
        print('\n\n\n====================Finding S3 Standard Tiering  on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
        s3_cl = sessinfo['session'].client('s3', region_name="us-east-1")
        s3_res = sessinfo['session'].resource('s3', region_name="us-east-1")

        cw_res = sessinfo['session'].resource('cloudwatch', region_name="us-east-1")

        cw=CloudWatchWrapper(cw_res)
        bucket_list = s3_res.buckets.all()
        s3_int_tier_list=[]
        for bucket_obj in bucket_list:
            lcycle_list=[]
            s3_std_class='NA'
            try:
                response = s3_cl.get_bucket_lifecycle(
                    Bucket=bucket_obj.name
                )
                print (response['Rules'])

                for lcycle in response['Rules']:
                    print('lcycle ',lcycle['ID'])
                    lcycle_list.append(lcycle['ID'])
            except botocore.exceptions.ClientError as err:
                if "NoSuchLifecycleConfiguration" in str(err) or 'AccessDenied' in str(err):
                    print (str(err))
                    print ("continue")
                    pass
                else:
                    raise


            bucken_dim={'Name':'BucketName','Value':bucket_obj.name}
            dimension_STD=[
                bucken_dim,
                {
                    'Name': 'StorageType',
                    'Value': 'StandardStorage'
                }
            ]


            s3_std_class=cw.get_metric_statistics('AWS/S3','BucketSizeBytes', starttime, endtime, 7200, 'Average',dimension_STD,unit=1000000000)
            print (bucket_obj.name,str(lcycle_list),s3_std_class)
            out_format="{:15},{:20},{:80},{:15},{:10}".format(account,sessinfo['name'],bucket_obj.name,str(';'.join(lcycle_list)),s3_std_class)

            print(out_format)
            fout.write(out_format + '\n')




def  list_s3_storage_class_metric(account='All',region='us-east-1'):


        storage_class=[
        'StandardStorage',
        'IntelligentTieringAAStorage',
        'IntelligentTieringAIAStorage',
        'IntelligentTieringDAAStorage',
        'IntelligentTieringFAStorage',
        'IntelligentTieringIAStorage',
        'StandardIAStorage',
       # 'StandardIASizeOverhead',
       # 'IntAAObjectOverhead',
       # 'IntAAS3ObjectOverhead',
       # 'IntDAAObjectOverhead',
       # 'IntDAAS3ObjectOverhead',
        'OneZoneIAStorage',
        #'OneZoneIASizeOverhead',
        'ReducedRedundancyStorage',
       # 'GlacierInstantRetrievalStorage',
        'GlacierStorage',
       # 'GlacierStagingStorage',
       # 'GlacierObjectOverhead',
       # 'GlacierS3ObjectOverhead',
        'DeepArchiveStorage',
       # 'DeepArchiveObjectOverhead',
       # 'DeepArchiveS3ObjectOverhead',
       # 'DeepArchiveStagingStorage'
        ]




        if type != 'All':
            Account_Session.build_sess_subaccount(account)
            fout=open(cost_dir+'list_s3_storage_class_metric_' + account + '_'+date+'.txt','w')



        else:
            Account_Session.initialize_all()
            fout=open(cost_dir+'list_s3_storage_class_metric' + '_'+date+'.txt','w')


        endtime=datetime.datetime.utcnow()
        starttime=endtime - datetime.timedelta(hours=int(72))


        fout.write("{:15},{:20},{:80},{:15},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10}\n".
                   format('Account',
                          'AccountName',
                          'Bucket_Name',
                          'Life_Cycle',
                          'LCycle_Status',
                          'Std(GB)',
                          'Int_AAS(GB)',
                          'Int_AIAS(GB)',
                          'Int_DAAS(GB) ',
                          'Int_FAS(GB)',
                          'Int_IAS(GB)',
                          'Std_IAS(GB)',
                          'OneZoneIAS(GB)',
                          'ReducedRedund(GB)',
                          'Glacier(GB)',
                          'DeepArchive(GB)')
                   )





        print("################Getting S3 Bucket Storage Class Metric ################")
        Account_Session.get_account_list()
        lng=len(Account_Session.ACCLIST)
        recon=0
        inst_dict={}


        if account.upper() != 'ALL':
            Account_Session.build_sess_subaccount(subaccount=account)
            last_cnt=2

        else:
            #Account_Session.initialize_all()
            last_cnt= int(lng/acc_step)+2


        for cnt in range(1,last_cnt):
            if last_cnt != 2:
                Account_Session.SESS_DICT={}
                Account_Session.initialize(cnt)
            elif last_cnt == 2:
                print("no collective session connections are  required")


            for account,sessinfo in Account_Session.SESS_DICT.items():
                print('\n\n\n====================Finding S3 Bucket Existing Storage Class Usage on account : ' + account + ":" + sessinfo['name'] + ' ============================\n\n\n')
                s3_cl = sessinfo['session'].client('s3', region_name=region)
                s3_res = sessinfo['session'].resource('s3', region_name=region)

                cw_res = sessinfo['session'].resource('cloudwatch', region_name=region)

                cw=CloudWatchWrapper(cw_res)
                bucket_list = s3_res.buckets.all()
                bucket_info_list=[]

                for bucket_obj in bucket_list:
                    bucket_lc_rules_list=[]
                    bucket_info_dict={}


                    try:
                        print ("getting info bucket ",bucket_obj.name)
                        resp = s3_cl.get_bucket_lifecycle(
                            Bucket=bucket_obj.name
                        )
                        for response in resp['Rules']:
                            bucket_lc_rules_dict={}
                            print ('life_cycle:  ',response['ID'],' Storage Class :',response['ID'],' Status: ',response['Status'])
                            bucket_lc_rules_dict.update({'life_cycle':response['ID'],'Storage Class':response['ID'],'Status':response['Status']})
                            bucket_lc_rules_list.append(bucket_lc_rules_dict)

                    except botocore.exceptions.ClientError as err:
                        if "NoSuchLifecycleConfiguration" in str(err) or 'AccessDenied' in str(err):
                            print (str(err))
                            bucket_lc_rules_dict={}

                            bucket_lc_rules_dict.update({'life_cycle':'NA','Storage Class':'NA','Status':'NA'})
                            bucket_lc_rules_list.append(bucket_lc_rules_dict)
                            #print ("continue")
                            #pass

                    except Exception as err:
                        print((traceback.format_exc()))
                        print(str(err))
                        raise


                    bucket_info_dict.update({'bucket_name':bucket_obj.name})
                    bucket_info_dict.update({'life_cycle':bucket_lc_rules_list})



                    bucken_dim={'Name':'BucketName','Value':bucket_obj.name}
                    for stor_class_dimension in storage_class:
                        dimension=[
                            bucken_dim,
                            {
                                'Name': 'StorageType',
                                'Value': stor_class_dimension
                            }
                        ]
                        # print ('dimension', str(dimension))
                        stor_class_metric=cw.get_metric_statistics('AWS/S3','BucketSizeBytes', starttime, endtime, 7200, 'Average',dimension,unit=1000000000)
                        bucket_info_dict.update({stor_class_dimension:stor_class_metric})
                        print(bucket_obj.name,str(stor_class_metric))
                    bucket_info_list.append(bucket_info_dict)


                for bm in bucket_info_list:
                    # print("stats ",str(bm))


                    out_format=("{:15},{:20},{:80},{:15},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10},{:10}\n".
                       format(account,
                              sessinfo['name'],
                              bm['bucket_name'],
                              #';'.join(bm.get('life_cyle','NA')),
                              #';'.join(str(bm['life_cycle'])),
                              ### Need To Be Improved Later
                              bm['life_cycle'][0]['life_cycle'],
                              bm['life_cycle'][0]['Status'],
                              ### Need To Be Improved Later
                              bm['StandardStorage'],
                              bm['IntelligentTieringAAStorage'],
                              bm['IntelligentTieringAIAStorage'],
                              bm['IntelligentTieringDAAStorage'],
                              bm['IntelligentTieringFAStorage'],
                              bm['IntelligentTieringIAStorage'],
                              bm['StandardIAStorage'],
                              bm['OneZoneIAStorage'],
                              bm['ReducedRedundancyStorage'],
                              bm['GlacierStorage'],
                              bm['DeepArchiveStorage']
                            )
                       )


                    print(out_format)
                    fout.write(out_format)














        #fout.write(out_format + '\n')




