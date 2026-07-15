"""
Consturct a dicitionary containing four product and theie prices. Prompt the user to
enter a product name. Use the in keyword to check the product exist if it exist print
the price else product not found
"""

Product = {
    "Laptop": 85000,
    "Keyboard": 500,
    "Mouse": 300,
    "Pendrive": 500,
}
product = input("Enter the Product Name: ")
print(Product.get(product, "Product Not Found"))
