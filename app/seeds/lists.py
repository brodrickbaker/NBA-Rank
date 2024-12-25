from app.models import db, List, environment, SCHEMA
from sqlalchemy.sql import text


def seed_lists():
    list_1 = List(
        user_id=1, player_1='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', player_2='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    list_2 = List(
        user_id=2, player_1='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', player_2='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    list_3 = List(
        user_id=3, player_1='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', player_2='53f2fa48-e61b-49fb-843d-8a3e872257eb')

    db.session.add(list_1)
    db.session.add(list_2)
    db.session.add(list_3)
    db.session.commit()

def undo_lists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.lists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM lists"))
        
    db.session.commit()