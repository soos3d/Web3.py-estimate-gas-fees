from web3 import Web3

node_url = "CHAINSTACK NODE URL"

web3 = Web3(Web3.HTTPProvider(node_url))

# verify if the connection is successful 
if web3.isConnected():
    print("Connection Succsessful")
else:
    print("Connection Failed")

# function to estimate how many gwei to use for gas.     
def estimate_gas():
    base_fee = web3.eth.gas_price
    priority_fee = 2000000000 # 2 Gwei in wei
    total_fee = base_fee + priority_fee   

    return total_fee  # this is returned in wei

# retrieve the latest block number  
last = web3.eth.block_number
print('Latest block:', last)

# simulate a transaction and retrieve gas limit
gas_limit = web3.eth.estimate_gas(({"from":"0x43e4715ae093a4C86B5eCdDb52216c4f879e9672","to":"0xA090e606E30bD747d4E6245a1517EbE430F0057e"}), "latest")
print('Gas limit:', gas_limit)

# use the function to retrieve how many gwei to use for gas
total_fee = estimate_gas()

# convert Wei to Gwei
fee_gwei = web3.fromWei(total_fee, 'gwei')
print('Reasonable fee: ' + str(fee_gwei) + ' Gwei')

print('-' * 30)

# calculate and display how much ETH is used as gas 
gas_fee = estimate_gas() * gas_limit
print('Ether paid as gas fee:' + str(web3.fromWei(gas_fee, 'ether')) + ' ETH')

# this is not the most secure way to keep these, but it works for the example
# fill up with your data
sender = 'SENDER ADDRESS'
receiver = 'RECEIVER ADDRESS'
privateKey = 'PRIVATE KEY'      # used to sign the transaction

#nonce, retrieve how many transactions the sender address has made
nonce = web3.eth.getTransactionCount(sender)

# build the transaction
tx = {
    'nonce' : nonce,
    'to': receiver,
    'value': web3.toWei(0.01, 'ether'),   # value to send
    'gas': gas_limit,
    'gasPrice' : estimate_gas()           # use the function to estimate the gas fee live
}

# sign tx using the private key 
signed_tx = web3.eth.account.signTransaction(tx, privateKey)

# send transaction, and print the tx hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print('Transaction hash:', web3.toHex(tx_hash))
