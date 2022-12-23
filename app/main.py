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
print(repr(instance))

# it will give us true value
print(isinstance(instance, Product))

# it give us class type result
print(type(Product))