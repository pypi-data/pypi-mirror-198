rlt = {}
tids = []
for trx in trxs:
    tid = trx["TrxId"]
    itype = trx.get("Content").get("type")
    iname = trx.get("Content").get("name")
    if iname.find("seg-") == -1:
        print(tid, iname)
    ts = Stime.ts2datetime(trx["TimeStamp"])
    if iname == "fileinfo":
        print(len(tids), tids)
        for x in range(len(tids)):
            if f"seg-{x+1}" not in tids:
                print("【ERROR】", f"seg-{x+1}", "not exists")
            if tids.count(f"seg-{x+1}") > 1:
                print("【ERROR】", f"seg-{x+1}", tids.count(f"seg-{x+1}"))
        else:
            print("+" * 100)
        print(iname, tid)
        tids = []
    else:
        tids.append(iname)
