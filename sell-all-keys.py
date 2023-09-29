# Friend.tech Liquidate Account
# Over the hype? Run this script to sell all keys, and send ETH on BASE back to another wallet.    
import requests
from web3 import Web3
from web3.middleware import geth_poa_middleware,construct_sign_and_send_raw_middleware

# USER VARIABLES
provider_rpc ="https://mainnet.base.org"
withdrawal_wallet_addr = "WALLET_ADDRESS_2_WITHDRAW"
friendtech_wallet = "FRIENDTECH_WALLET"
friendtech_private_key = "PRIVATE_KEY_EXPORT_FROM_FRIENDTYECH"

def get_keys_held(address):
    url = f"https://prod-api.kosetto.com/users/{address}/token-holdings"
    headers = {'accept': 'application/json, text/plain, */*',
                'content-type': 'application/json',
                "referrer": "https://www.friend.tech/",
                "referrerPolicy": "strict-origin-when-cross-origin",}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
    except Exception as e:
        print(e)
    return data


# URL: https://basescan.org/address/0xcf205808ed36593aa40a44f10c7f7c2f67d4a4d4
friendtech_contract_addr = "0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4"
friends_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"trader","type":"address"},{"indexed":false,"internalType":"address","name":"subject","type":"address"},{"indexed":false,"internalType":"bool","name":"isBuy","type":"bool"},{"indexed":false,"internalType":"uint256","name":"shareAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"protocolEthAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"subjectEthAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"supply","type":"uint256"}],"name":"Trade","type":"event"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"buyShares","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getBuyPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getBuyPriceAfterFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"supply","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getSellPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getSellPriceAfterFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeeDestination","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sharesSubject","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"sellShares","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeDestination","type":"address"}],"name":"setFeeDestination","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feePercent","type":"uint256"}],"name":"setProtocolFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_feePercent","type":"uint256"}],"name":"setSubjectFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"sharesBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"sharesSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"subjectFeePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

# initalize web3
web3 = Web3(Web3.HTTPProvider(provider_rpc))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
#init friends contract
friends_contract = web3.eth.contract(web3.to_checksum_address(friendtech_contract_addr), abi=friends_abi)

#get all held keys from friends api, could also be done on chain, but this is faster.
print("Getting Keys Held.")
held_keys = (get_keys_held(friendtech_wallet))['users']

print(f"You hold {len(held_keys)} keys.")
total_sale = 0
sale_deets = []
#loop through all keys and get sale data/pricing
for key in held_keys:
    sell_after_fee = friends_contract.functions.getSellPriceAfterFee(web3.to_checksum_address(key['address']), int(key['balance'])).call()
    print(f"{key['twitterName']} : {web3.from_wei(sell_after_fee,'ether')} ETH")
    total_sale += web3.from_wei(sell_after_fee,'ether')
    sale_deets.append({"address":key["address"],"balance":key["balance"],"sell_after_fee":web3.from_wei(sell_after_fee,'ether'),"sale_price":(friends_contract.functions.getSellPrice(web3.to_checksum_address(key['address']), int(key['balance'])).call(),'ether')})

print(f"Selling All Keys For {total_sale} ETH.")
#Get Current Nonce for wallet
current_nonce = web3.eth.get_transaction_count(friendtech_wallet)

print(f"Current Wallet Nonce: {current_nonce}")
#Loop through all keys and sell
for key in sale_deets:
    #create data TX
    data_tx = friends_contract.encodeABI(fn_name='sellShares', args=[web3.to_checksum_address(key['address']), int(key['balance'])])
    #build tx params. Value is what the value of the key is without fee. Required Input
    tx_params = {
                    'from': friendtech_wallet,
                    'to': friendtech_contract_addr,
                    'chainId': 8453,
                    'value': int(key['sale_price'][0]),
                    'gasPrice': web3.eth.gas_price,
                    'gas': 6500000,
                    'nonce': current_nonce,
                    'data': data_tx
                }
    #Sign and send TX
    signed_txn = web3.eth.account.sign_transaction(tx_params, private_key=friendtech_private_key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Sent Transaction: {tx_token.hex()}")
    print(f"---------------- {key['address']} Sell Successful!------------------")
    #increment nonce manually to quickly send next TX
    current_nonce += 1


#Time to Send to another Base Wallet
tx_params = {
                'from': friendtech_wallet,
                'to': withdrawal_wallet_addr,
                'chainId': 8453,
                'value': web3.eth.get_balance(friendtech_wallet) - (web3.to_wei(.0001, 'ether')),
                'maxFeePerGas': web3.to_wei((1.5), 'gwei'),
                'maxPriorityFeePerGas': web3.to_wei(.1, 'gwei'),
                'gas': 22000,
                'nonce': current_nonce
            }
#Sign and send TX
try:
    signed_txn = web3.eth.account.sign_transaction(tx_params, private_key=friendtech_private_key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Sent Transaction: {tx_token.hex()}")
    print(f"---------------- {withdrawal_wallet_addr} Withdraw Successful!------------------")
except Exception as e:
    print("Failed to Withdraw!")
    print(e)
    
