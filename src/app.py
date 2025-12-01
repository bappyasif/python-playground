from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models import ProductCrude, Product, PatchProduct
from src.db import SessionLocal, engine
import src.db_models
from sqlalchemy.orm import Session
# from src.db_models import users
from src.schemas import UserCreate, UserLogin
# from passlib.context import CryptContext
from bcrypt import hashpw, gensalt, checkpw

server = FastAPI()

server.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
)

src.db_models.Base.metadata.create_all(bind=engine)

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

@server.get("/")
async def root():
    return {"message": "Hello World"}

products = [
    # ProductCrude(1, "budget gadget", "This is a budget gadget", 19.99, 10),
    Product(id=2, name="Wireles Mouse", description="This is a wireless mouse", price=9.99, quantity=10),
    Product(id=3, name="Wireles Keyboard", description="This is a wireless keyboard", price=9.99, quantity=10),
    Product(id=4, name="Wireles Headset", description="This is a wireless headset", price=9.99, quantity=10)
]

# getting database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def db_init():
    db = SessionLocal()

    count = db.query(src.db_models.Product).count()

    if count == 0:
        for product in products:
            # as we are making use of our existing pydantic product model for our local db we need to convert it to db model
            db.add(src.db_models.Product(**product.model_dump())) # this will convert product to dict and then add it to db
        db.commit()
        db.close()

db_init()

# @server.on_event("startup")
# async def startup_event():
#     db_init()

# @server.on_event("shutdown")
# async def shutdown_event():
#     db = SessionLocal()
#     db.close()

# @server.post("/register", response_model=UserCreate)
# @server.post("/register")
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

#     # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#     if query:
#         return {"message": "User already exists"}
#     else:
#         # hashed_password = pwd_context.hash(user.password)
#         hashed_password = pwd_context.hash(user.password[:20])    # this will hash only first 72 characters, unsafe but still getting password has more than 72 characters
#         # new_user = users(username=user.username, password=hashed_password)
#         new_user = src.db_models.User(username=user.username, password=hashed_password)
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return {"message": "User created", "user": new_user}

# this is functioning properly
# @server.post("/register")
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

#     if query:
#         return {"message": "User already exists"}
#     else:
#         salt = gensalt()
#         hashed_password = hashpw(user.password.encode('utf-8'), salt)

#         # transform bytes to string
#         hashed_password = hashed_password.decode('utf-8') # without this conversion it will throw error as bytes object is not verifyable against string

#         # when we dont have to manually include user schema based data into db
#         # new_user = src.db_models.User(**user.model_dump())
#         new_user = src.db_models.User(username=user.username, password=hashed_password)
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return {"message": "User created", "user": new_user, "hashed_password": hashed_password, "salt": salt}

@server.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        return {"message": "User already exists"}
    else:
        salt = gensalt()
        hashed_password = hashpw(user.password.encode('utf-8'), salt)

        # transform bytes to string
        hashed_password = hashed_password.decode('utf-8') # without this conversion it will throw error as bytes object is not verifyable against string

        new_user = src.db_models.User(username=user.username, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created", "user": new_user, "hashed_password": hashed_password, "salt": salt}
    
@server.post("/register-uwoh")
def register_user_without_hashing(user: UserCreate, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        return {"message": "User already exists"}
    else:
        new_user = src.db_models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created", "user": new_user}
    
@server.post("/login-uwoh")
async def user_login_witout_hashing(user: UserLogin, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        if query.password == user.password:
            return {"message": "Login successful"}
        else:
            return {"message": "Incorrect password"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
def verify_password(password: str, hashed_password: str) -> bool:
    return checkpw(password.encode(), hashed_password.encode())
    
@server.post("/login")
async def user_login(user: UserLogin, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        if verify_password(user.password, query.password):
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# @server.post("/register-user")
# async def user_registration(user: UserCreate, db: Session = Depends(get_db)):
#     query = users.select().where(users.c.username == user.username)
#     existing_user = db.execute(query).fetchone()

#     if existing_user:
#         raise HTTPException(status_code=400, detail="User already exists")
#     else:
#         hashed_password = pwd_context.hash(user.password)
#         new_user = users.insert().values(username=user.username, password=hashed_password)
#         await db.execute(new_user)
#         db.commit()
#         return {"message": "User created"}


# @server.post("/login")
# async def user_login(user: UserLogin, db: Session = Depends(get_db)):
#     query = users.select().where(users.c.username == user.username)
#     existing_user = db.execute(query).fetchone()

#     if existing_user:
#         if pwd_context.verify(user.password, existing_user.password):
#             return {"message": "Login successful"}
#         else:
#             raise HTTPException(status_code=401, detail="Invalid credentials")
#     else:
#         raise HTTPException(status_code=404, detail="User not found")

# @server.post("/login")
# def user_login(user: UserLogin, db: Session = Depends(get_db)):
#     query = src.db_models.User.select().where(src.db_models.User.username == user.username)
#     existing_user = db.execute(query).fetchone()

#     if existing_user:
#         if pwd_context.verify(user.password, existing_user.password):
#             return {"message": "Login successful"}
#         else:
#             raise HTTPException(status_code=401, detail="Invalid credentials")
#     else:
#         raise HTTPException(status_code=404, detail="User not found")

@server.get("/products")
def get_products():
    # db = SessionLocal(),
    # db.query()
    return {"message": "Products list", "products": products}

@server.get("/db-products")
def get_products_from_db(
    db: Session = Depends(get_db) # dependency injection
):
    # db = SessionLocal(), # we dont have to do this anymore as we are using dependency injection

    db_products = db.query(src.db_models.Product).all()
    
    return {"message": "Products list!!", "products": db_products}

@server.get("/db-products/{product_id}")
def get_product_from_db(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(src.db_models.Product).filter(src.db_models.Product.id == product_id).first()

    if db_product:
        return {"message": "DB_Product found", "product": db_product}
    else:
        return {"message": "Product not found"}

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

@server.post("/db-products")
def create_product_in_db(product: Product, db: Session = Depends(get_db)):
    db_products = db.query(src.db_models.Product).all()
    for p in db_products:
        if p.id == product.id:
            return {"message": "Product already exists"}
    
    db.add(src.db_models.Product(**product.model_dump()))
    db.commit()
    # db.close()

    return {"message": "Product created in db", "product": product}
 
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

@server.put("/db-products/{product_id}")
def update_db_product_as_its_entirity(product: Product, db: Session = Depends(get_db)):
    db_product = db.query(src.db_models.Product).filter(src.db_models.Product.id == product.id).first()

    if not db_product:
        return {"message": "Product not found"}
    
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    # db.close()

    return {"message": "Product updated in db", "product": product}

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

@server.delete("/db-products/{product_id}")
def delete_product_from_db(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(src.db_models.Product).filter(src.db_models.Product.id == product_id).first()

    if db_product:
        db.delete(db_product)
        db.commit()
        # db.close()
        return {"message": "Product deleted"}
    else:
        return {"message": "Product not found"}

# @server.delete("/products/{product_id}")
@server.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            del products[i]
            return {"message": "Product deleted"}
    return {"message": "Product not found"}