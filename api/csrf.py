from flask import Flask, request
app = Flask(__name__)

@app.route('/auth/', methods=['POST'])
def auth():
    if 'forgot_password' in request.args:
        return "CSRF атака: восстановление пароля выполнено!", 200
    elif 'login' in request.args:
        return "CSRF атака: вход выполнен!", 200
    elif 'register' in request.args:
        return "CSRF атака: регистрация выполнена!", 200
    return "Неизвестное действие.", 400
