from tests import client


def test_network():
    seed = client.api.create_group("mytest_network")
    client.group_id = seed["group_id"]
    r = client.api.node_info().get("peers")
    print(r)
    peers = [
        "/ip4/101.34.248.248/tcp/50124/ws/p2p/16Uiu2HAm5UUssKUda49331pt8uNzqxn789ZazQGmuP7G6ZX97MuZ",
        "/ip4/106.54.162.192/tcp/61985/ws/p2p/16Uiu2HAm7ktJbDJN85GduWQiGgyYYpTphKNEWGK23t7GHcPR16gq",
        "/ip4/94.23.17.189/tcp/10666/p2p/16Uiu2HAmGTcDnhj3KVQUwVx8SGLyKBXQwfAxNayJdEwfsnUYKK4u",
    ]
    client.api.connect_peers(peers)
