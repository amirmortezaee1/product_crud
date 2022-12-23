class Product:
    _product: []
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
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.isAvailable = is_available
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stoke = manage_stoke
        self.stoke_quantity = stoke_quantity
        self.is_visible = is_visible

    def __repr__(self):
        product_detail = f"\
        title is {self.title}\n\
        short_description is {self.short_description}\n\
        description is {self.description} and sale price is {self.sale_price}"
        return product_detail

    def add_product(self):
        self._product.append(self)
        return self.__repr__()

    def read_product(self):
        for i in self._product:
            print(i)

    def update_product(self, values:[]):
        if len(values) != 12:
            print("the input values are less or more than 12")
        else:
            if len(self._product == 0):
                print("the product is empty so the value will added")
            self._product.clear()
            for i in values:
                self._product.append(i)
            print("Updated!")
            return(self.__repr__())

    def delete_product(self):
        if self._product == []:
            print('nothing is hear')
        else:
            print(self._product.clear())


