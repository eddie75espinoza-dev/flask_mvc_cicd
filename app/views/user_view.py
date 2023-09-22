from flask import Blueprint, jsonify, make_response
from app.controller.user_controller import get_users

user_view = Blueprint('user_view', __name__)

@user_view.route('/users')
def get_users():
    # Lógica adicional para manipular los usuarios
    _, users = get_users()
    return make_response(jsonify(users), 200)

# Otras rutas y lógica adicional para la vista de usuarios
