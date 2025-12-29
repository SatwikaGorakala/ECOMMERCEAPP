class product:
    def __init__(self,product_id:int,product_name:str,price:float,stock:int):
        if not isinstance(product_id, int):
            raise TypeError("product_id must be integer")
        if not isinstance(product_name, str):
            raise TypeError("product_name must be string")
        if not isinstance(price, float):
            raise TypeError("price must be float")
        if not isinstance(stock, int):
            raise TypeError("stock must be integer")
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.stock=stock
    
    
    

p1=product(120,"watch",120.2,2000)
