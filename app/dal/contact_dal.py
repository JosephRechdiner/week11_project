from bson import ObjectId

class ContactDal:
    @classmethod
    def get_collection(collection_name: str, db):
        all_documents = []
        for document in db[collection_name].find():
            all_documents.append(document)
        return all_documents

    @classmethod
    def insert_document(new_document: dict, collection_name: str, db):
        try:
            db_result = db[collection_name].insert_one(new_document)
            if db_result:
                return db_result.inserted_id
            return False
        except Exception as e:
            raise e

    @classmethod
    def update_document(doc_id: ObjectId, new_document: dict, collection_name: str, db):
        try:
            contact_to_update = db[collection_name].find_one({"_id": doc_id})
            if contact_to_update:
                for key, val in new_document.items():
                    db[collection_name].update_one({"_id": doc_id}, {"$set": {key: val}})
                    return True
            return False
        except Exception as e:
            raise e
            
    @classmethod
    def delete_document(doc_id: ObjectId, collection_name: str, db):
        try:
            contact_to_delete = db[collection_name].find_one({"_id": doc_id})
            if contact_to_delete:
                db[collection_name].delete_one({"_id": doc_id})
                return True
            return False
        except Exception as e:
            raise e