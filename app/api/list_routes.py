from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models.list import List
from app.models import db

list_routes = Blueprint('lists', __name__)

#Get current user's list
@list_routes.route('/current')
@login_required
def get_user_list():
    list = List.query.filter_by(user_id=current_user.id).first()
    if list:
        return jsonify(list.to_dict())
    return jsonify({"message": "List couldn't be found"}), 404

#Add a player to the current user's list
@list_routes.route('/current', methods=['PUT'])
@login_required
def add_player():
    data = request.get_json()
    player = data.get("player")
    list = List.query.filter_by(user_id=current_user.id).first()
    if list:
        if player == list.player_1 or player == list.player_2 or player == list.player_3 or player == list.player_4 or player == list.player_5:
            return jsonify({"message": "This player is already on your list"}), 400
        if not list.player_1:
            list.player_1 = player
        elif not list.player_2:
            list.player_2 = player
        elif not list.player_3:
            list.player_3 = player
        elif not list.player_4:
            list.player_4 = player
        elif not list.player_5:
            list.player_5 = player
        else:
            return jsonify({"message": "Can only have 5 players, must delete one first"}), 400
        db.session.add(list)
        db.session.commit()
        return jsonify(list.to_dict())
    return jsonify({"message": "List couldn't be found"}), 404

# Delete a player from the current user's list
@list_routes.route('/current/<playerId>', methods=['DELETE'])
@login_required
def delete_player(playerId):
    list = List.query.filter_by(user_id=current_user.id).first()
    if list:
        for player, id in list.to_dict().items():
            if id == playerId:
                if player == 'player_1':
                    list.player_1 = None
                if player == 'player_2':
                    list.player_2 = None
                if player == 'player_3':
                    list.player_3 = None
                if player == 'player_4':
                    list.player_4 = None
                if player == 'player_5':
                    list.player_5 = None
                db.session.add(list)
                db.session.commit()
                return jsonify(list.to_dict()), 200
    return jsonify({"message": "Player not found"}), 404