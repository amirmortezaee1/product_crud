from product import Product

instance = Product("pizza",
                   "italian",
                   "delicious italian pizza",
                   "ok",
                   "https",
                   20,
                   22,
                   24,
                   10,
                   5,
                   True,
                   True,
                   )

# sample list for crud methods
sample = ["pizza", "italian", "delicious italian pizza", "ok", "https", 20, 22, 24, 10, 5, True, True]

# use crud methods that implemented in product.py file
print(instance.add_product())
print(instance.read_product())
print(instance.update_product(sample))
print(instance.delete_product())

# if file run directly, this pices of code will run:
if __name__ == "__main__":
    # it will show us
    print(repr(instance))

    # result of this code wille be true
    print(isinstance(instance, Product))

    # result of this code will be true
    print(type(Product))