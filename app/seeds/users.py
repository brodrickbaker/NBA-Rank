from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', about="I'm a passionate basketball fan who loves everything about the game. I enjoy analyzing player stats, debating the greatest of all time, and staying updated with the latest news.")
    marnie = User(
        username='Marnie', email='marnie@aa.io', password='password', about='about Marnie')
    bobbie = User(
        username='Bobbie', email='bobbie@aa.io', password='password', about='about Bobbie')
    user1 = User( 
        username='DunkMaster23', email='user1@example.com', password='password1', about='about User1' ) 
    user2 = User( 
        username='HoopsHero', email='user2@example.com', password='password2', about='about User2' ) 
    user3 = User( 
        username='SlamDunkKing', email='user3@example.com', password='password3', about='about User3' )
    user4 = User( 
        username='ThreePointPro', email='user4@example.com', password='password1') 
    user5 = User( 
        username='ReboundRuler', email='user5@example.com', password='password2' ) 
    user6 = User( 
        username='CourtWarrior', email='user6@example.com', password='password3' )
    user7 = User( 
        username='DribbleDynasty', email='user7@example.com', password='password1') 
    user8 = User( 
        username='AlleyOopAce', email='user8@example.com', password='password2' ) 
    user9 = User( 
        username='BuzzerBeaterBoss', email='user9@example.com', password='password3' )
    user11 = User( 
        username='HoopDreamer', email='user11@example.com', password='password1' ) 
    user12 = User( 
        username='ThreePointKing', email='user12@example.com', password='password2' ) 
    user13 = User( 
        username='SlamDunkMaster', email='user13@example.com', password='password3' )
    user14 = User( 
        username='BuzzerBeater', email='user14@example.com', password='password1') 
    user15 = User( 
        username='BasketballJunkie', email='user15@example.com', password='password2' ) 
    user16 = User( 
        username='NetNinja', email='user16@example.com', password='password3' )
    user17 = User( 
        username='DribbleDynamo', email='user17@example.com', password='password1') 
    user18 = User( 
        username='FreeThrowGuru', email='user18@example.com', password='password2' ) 
    user19 = User( 
        username='BBallBro', email='user19@example.com', password='password3' )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user11)
    db.session.add(user12)
    db.session.add(user13)
    db.session.add(user14)
    db.session.add(user15)
    db.session.add(user16)
    db.session.add(user17)
    db.session.add(user18)
    db.session.add(user19)
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
