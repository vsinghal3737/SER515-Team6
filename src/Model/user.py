import SQLAlchemyCreateDB as sql


class User:
    @classmethod
    def find_by_username(cls, username):
        return sql.User.query.filter_by(Username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return sql.User.query.get(_id)

    @classmethod
    def NewPassword(cls, username, newPassword):
        sql.User.query.filter_by(Username=username).first().Password = newPassword
