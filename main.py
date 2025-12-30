from fastapi import FastAPI
import inventory as I
import shopping as s

#uvicorn main:app --reload
#http://127.0.0.1:8000/docs
#instantiate fastapi class

app = FastAPI()
inventory = I.inventory()



@app.get("/")
def test_fastapi():
    return "hello from fastapi get method - successfully running"


@app.post("/add_product")
def add_product(prd_id: int, prd_name: str, prd_cost: float, prd_stkqty: int):
    try:
        added_product = inventory.add_product(prd_id, prd_name, prd_cost, prd_stkqty)
        return {
            "message": "Product added successfully",
            "product_id": added_product
        }   
    except Exception as e:
        return {"error": str(e)}


@app.post("/update_product")
def update_product(prd_id: int, prd_stkqty: int):
    try:
        inventory.update_product( prd_id, prd_stkqty )
        return {
            "message": "product updated successfully"
            
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/get_product")
def get_product(prd_id: int):
    try:
        product1 = inventory.get_product(prd_id)
        return {
            "message": "product is found",
            "product_id": product1.product_id,
            "product_name":product1.product_name
            #[prd.product_id,prd.product_name,prd.price,prd.stock]
        }
    except Exception as e:
        return {"error": str(e)}

    
shopping=s.shopping(inventory)
 
@app.post("/add_to_cart")
def add_to_cart(prd_id: int, prd_buyqty: int, prd_price:float):
    try:
        listvalues = shopping.add_to_cart(prd_id, prd_buyqty, prd_price)
        return {
        "message": "Product added to cart", 
        "product_name": listvalues[0],
        "product_buyqty": listvalues[1],
        "product_totalbill": listvalues[2]

        }
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/get_all_products")
def get_all_products():
    prodinv = inventory.get_allproducts()
    return{
            "product_inventory": prodinv
    }








'''
inventory = inventory.inventory()
inventory.add_product(123,"watch", 100.0,10)
inventory.add_product(112,"phone", 200.0,10)
inventory.add_product(333,"fridge", 500.0,10)
shopping = shopping.shopping(inventory)
print(shopping.add_to_cart(123,1,100.0))
print(shopping.add_to_cart(112,1,200.0))
print(shopping.add_to_cart(333,1,500.0))
'''

      

