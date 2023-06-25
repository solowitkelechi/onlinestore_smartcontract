// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract OnlineStore is Ownable {
    address[] sellers;
    address public allowedTokenAddress;

    mapping(address => uint256) public sellersBalance;

    function approveSellTransaction(address _seller) public payable {
        require(msg.value > 0, "Amount must be more than zero");
        updateSellerBalance(_seller, msg.value);
    }

    function updateSellerBalance(address _seller, uint256 _amount) public {
        // add to token balance when seller's item is sold
        sellersBalance[_seller] = sellersBalance[_seller] + _amount;
        if (checkSellerList(_seller) == false) {
            sellers.push(_seller);
        }
    }

    function checkSellerList(address _seller) public view returns (bool) {
        for (uint256 _index = 0; _index < sellers.length; _index++) {
            if (sellers[_index] == _seller) {
                return true;
            }
        }
        return false;
    }

    function adminWithdraw() public payable onlyOwner {
        require(
            sellers.length > 0,
            "No sellers yet: no items sold on this network"
        );
        for (uint256 index = 0; index < sellers.length; index++) {
            payable(sellers[index]).transfer(sellersBalance[sellers[index]]);
            sellersBalance[sellers[index]] = 0;
        }
    }

    function withdraw() public {
        require(checkSellerList(msg.sender), "User has not sold any item yet.");
        uint256 balance = sellersBalance[msg.sender];
        require(balance > 0, "Your balance cannot be 0");
        payable(msg.sender).transfer(balance);
        sellersBalance[msg.sender] = 0;
        //removeFromList(msg.sender);
    }

    function checkSellerBalance(
        address _sellerAddress
    ) public view returns (uint256) {
        if (!checkSellerList(_sellerAddress)) {
            return 0;
        }
        return sellersBalance[_sellerAddress];
    }

    //function removeFromList(address _sellerAddress) public {
    //    for (uint256 index = 0; index < sellers.length; index++){
    //        if (sellers[index] == _sellerAddress){
    //            removeSeller(index);
    //        }
    //    }
    //}

    function removeSeller(uint256 _index) private {
        for (uint256 i = _index; i < sellers.length - 1; i++) {
            sellers[i] = sellers[i + 1];
        }
        sellers.pop();
    }
}
