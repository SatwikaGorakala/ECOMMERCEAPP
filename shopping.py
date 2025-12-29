class shopping:
    def __init__(self,inventory):
        self.product_cart={} # ********** change code here ************** 
        self.inventory=inventory


    def add_to_cart(self,product_id,buy_quantity,product_price):
        product=self.inventory.product_inventory[product_id]
        if product.stock>=buy_quantity:
            self.product_cart[product_id]=[product_id,buy_quantity,product_price] # ********** change code here ***********
            product.stock = product.stock - buy_quantity
            #return self.total_bill()
        else:
            print("currently stock unavailable")
        return self.total_bill() # calling total_bill method to calcuate total bill for the cart

    def total_bill(self):
        totalbill = 0 # total bill set to 0
        for cartitem in self.product_cart.values(): #fetching each item from the dictionary object (product_cart)
            itemprice = cartitem[1]*cartitem[2] # fetch and multiply buy_qty * prd_price
            totalbill = totalbill+itemprice # adding itemprice from previous line to total bill for each item
        return totalbill
            

import inventory
#instantiate inventory
if __name__ == '__main__':
    inventory = inventory.inventory()
    inventory.add_product(123,"watch", 100.0,10)
    inventory.add_product(112,"phone", 200.0,10)
    inventory.add_product(333,"fridge", 500.0,10)
    shopping = shopping(inventory)
    print(shopping.add_to_cart(123,1,100.0))
    print(shopping.add_to_cart(112,1,200.0))
    print(shopping.add_to_cart(333,1,500.0))

      

