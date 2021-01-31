from flask_restful import Resource, reqparse
from models.usuario import UserModel


class User(Resource):

    def get(self, user_id):
        user = UserlModel.find_user(user_id)
        if user:
            return user.json()
        return {'message':'User not found.'}, 404 # not found

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message':'An error ocurred trying to delete user'}, 500
            return {'message':'user deleted'}
        return{'message':'user not found'}, 404
