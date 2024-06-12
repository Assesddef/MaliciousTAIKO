import os
import random
import time
from datetime import datetime, timedelta, timezone
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Setup Web3
w3 = Web3(Web3.HTTPProvider('https://rpc.taiko.xyz'))

# Private key from env
pk = os.getenv('PRIVATE_KEY')

# Wallet setup
acct = Account.from_key(pk)
addr = acct.address

print("Wallet Address:", addr)

# Contract details
contract_addr = '0xf89b01fa87a3e51bda2da67154ea35a3f84ec373'
if not Web3.is_checksum_address(contract_addr):
    contract_addr = Web3.to_checksum_address(contract_addr)
contract_abi = [
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "lend",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_addr, abi=contract_abi)

# Function to send a transaction
def send_tx(amt, gas_price):
    nonce = w3.eth.get_transaction_count(addr)
    txn = contract.functions.lend(amt).build_transaction({
        'chainId': 167000,
        'gas': 2000000,
        'gasPrice': gas_price,
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=pk)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return tx_hash

# Check if it's 1 AM UTC
def is_reset_time():
    now = datetime.now(timezone.utc)
    return now.hour == 1 and now.minute == 0

# Main function
def main():
    tx_count = 0
    reset_time = datetime.now(timezone.utc).replace(hour=1, minute=0, second=0, microsecond=0)
    if reset_time < datetime.now(timezone.utc):
        reset_time += timedelta(days=1)

    base_gas = w3.eth.gas_price
    max_gas = base_gas * 5

    while True:
        if tx_count < 5:
            # Check balance
            balance = w3.eth.get_balance(addr)
            gas_limit = 2000000
            gas_price = base_gas + (tx_count * w3.to_wei(1, 'gwei'))
            gas_price = min(gas_price, max_gas)
            tx_cost = gas_limit * gas_price

            # Check if balance covers tx cost
            if balance < tx_cost:
                print("Not enough funds. Skipping transaction.")
                break

            amt = random.randint(100000, 200000)
            sleep_time = random.randint(180, 600)
            tx_hash = send_tx(amt, gas_price)
            tx_link = f"https://taikoscan.io/tx/{tx_hash.hex()}"
            amt_decimal = amt / 1000000
            print(f"Transaction sent: {tx_link}, Amount: {amt_decimal} USD, Gas Price: {w3.from_wei(gas_price, 'gwei')} Gwei, Sleep Time: {sleep_time} seconds")
            tx_count += 1
            time.sleep(sleep_time)
        else:
            now = datetime.now(timezone.utc)
            if now >= reset_time:
                tx_count = 0
                reset_time += timedelta(days=1)
            else:
                time_to_reset = (reset_time - now).total_seconds()
                print(f"Sleeping until reset time in {time_to_reset // 60} minutes...")
                time.sleep(time_to_reset)

if __name__ == "__main__":
    main()
