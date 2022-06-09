from web3 import Web3

node_url = "CHAINSTACK NODE URL"

web3 = Web3(Web3.HTTPProvider(node_url))

# verify if the connection is successful
if web3.isConnected():
    print("Connection Succsessful")
else:
    print("Connection Failed")

# retrieve the latest block
last = web3.eth.block_number
print('Latest block:', last)

# retrieve the gas limit for this simulated transaction. "value" is the latest block encoded in hex
gas_limit = web3.eth.estimate_gas(({"from":"0x43e4715ae093a4C86B5eCdDb52216c4f879e9672","to":"0x7Be657948CA28a51dcccBf93fdb932a033AdfFbe","value":"6c6174657374"}))
print('Gas limit:', gas_limit)

# retrieve the base fee in wei, then displays it in Gwe
base_fee = web3.eth.gas_price
print('Base fee: ' + str(web3.fromWei(base_fee, 'gwei')) + ' Gwei')

# set up the miner tip in wei
priority_fee = 2000000000       # 2 Gwei in wei
print('Priority fee: ' + str(web3.fromWei(priority_fee, 'gwei')) + ' Gwei')

# generate a total fee 
total_fee = base_fee + priority_fee
fee_gwei = web3.fromWei(total_fee, 'gwei')
print('Reasonable fee: ' + str(fee_gwei) + ' Gwei')

print('-' * 30)

# calculate how much ETH will be used as gas for this transaction
gas_fee = total_fee * gas_limit
print('Ether paid as gas fee: ' + str(web3.fromWei(gas_fee, 'ether')) + ' ETH')
