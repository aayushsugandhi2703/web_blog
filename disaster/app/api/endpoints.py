from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from app.models import UserData, PostData, Session

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Request parsers for POST and PUT requests
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help='Name is required')
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')

post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help='Title is required')
post_parser.add_argument('content', type=str, required=True, help='Content is required')
post_parser.add_argument('user_id', type=int, required=True, help='User ID is required')

class UserResource(Resource):
    def get(self, user_id):
        session = Session()
        user = session.query(UserData).get(user_id)
        session.close()
        if user:
            return {'id': user.id, 'name': user.name, 'username': user.username}, 200
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        args = user_parser.parse_args()
        session = Session()
        user = session.query(UserData).get(user_id)
        if user:
            user.name = args['name']
            user.username = args['username']
            user.password = args['password']
            session.commit()
            session.close()
            return {'message': 'User updated'}, 200
        session.close()
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        session = Session()
        user = session.query(UserData).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return {'message': 'User deleted'}, 200
        session.close()
        return {'message': 'User not found'}, 404

class UserListResource(Resource):
    def get(self):
        session = Session()
        users = session.query(UserData).all()
        session.close()
        return [{'id': user.id, 'name': user.name, 'username': user.username} for user in users], 200

    def post(self):
        args = user_parser.parse_args()
        session = Session()
        new_user = UserData(
            name=args['name'],
            username=args['username'],
            password=args['password']
        )
        session.add(new_user)
        session.commit()
        session.close()
        return {'message': 'User created'}, 201

class PostResource(Resource):
    def get(self, post_id):
        session = Session()
        post = session.query(PostData).get(post_id)
        session.close()
        if post:
            return {'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id}, 200
        return {'message': 'Post not found'}, 404

    def put(self, post_id):
        args = post_parser.parse_args()
        session = Session()
        post = session.query(PostData).get(post_id)
        if post:
            post.title = args['title']
            post.content = args['content']
            post.user_id = args['user_id']
            session.commit()
            session.close()
            return {'message': 'Post updated'}, 200
        session.close()
        return {'message': 'Post not found'}, 404

    def delete(self, post_id):
        session = Session()
        post = session.query(PostData).get(post_id)
        if post:
            session.delete(post)
            session.commit()
            session.close()
            return {'message': 'Post deleted'}, 200
        session.close()
        return {'message': 'Post not found'}, 404

class PostListResource(Resource):
    def get(self):
        session = Session()
        posts = session.query(PostData).all()
        session.close()
        return [{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id} for post in posts], 200

    def post(self):
        args = post_parser.parse_args()
        session = Session()
        new_post = PostData(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id']
        )
        session.add(new_post)
        session.commit()
        session.close()
        return {'message': 'Post created'}, 201

# Register resources with the API
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
