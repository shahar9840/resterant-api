from db import db

#מודל קטגוריות מקושר למנות בקשר יחיד לרבים 
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    imageUrl = db.Column(db.Text)
    
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "imageUrl":self.imageUrl,
            "dishes":[dish.serialize() for dish in self.dishes]
        }
    
