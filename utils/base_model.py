from datetime import datetime
from app import db


class BaseModel:
    def create(self):        
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        self.update_at = datetime.now()
        db.session.commit()
    
    def delete_one(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def delete_many(cls, ids):
        delete_count = cls.query.filter(cls.union_id.in_(ids)).delete()
        db.session.commit()
        return delete_count
