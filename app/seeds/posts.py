from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text


def seed_posts():
    post_1 = Post(
        user_id=2, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91', 
        title='Is he the GOAT?', 
        body="I'm not saying he is or he isn't, Im just saying there's a case to be made.", 
        username='Marnie')
    post_2 = Post(
        user_id=3, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb', 
        title="Hand's down my fave!", 
        body="What is there to say? He's just so fun to watch!", 
        username='Bobbie')
    post_3 = Post(
        user_id=4, player_id='8ec91366-faea-4196-bbfd-b8fab7434795', 
        title='3-Point GOD!', 
        body="I'm pretty sure it's safe to say that nobody will ever surpass this man as the 3-point king.", 
        username='Danny')
    post_4 = Post(
        user_id=1, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91', 
        title="LeBron James' Incredible Longevity", 
        body="Just watched another stellar performance by LeBron James! At 36, he's still dominating the court like he's in his prime. His ability to adapt and evolve his game over the years is simply unmatched. Do you think we'll ever see another player with such incredible longevity and versatility? #KingJames #GOATdebate", 
        username='Demo')
    post_5 = Post(
        user_id=1, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb', 
        title="Kevin Durant's Scoring Prowess", 
        body="KD is back and better than ever! His scoring efficiency and smooth style make him one of the most unguardable players in the league. The way he effortlessly scores from mid-range, beyond the arc, and in the paint is a thing of beauty. Where do you rank KD among the all-time greats? #KDTrey5 #SlimReaper", 
        username='Demo')
    post_6 = Post(
        user_id=1, player_id='8ec91366-faea-4196-bbfd-b8fab7434795', 
        title='Stephen Curry: The Three-Point Maestro', 
        body="Stephen Curry is hands down the best shooter the NBA has ever seen. His ability to drain three-pointers from anywhere on the court is unreal! Watching him play is like watching a masterpiece in motion. How many more records do you think he'll break before he retires? #ChefCurry #SplashBrothers", 
        username='Demo')
    post_7 = Post(
        user_id=1, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', 
        title="Luka Dončić: The Future of the NBA", 
        body="Luka Dončić is a phenom! At such a young age, he's already putting up historic numbers and making game-winning plays. His court vision and basketball IQ are off the charts. It's exciting to think about how much more he can accomplish. Is Luka the future face of the NBA? #LukaMagic #MFFL", 
        username='Demo')
    post_8 = Post(
        user_id=1, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0', 
        title="Nikola Jokić: The Joker's Unstoppable Playmaking", 
        body="Nikola Jokić continues to amaze with his incredible playmaking skills. His vision and ability to make pinpoint passes from the center position are unparalleled. Watching him orchestrate the Denver Nuggets' offense is a treat for any basketball fan. Do you think Jokić is the best passing big man of all time?", 
        username='Demo') 
    post_9 = Post(
        user_id=2, player_id='5cc51c05-06f5-4ae4-89a4-1d329fbbcdfb', 
        title='Zion Williamson: A Force of Nature', 
        body="When Zion Williamson is on the court, he's an unstoppable force of nature. His combination of power, speed, and agility is unmatched. Watching him throw down thunderous dunks and dominate the paint is exhilarating. What do you think are the keys to Zion staying healthy and reaching his full potential? #Zanos", 
        username='Marnie')
    post_10 = Post(
        user_id=3, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6', 
        title="Devin Booker's Scoring Mastery", 
        body="Devin Booker's scoring ability is nothing short of spectacular. His smooth shooting stroke and clutch performances have made him one of the premier scorers in the NBA. That 70-point game is still fresh in my mind! How far do you think Booker can lead the Suns this season?", 
        username='Bobbie')
    post_11 = Post(
        user_id=4, player_id='98136da3-452f-49dc-a794-1ee9c76443f2', 
        title="The Celtics' Rising Star", 
        body="Jayson Tatum continues to rise as one of the NBA's premier young talents. His smooth offensive game and ability to take over in clutch moments make him a true star. It's been incredible watching his growth each season. Can Tatum lead the Celtics to a championship in the near future?", 
        username='Danny')
    post_12 = Post(
        user_id=4, player_id='98e2cdeb-69dc-499c-a853-84c32c714924', 
        title='Definitely the future GOAT!', 
        body="There's absolutely nothing youi can say to me to convince me that this man is not going to go down as the greatest player in NBA history when it's all said and done. He has all of the physical gifts and the drive to succeed. I just can't wait to see it happen.", 
        username='Danny')
    post_13 = Post(
        user_id=1, player_id='98e2cdeb-69dc-499c-a853-84c32c714924', 
        title="The Next Big Thing", 
        body="Victor Wembanyama is the future of the NBA! Standing at 7'4\" with guard-like skills, he's a unicorn in the truest sense. His ability to shoot, dribble, and block shots makes him a nightmare for opponents. It's going to be exciting to see how he develops over the next few years. Is Wembanyama the most hyped prospect since LeBron?", 
        username='Demo')
    post_14 = Post(
        user_id=2, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', 
        title='Best European ever?', 
        body="There are some guys that might be able to make a claim for the title, but for me it's gotta be Luka ", 
        username='Marnie')
    post_15 = Post(
        user_id=2, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3', 
        title='The new King of New York', 
        body="There's a new king in the Garden! Jalen Brunson has revitalized the Knicks, I can't believe the Mavs let him walk!! Big loss for them for sure!", 
        username='Marnie')
    post_16 = Post(
        user_id=5, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1', 
        title='SGA All Day', 
        body="I never thought I would see a young OKC team like the KD, Westbrook and Harden team again but here we are! SGA is a young superstar and this team reminds me so much of that young team, hopefully they actually keep them together this time!", 
        username='Brandon')
    post_17 = Post(
        user_id=6, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3', 
        title="My DPOY", 
        body="He's been robbed so many times! He definitely should have at least one DPOY, maybe two. I know people say he's always injured but he's only missed big time in a couple of seasons, he deserves one at some point.", 
        username='Ashley')
    post_18 = Post(
        user_id=3, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1', 
        title="Did you know he's Canadian?", 
        body="I had no idea until I saw him playing for the Canadian Olympic team, seems like all the best players are from other countries these days.", 
        username='Bobbie')
    post_19 = Post(
        user_id=5, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905', 
        title='The Greek Freak', 
        body="This man has all the tools and the drive to be great, I think him and Jokic are neck and neck for best players in the game today.", 
        username='Brandon')
    post_20 = Post(
        user_id=6, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0', 
        title="The GOAT you never saw coming", 
        body="Nobody thought when he was drafted during a commercial break in the second round that this just might be the best player to ever lace them up. It's hard to believe sometimes even when you're watching. He just doesn't look the part, but he definitely has the skills.", 
        username='Ashley')

    db.session.add(post_1)
    db.session.add(post_2)
    db.session.add(post_3)
    db.session.add(post_4)
    db.session.add(post_5)
    db.session.add(post_6)
    db.session.add(post_7)
    db.session.add(post_8)
    db.session.add(post_9)
    db.session.add(post_10)
    db.session.add(post_11)
    db.session.add(post_12)
    db.session.add(post_13)
    db.session.add(post_14)
    db.session.add(post_15)
    db.session.add(post_16)
    db.session.add(post_17)
    db.session.add(post_18)
    db.session.add(post_19)
    db.session.add(post_20)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
        
    db.session.commit()