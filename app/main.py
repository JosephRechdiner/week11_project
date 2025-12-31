from fastapi import FastAPI
from routes.contact_routes import contact_route

app = FastAPI()

app.include_router(contact_route)