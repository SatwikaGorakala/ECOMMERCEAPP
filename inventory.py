import product
class inventory:
    def __init__(self):
        self.product_inventory={}
    
    def add_product(self,product_id:int,product_name:str,price:float,stock:int):
        if not isinstance(product_id, int):
            raise TypeError("product_id must be integer")
        if not isinstance(product_name, str):
            raise TypeError("product_name must be string")
        if not isinstance(price, float):
            raise TypeError("price must be float")
        if not isinstance(stock, int):
            raise TypeError("stock must be integer")
    
        p2=product.product(product_id,product_name,price,stock)
        self.product_inventory[product_id]=p2 # adding product to dictionay object(product_inventory) using key(productid)
    


    def update_product(self,product_id:int,stock_quantity:int):
        if not isinstance(product_id, int):
            raise TypeError("product_id must be integer")
        if not isinstance(stock_quantity, int):
            raise TypeError("stock_quantity must be integer")
        #p3=product(product_id,stock_quantity)
        prd = self.product_inventory[product_id]  # fetchin product from  dictionay object(product_inventory) using key(productid)
        prd.stock=prd.stock+stock_quantity
        

        
    
       



