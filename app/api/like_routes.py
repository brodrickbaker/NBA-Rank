from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models.like import Like
from app.models import db

like_routes = Blueprint('likes', __name__)

#Get player likes by player id
@like_routes.route('/<playerId>')
def get_player_likes(playerId):
    try:
        likes = Like.query.filter_by(player_id=playerId).all()
        if likes:
            return([like.to_dict() for like in likes])
    except:
        return jsonify({"message": "Player has no likes"})

#Add a like to a player
@like_routes.route('/<playerId>', methods=['POST'])
@login_required
def add_like(playerId):
    try:
        like = Like(
        user_id=current_user.id,
        player_id=playerId
    )
        db.session.add(like)
        db.session.commit()
        return jsonify(like.to_dict())
    except:
        return jsonify({"errors": "Player already liked by user"})

# Delete a player from the current user's list
@like_routes.route('/<playerId>', methods=['DELETE'])
@login_required
def delete_player(playerId):
    like = Like.query.filter_by(user_id=current_user.id, player_id=playerId).first()
    if not like:
        return jsonify({"message": "Like not found"})
    elif like.user_id != current_user.id:
        return jsonify({"message":" Forbidden"}), 403
    db.session.delete(like)
    db.session.commit()
    return jsonify({'message': "Successfully Deleted"}), 200