class Product:
    # use a list for storing product values 
    _product = []

    def __init__(self,
                 title,
                 short_description: "",
                 description: "",
                 slug: "",
                 permalink: "",
                 price: 0,
                 regular_price: 0,
                 sale_price: 0,
                 manage_stoke: 0,
                 stoke_quantity: 0,
                 is_available: True,
                 is_visible: True,
                 ):
        self.id = id
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stoke = manage_stoke
        self.stoke_quantity = stoke_quantity
        self.is_visible = is_visible

    def __repr__(self):
        return f'Inforamation of Product:({self.id},{self.title},{self.short_description},{self.description},{self.slug}' \
        f'{self.permalink},{self.is_available},{self.price},{self.regular_price},{self.sale_price}' \
        f'{self.manage_stoke},{self.stoke_quantity},{self.is_visible})'

    # add value to _product
    def add_product(self):
        self._product.append(self)
        return self.__repr__()

    # type values of _product
    def read_product(self):
        for i in self._product:
            print(i)

    # update_product give list of values and replace them with older value product
    def update_product(self, values: []):
        # check the input value size
        if len(values) != 12:
            print("the input values are less or more than 12")
        else:
            # check the _product list not empty
            if len(self._product) == 0:
                print("the product storage is empty so the value will added")
            # clear the _product
            self._product.clear()
            # update the _product with input values
            for i in values:
                self._product.append(i)
            print("Updated!")
            # return input values
            return self.__repr__()

    # delete the _product information
    def delete_product(self):
        # check _product is empty or not
        if self._product == []:
            print('nothing is hear')
        # clear the __product
        else:
            print(self._product.clear())
