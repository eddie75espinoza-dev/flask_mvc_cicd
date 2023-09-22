from app.database import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all():
        return UserModel.query.all()

    # Otras consultas y lógica adicional para el modelo de usuario
