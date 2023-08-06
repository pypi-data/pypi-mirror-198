from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://149.56.22.113:8545"))

w3.isConnected()

# 读取区块高度
w3.eth.blockNumber

# 当前节点是否正在同步
w3.eth.syncing

# 当前节点是否正在挖矿
w3.eth.mining

eos_contract_address = "0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0"

# 以下两个函数为检测地址正确性的函数，与实际查询业务无关
a = w3.isAddress(eos_contract_address)
b = w3.isChecksumAddress(eos_contract_address)
