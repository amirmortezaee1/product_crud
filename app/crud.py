class Product:
    def __init__(self,
                 title,
                 short_description,
                 description:str,
                 slug:str,
                 permalink:str,
                 price:float,
                 regular_price,
                 sale_price,
                 manage_stoke,
                 stoke_quantity,
                 isAvailable,
                 isVisible
                 ):
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.isAvailable = isAvailable
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stoke = manage_stoke
        self.stoke_quantity = stoke_quantity
        self.isVisible = isVisible
