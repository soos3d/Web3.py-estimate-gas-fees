# Web3.py estimate gas fees
This script shows how you can estimate gas fees on an EVM blockchain, using a Chainstack node. You can use it to simply retrieve information to create an app like eth gas station, or to calculate how much the gas fee should be when sending a transaction using a bot written using web3.py.

You can also check my Skillshare class where I show the fundamentals about web3.py. WEB3.py: Interact with the Blockchain
Get 30 days for free using this link! https://skl.sh/3McEymV

There are two scripts here:
  - estimate_gas.py --> Retrieve and display information: Gas limit, base gas fee, priority gas fee(standard 2 Gwei, modifiable by the user), calculate hom much ETH will be used in gas. 
  
  - transaction_gas.py --> Uses a function to estimate how many Gwei are needed for sending ETH to another address, and shows it a built transaction as an example. 


Note that much of the code is just to make it look better once printed on the console. Like converting the Wei values into Gwei and Ether.

<b>What is Web3.py?</b>

Web3.py is a Python library for interacting with the Ethereum network (Or other networks based on the EVM).

It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

The original API was derived from the Web3.js Javascript API but has since evolved toward the needs and creature comforts of Python developers. (source: [Web3.py docs](https://web3py.readthedocs.io/en/stable/).)

<b>How do I use this program to estimate gas fees?</b>

1 - The Web3.py library must be installed in your environment.

2 - Have access to an HTTPS endpoint that allows creating the connection to the EVM. For the connection, it is recommended to use the service provided by [chainstack.com](https://chainstack.com/), where you can create your personal node on the cloud. You can register and create one node for free. This is the recommended option as not all the HTTPS endpoints that can be found online support the methods that can be used through Web3.py.

![162478127-94cd2344-72f1-4136-a220-8b2c8e52d194](https://user-images.githubusercontent.com/99700157/169823194-c3202f8f-5438-4a45-95e8-b2e1f6d44225.png)

Insert the URL you get from your Chainstack node in the 'node_url' variable.

```py
# Node endpoint
node_url = "CHAINSTACK_NODE_URL"

# Create the node connection
web3 = Web3(Web3.HTTPProvider(node_url))

# Verify if the connection is successful
if web3.isConnected():
    print("Connection Successful")
    print('-' * 50)
else:
    print("Connection Failed")
```

Customize the priority fee if you want. On Ethereum, 2 Gwei is generally the minimum required for your transaction to be picked by the miners. This is referred as 'miner tip' as well, you can increase it to incetivice them to pick up and process your transaction faster. 

```py
# set up the miner tip in wei
priority_fee = 2000000000       # 2 Gwei in wei
print('Priority fee: ' + str(web3.fromWei(priority_fee, 'gwei')) + ' Gwei')
```

Now, you can run the program and you will receive a result like this in the console:

```sh
Connection Successful
Latest block: 14934388
Gas limit: 21000
Base fee: 72.960051418 Gwei
Priority fee: 2 Gwei
Reasonable fee: 74.960051418 Gwei
------------------------------
Ether paid as gas fee: 0.001574161079778 ETH
```
