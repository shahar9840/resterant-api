from db import db 

#מודל מנות מקושר לעגלה במערכת רבים לרבים ומקושר לקטגוריות ברבים ליחיד
class Dish(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text,nullable=False)
    imageUrl = db.Column(db.Text,default='')
    is_gluten_free = db.Column(db.Boolean,default=False)
    is_vegeterian = db.Column(db.Boolean,default=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    categories = db.relationship('Category',backref='dishes',cascade="save-update")

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "imageUrl":self.imageUrl,
            "is_gluten_free":self.is_gluten_free,
            "is_vegeterian":self.is_vegeterian,
            "category_id":self.category_id
            
        }




