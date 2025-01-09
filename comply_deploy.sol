pragma solidity ^0.8.0;

contract HalalMarketplace {
    struct Product {
        string name;
        uint256 price;
        bool isHalal;
    }

    mapping(uint256 => Product) public products;
    uint256 public productCount;

    event ProductAdded(uint256 productId, string name, uint256 price, bool isHalal);

    function addProduct(string memory _name, uint256 _price, bool _isHalal) public {
        productCount++;
        products[productCount] = Product(_name, _price, _isHalal);
        emit ProductAdded(productCount, _name, _price, _isHalal);
    }

    function halalCertified(uint256 _productId) public view returns (bool) {
        return products[_productId].isHalal;
    }
}
