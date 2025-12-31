from fastapi import APIRouter, Depends
from service.contact_service import ContactService
from database.connector import MongoDB
from schemas import ContactCreate, ContactUpdate
from bson import ObjectId

contact_route = APIRouter(prefix="/contacts")

@contact_route.get("/get_all_contacts")
def get_all_contacts(collection_name = Depends(MongoDB.get_collection_name()), db= Depends(MongoDB.get_db())):
    return ContactService.get_collection_service(collection_name, db)

@contact_route.post("/create_new_contact")
def create_new_contact(new_document = ContactCreate, collection_name = Depends(MongoDB.get_collection_name()), db= Depends(MongoDB.get_db())):
    return ContactService.insert_document_service(new_document.model_dump(), collection_name, db)

@contact_route.put("/update_existing_contact/{id}")
def update_existing_contact(id, new_document = ContactUpdate, collection_name = Depends(MongoDB.get_collection_name()), db= Depends(MongoDB.get_db())):
    return ContactService.update_document_service(ObjectId(id), new_document.model_dump(), collection_name, db)

@contact_route.delete("/delete_contact/{id}")
def delete_contact(id, collection_name = Depends(MongoDB.get_collection_name()), db= Depends(MongoDB.get_db())):
    return ContactService.delete_document_service(ObjectId(id), collection_name, db)

