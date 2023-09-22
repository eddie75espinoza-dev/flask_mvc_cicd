from flask import Blueprint
from app.models.user_model import UserModel

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def get_users():
    users = UserModel.get_all()
    # Lógica adicional para manipular los usuarios
    return {'users': users}, 200

# Otras rutas y lógica adicional para el controlador de usuarios
