from scripts.helpful_scripts import get_account
from brownie import OnlineStore, network, config
from web3 import Web3
import yaml, json, os, shutil


def deploy():
    account = get_account()
    print(network.show_active())
    online_store = (
        OnlineStore[-1]
        if OnlineStore
        else OnlineStore.deploy(
            {"from": account},
        )
    )
    return online_store


def approveSellTransaction(seller):
    account = get_account()
    online_store = OnlineStore[-1]
    tx = online_store.approveSellTransaction(
        seller, {"from": account, "value": Web3.toWei(0.1, "ether")}
    )
    tx.wait(1)


def checkSellerList(seller):
    account = get_account()
    online_store = OnlineStore[-1]
    tx = online_store.checkSellerList(seller, {"from": account})
    print(tx)


def checkSellerBalance(address):
    account = get_account()
    online_store = OnlineStore[-1]
    tx = online_store.checkSellerBalance(address, {"from": account})
    print(tx)


def adminWithdraw():
    account = get_account()
    online_store = OnlineStore[-1]
    tx = online_store.adminWithdraw({"from": account})
    tx.wait(1)


def main():
    adminWithdraw()
