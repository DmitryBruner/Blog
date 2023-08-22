from config import db


class Post(db.Model):
    #  __tablename__ = 'post' #maybe wrong
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post{self.id}>'


class Users(db.Model):
    # __tablename__ = 'users' #maybe wrong
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(140), nullable=False)
    password = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return f'<Users{self.id}>'