from app.models import db, Like, environment, SCHEMA
from sqlalchemy.sql import text


def seed_likes():
    like_1 = Like(
        user_id=1, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_2 = Like(
        user_id=2, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_3 = Like(
        user_id=3, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')

    db.session.add(like_1)
    db.session.add(like_2)
    db.session.add(like_3)
    db.session.commit()

def undo_lists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.lists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM lists"))
        
    db.session.commit