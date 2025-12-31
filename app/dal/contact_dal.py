from bson import ObjectId
class ContactDal:
    @staticmethod
    def get_collection_dal(collection_name: str, db):
        all_documents = []
        for document in db[collection_name].find():
            all_documents.append(document)
        return all_documents

    @staticmethod
    def insert_document_dal(new_document: dict, collection_name: str, db):
        try:
            db_result = db[collection_name].insert_one(new_document)
            if db_result:
                return db_result.inserted_id
            return False
        except Exception as e:
            raise e

    @staticmethod
    def update_document_dal(doc_id: ObjectId, new_document: dict, collection_name: str, db):
        try:
            contact_to_update = db[collection_name].find_one({"_id": doc_id})
            if contact_to_update:
                for key, val in new_document.items():
                    db[collection_name].update_one({"_id": doc_id}, {"$set": {key: val}})
                    return True
            return False
        except Exception as e:
            raise e
            
    @staticmethod
    def delete_document_dal(doc_id: ObjectId, collection_name: str, db):
        try:
            contact_to_delete = db[collection_name].find_one({"_id": doc_id})
            if contact_to_delete:
                db[collection_name].delete_one({"_id": doc_id})
                return True
            return False
        except Exception as e:
            raise e