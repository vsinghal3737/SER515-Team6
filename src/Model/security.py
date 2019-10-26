from werkzeug.security import check_password_hash, generate_password_hash
from user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and check_password_hash(user.Password, password):
        return user


def identity(user_id):
    return User.find_by_id(user_id)


def FirstTime(username, password):
    newPassword = generate_password_hash(password, method='sha256')
    User.NewPassword(username, newPassword)
