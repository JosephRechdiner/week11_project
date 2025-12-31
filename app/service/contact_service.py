from bson import ObjectId
from dal.contact_dal import ContactDal
from fastapi import HTTPException

class ContactService:
    @staticmethod
    def get_collection_service(collection_name: str, db):
        all_documents = ContactDal.get_collection_dal(collection_name, db)
        return all_documents


    @staticmethod
    def insert_document_service(new_document: dict, collection_name: str, db):
        try:
            new_document_id = ContactDal.insert_document_dal(new_document, collection_name, db)
            if new_document_id:
                return {"msg": "Contact added succesfully", "Id": "new_document_id"}
        except Exception as e:
            raise HTTPException(status_code=409, detail=str(e))


    @staticmethod
    def update_document_service(doc_id: ObjectId, new_document: dict, collection_name: str, db):
        try:
            dal_result = ContactDal.update_document_dal(doc_id, new_document, collection_name, db)
            if dal_result:
                return {"msg": "Contact updated succesfully"}
            raise HTTPException(status_code=404, detail="Not found")
        except Exception as e:
            raise HTTPException(status_code=409, detail=str(e))
            

    @staticmethod
    def delete_document_service(doc_id: ObjectId, collection_name: str, db):
        try:
            dal_result = ContactDal.delete_document_dal(doc_id, collection_name, db)
            if dal_result:
                return {"msg": "Contact deleted succesfully"}
            raise HTTPException(status_code=404, detail="Not found")
        except Exception as e:
            raise HTTPException(status_code=409, detail=str(e))