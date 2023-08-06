import datetime

import rumpy.utils as utils
from rumpy import FullNode

client = FullNode()

seed = client.api.create_group("mytest_pubqueque")
client.group_id = seed["group_id"]


def test_basic():
    r = client.api.pubqueue()
    print(r)


def test_update():
    for i in range(10):
        client.api.send_note(content=f"{str(i)*10}", group_id=seed["group_id"])

    data = client.api.pubqueue()
    print(data)

    for idata in data:
        s1 = utils.timestamp_to_datetime(idata["UpdateAt"])
        s2 = utils.timestamp_to_datetime(idata["Trx"]["TimeStamp"])
        s3 = utils.timestamp_to_datetime(idata["Trx"]["Expired"])
        s4 = datetime.datetime.now()
        tid = idata["Trx"]["TrxId"]
        print(idata["State"], tid, s2, s1 - s2)


if __name__ == "__main__":
    test_basic()
    test_update()
