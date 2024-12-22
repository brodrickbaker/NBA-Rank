from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_posts():
    post_1 = Post(
        user_id=1, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', title='Is he the GOAT?', body="I'm not saying he is or he isn't, Im just saying there's a case to be made.", username='Demo')
    post_2 = Post(
        user_id=1, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb', title="Hand's down my fave!", body="What is there to say? He's just so fun to watch!", username='Demo')
    post_3 = Post(
        user_id=1, player_id='8ec91366-faea-4196-bbfd-b8fab7434795', title='3-Point GOD!', body="I'm pretty sure it's safe to say that nobody will ever surpass this man as the 3-point king.", username='Demo')

    db.session.add(post_1)
    db.session.add(post_2)
    db.session.add(post_3)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
        
    db.session.commit()