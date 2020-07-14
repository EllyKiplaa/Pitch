from . import db
class Categories:
    '''
    # Category class to define category Objects
    # '''
    # def ___init__(self,id,name,description):
    #     self.id = id
    #     self.name = name
    #     self.description= description

    # def save_category(self):
    #     '''
    #     Function that saves a category
    #     '''
       
    # def get_categories(cls):

    #     Category.all_categories.append()
    #     return categories

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'