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
