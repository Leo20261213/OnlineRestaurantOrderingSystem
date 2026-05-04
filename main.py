from fastapi import FastAPI
from api.routers import index, auth, user, customer, menu_item, order

app = FastAPI(title="Online Restaurant Ordering System")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Online Restaurant Ordering System API"}


app.include_router(index.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(customer.router)
app.include_router(menu_item.router)
app.include_router(order.router)