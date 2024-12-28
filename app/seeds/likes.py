from app.models import db, Like, environment, SCHEMA
from sqlalchemy.sql import text


def seed_likes():
    like_1 = Like(
        user_id=1, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_2 = Like(
        user_id=2, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_3 = Like(
        user_id=3, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_4 = Like(
        user_id=4, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_5 = Like(
        user_id=5, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_6 = Like(
        user_id=6, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_7 = Like(
        user_id=4, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_8 = Like(
        user_id=5, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_9 = Like(
        user_id=6, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_11 = Like(
        user_id=1, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_12 = Like(
        user_id=2, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_13 = Like(
        user_id=3, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_14 = Like(
        user_id=4, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_15 = Like(
        user_id=5, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_16 = Like(
        user_id=6, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_17 = Like(
        user_id=1, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_18 = Like(
        user_id=2, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_19 = Like(
        user_id=3, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_21 = Like(
        user_id=1, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_22 = Like(
        user_id=2, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_23 = Like(
        user_id=3, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_24 = Like(
        user_id=4, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_25 = Like(
        user_id=5, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_26 = Like(
        user_id=6, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_27 = Like(
        user_id=4, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_28 = Like(
        user_id=5, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_29 = Like(
        user_id=6, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_31 = Like(
        user_id=1, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_32 = Like(
        user_id=2, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_33 = Like(
        user_id=3, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_34 = Like(
        user_id=4, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_35 = Like(
        user_id=5, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_36 = Like(
        user_id=6, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_37 = Like(
        user_id=4, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_38 = Like(
        user_id=5, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_39 = Like(
        user_id=6, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_40 = Like(
        user_id=2, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_41 = Like(
        user_id=3, player_id='5e86a9c3-b4d0-4fe1-a551-acd83e5d60eb')
    like_42 = Like(
        user_id=4, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3')
    like_43 = Like(
        user_id=5, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_44 = Like(
        user_id=6, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_45 = Like(
        user_id=2, player_id='254e42d7-df01-4c68-9264-bca06c83c2c1')
    like_46 = Like(
        user_id=3, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_47 = Like(
        user_id=4, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_48 = Like(
        user_id=5, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_49 = Like(
        user_id=6, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_50 = Like(
        user_id=2, player_id='5cc51c05-06f5-4ae4-89a4-1d329fbbcdfb')
    like_51 = Like(
        user_id=3, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_52 = Like(
        user_id=4, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_53 = Like(
        user_id=2, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3')
    like_54 = Like(
        user_id=3, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3')
    like_55 = Like(
        user_id=6, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')

    db.session.add(like_1)
    db.session.add(like_2)
    db.session.add(like_3)
    db.session.add(like_4)
    db.session.add(like_5)
    db.session.add(like_6)
    db.session.add(like_7)
    db.session.add(like_8)
    db.session.add(like_9)
    db.session.add(like_11)
    db.session.add(like_12)
    db.session.add(like_13)
    db.session.add(like_14)
    db.session.add(like_15)
    db.session.add(like_16)
    db.session.add(like_17)
    db.session.add(like_18)
    db.session.add(like_19)
    db.session.add(like_21)
    db.session.add(like_22)
    db.session.add(like_23)
    db.session.add(like_24)
    db.session.add(like_25)
    db.session.add(like_26)
    db.session.add(like_27)
    db.session.add(like_28)
    db.session.add(like_29)
    db.session.add(like_31)
    db.session.add(like_32)
    db.session.add(like_33)
    db.session.add(like_34)
    db.session.add(like_35)
    db.session.add(like_36)
    db.session.add(like_37)
    db.session.add(like_38)
    db.session.add(like_39)
    db.session.add(like_40)
    db.session.add(like_41)
    db.session.add(like_42)
    db.session.add(like_43)
    db.session.add(like_44)
    db.session.add(like_45)
    db.session.add(like_46)
    db.session.add(like_47)
    db.session.add(like_48)
    db.session.add(like_49)
    db.session.add(like_50)
    db.session.add(like_51)
    db.session.add(like_52)
    db.session.add(like_53)
    db.session.add(like_54)
    db.session.add(like_55)
    db.session.commit()

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM likes"))
        
    db.session.commit