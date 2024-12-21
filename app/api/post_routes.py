from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models.post import Post
from app.models import db
from datetime import datetime

post_routes = Blueprint('posts', __name__)

#Get posts for current user
@post_routes.route('/current')
@login_required
def get_user_posts():
    posts = Post.query.filter_by(user_id=current_user.id).all()
    if posts:
        return([post.to_dict() for post in posts])
    return jsonify({"errors": "user has no posts"})

#Get posts for specified player
@post_routes.route('/<playerId>')
def get_player_posts(playerId):
    posts = Post.query.filter_by(player_id=playerId).all()
    if posts:
        return([post.to_dict() for post in posts])
    return jsonify({"errors": "Player posts couldn't be found"})

#Create a new post
@post_routes.route('/<playerId>', methods=['POST'])
@login_required
def create_post(playerId):
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    if title and body:
        post = Post(title=title, body=body, user_id=current_user.id, player_id=playerId)
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict()), 201
    elif body and not title:
        return jsonify({"message": "Bad Request", "errors": {"title": "Title is required"}}), 400
    elif title and not body:
        return jsonify({"message": "Bad Request", "errors": {"body": "Body is required"}}), 400
    return jsonify({"message": "Bad Request", "errors": {"title": "Title is required", "body": "Body is required"}}), 400
    
#update a post
@post_routes.route('/<int:postId>', methods=['PUT'])
@login_required
def update_post(postId):
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    post = Post.query.filter_by(id=postId).first()
    if title and body:
        post.title=title
        post.body=body
        post.updated_at=datetime.now()
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict()), 201
    elif body and not title:
        return jsonify({"message": "Bad Request", "errors": {"title": "Title is required"}}), 400
    elif title and not body:
        return jsonify({"message": "Bad Request", "errors": {"body": "Body is required"}}), 400
    return jsonify({"message": "Bad Request", "errors": {"title": "Title is required", "body": "Body is required"}}), 400

# Delete Post
@post_routes.route('/<int:postId>', methods=['DELETE'])
@login_required
def delete_post(postId):
    post = Post.query.filter_by(id=postId).first()
    if not post:
        return jsonify({"message": "Post not found"}), 404
    elif post.user_id != current_user.id:
        return jsonify({"message":" Forbidden"}), 403
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': "Successfully Deleted"}), 200