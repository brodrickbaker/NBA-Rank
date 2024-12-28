from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', about="I'm a passionate basketball fan who loves everything about the game. I enjoy analyzing player stats, debating the greatest of all time, and staying updated with the latest news.")
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', about='about Marnie')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', about='about Bobbie')
    user1 = User( 
        username='User1', email='user1@example.com', password='password1', about='about User1' ) 
    user2 = User( 
        username='User2', email='user2@example.com', password='password2', about='about User2' ) 
    user3 = User( 
        username='User3', email='user3@example.com', password='password3', about='about User3' )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
