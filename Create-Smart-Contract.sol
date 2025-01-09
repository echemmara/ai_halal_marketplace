pragma solidity ^0.8.0;

contract HalalMarketplace {
    address public owner;
    
    // Event for product added
    event ProductAdded(uint productId, string name, uint price, address vendor);
    
    struct Product {
        uint id;
        string name;
        uint price;
        address vendor;
        bool isHalal;
    }

    Product[] public products;
    
    // Halal certification (For simplicity, hardcoded here. Expand with AI or DB integration.)
    mapping(uint => bool) public halalCertified;

    constructor() {
        owner = msg.sender;
    }

    function addProduct(string memory _name, uint _price, bool _isHalal) public {
        uint productId = products.length;
        products.push(Product(productId, _name, _price, msg.sender, _isHalal));
        
        // Emit the product added event
        emit ProductAdded(productId, _name, _price, msg.sender);
    }
    
    function buyProduct(uint _productId) public payable {
        Product storage product = products[_productId];
        require(msg.value >= product.price, "Insufficient funds");
        require(product.isHalal == true, "Product not Halal");
        
        // Transfer payment to vendor
        payable(product.vendor).transfer(product.price);
    }
}
