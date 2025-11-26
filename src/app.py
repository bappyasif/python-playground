from fastapi import FastAPI
from src.models import ProductCrude, Product, PatchProduct

server = FastAPI()

@server.get("/")
async def root():
    return {"message": "Hello World"}

products = [
    ProductCrude(1, "budget gadget", "This is a budget gadget", 19.99, 10),
    Product(id=2, name="Wireles Mouse", description="This is a wireless mouse", price=9.99, quantity=10),
    Product(id=3, name="Wireles Keyboard", description="This is a wireless keyboard", price=9.99, quantity=10),
    Product(id=4, name="Wireles Headset", description="This is a wireless headset", price=9.99, quantity=10)
]

@server.get("/products")
def get_products():
    return {"message": "Products list", "products": products}

@server.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return {"message": "Product found", "product": product}
    return {"message": "Product not found"}

# this method doesnt nsure product id is unique or not
# @server.post("/products")
# def create_product(product: Product):
#     products.append(product)
#     return {"message": "Product created", "product": product}
 
@server.post("/products")
def create_product(product: Product):
    for p in products:
        if p.id == product.id:
            return {"message": "Product already exists"}
        # these are now all done in pydantic model
        # if p.price <= 0:
        #     return {"message": "Price must be greater than 0"}
        # if p.quantity <= 0:
        #     return {"message": "Quantity must be greater than 0"}
        # if len(p.description) < 4:
        #     return {"message": "Description must be at least 4 characters long"}
    
    products.append(product)
    return {"message": "Product created", "product": product}

@server.put("/products/{product_id}")
def update_product_as_entirity(product: Product):
    for i in range(len(products)):
        if products[i].id == product.id:
            products[i] = product
            return {"message": "Product updated", "product": product}
    return {"message": "Product not found"}

@server.patch("/products/{product_id}")
def update_product_as_partial(product_update: PatchProduct):
    # for i, p in enumerate(products):
        # if p.id == product_update.id:
        #     if product_update.name:
        #         products[i].name = product_update.name
        #     if product_update.description:
        #         products[i].description = product_update.description
        #     if product_update.price:
        #         products[i].price = product_update.price
        #     if product_update.quantity:
        #         products[i].quantity = product_update.quantity
        #     return {"message": "Product updated", "product": products[i]}

    # for i, p in enumerate(products):
    #     if p.id == product_update.id:
    #         p_data = {k: v for k, v in product_update.__dict__.items() if v is not None}
    #         for key, value in p_data.items():
    #             setattr(p, key, value)
    #         return {"message": "Product updated", "product": p}
        
    for i, p in enumerate(products):
        if p.id == product_update.id:
            for key, value in product_update.__dict__.items():
                if value is not None:
                    setattr(p, key, value)
            return {"message": "Product updated", "product": p}
        
    return {"message": "Product not found"}

# @server.delete("/products/{product_id}")
@server.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            del products[i]
            return {"message": "Product deleted"}
    return {"message": "Product not found"}