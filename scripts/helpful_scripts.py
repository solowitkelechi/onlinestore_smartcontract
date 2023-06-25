from brownie import (
    network,
    accounts,
    config,
    Contract,
    web3,
)

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]

#contract_to_mock = {
#    "eth_usd_price_feed": MockV3Aggregator,
#}

DECIMALS = 18
INITIAL_VALUE = web3.toWei(2000, "ether")
BASE_FEE = 100000000000000000  # The premium
GAS_PRICE_LINK = 1e9  # Some value calculated depending on the Layer 1 cost and Link


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    print("Deploying Mock Price Feed...")
    mock_price_feed = MockV3Aggregator.deploy(
        decimals, initial_value, {"from": account}
    )
    print(f"Deployed to {mock_price_feed.address}")
    print("Deploying Mock DAI...")
    dai_token = MockDAI.deploy({"from": account})
    print(f"Deployed to {dai_token.address}")
    print("Deploying Mock WETH...")
    weth_token = MockWETH.deploy({"from": account})
    print(f"deployed to {weth_token.address}")
    print("Mocks Deployed")
