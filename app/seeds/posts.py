from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


def seed_posts():
    post_1 = Post(
        user_id=2, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91', 
        title='Is he the GOAT?', 
        body="I'm not saying he is or he isn't, Im just saying there's a case to be made.", 
        username='Marnie',
        created_at=date.fromisoformat('2024-12-01'),
        updated_at=date.fromisoformat('2024-12-01'))
    post_2 = Post(
        user_id=3, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb', 
        title="Hand's down my fave!", 
        body="What is there to say? He's just so fun to watch!", 
        username='Bobbie',
        created_at=date.fromisoformat('2024-12-02'),
        updated_at=date.fromisoformat('2024-12-02'))
    post_3 = Post(
        user_id=4, player_id='8ec91366-faea-4196-bbfd-b8fab7434795', 
        title='3-Point GOD!', 
        body="I'm pretty sure it's safe to say that nobody will ever surpass this man as the 3-point king.", 
        username='DunkMaster23',
        created_at=date.fromisoformat('2024-12-03'),
        updated_at=date.fromisoformat('2024-12-03'))
    post_4 = Post(
        user_id=1, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91', 
        title="LeBron James' Incredible Longevity", 
        body="Just watched another stellar performance by LeBron James! At 39, he's still dominating the court like he's in his prime. His ability to adapt and evolve his game over the years is simply unmatched. Do you think we'll ever see another player with such incredible longevity and versatility? #KingJames #GOATdebate", 
        username='Demo',
        created_at=date.fromisoformat('2024-12-04'),
        updated_at=date.fromisoformat('2024-12-04'))
    post_5 = Post(
        user_id=1, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb', 
        title="Kevin Durant's Scoring Prowess", 
        body="KD is back and better than ever! His scoring efficiency and smooth style make him one of the most unguardable players in the league. The way he effortlessly scores from mid-range, beyond the arc, and in the paint is a thing of beauty. Where do you rank KD among the all-time greats? #KDTrey5 #SlimReaper", 
        username='Demo',
        created_at=date.fromisoformat('2024-12-05'),
        updated_at=date.fromisoformat('2024-12-05'))
    post_6 = Post(
        user_id=1, player_id='8ec91366-faea-4196-bbfd-b8fab7434795', 
        title='Stephen Curry: The Three-Point Maestro', 
        body="Stephen Curry is hands down the best shooter the NBA has ever seen. His ability to drain three-pointers from anywhere on the court is unreal! Watching him play is like watching a masterpiece in motion. How many more records do you think he'll break before he retires? #ChefCurry #SplashBrothers", 
        username='Demo',
        created_at=date.fromisoformat('2024-12-06'),
        updated_at=date.fromisoformat('2024-12-06'))
    post_7 = Post(
        user_id=1, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', 
        title="Luka Dončić: The Future of the NBA", 
        body="Luka Dončić is a phenom! At such a young age, he's already putting up historic numbers and making game-winning plays. His court vision and basketball IQ are off the charts. It's exciting to think about how much more he can accomplish. Is Luka the future face of the NBA? #LukaMagic #MFFL", 
        username='Demo',
        created_at=date.fromisoformat('2024-12-07'),
        updated_at=date.fromisoformat('2024-12-07'))
    post_8 = Post(
        user_id=1, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0', 
        title="Nikola Jokić: The Joker's Unstoppable Playmaking", 
        body="Nikola Jokić continues to amaze with his incredible playmaking skills. His vision and ability to make pinpoint passes from the center position are unparalleled. Watching him orchestrate the Denver Nuggets' offense is a treat for any basketball fan. Do you think Jokić is the best passing big man of all time?", 
        username='Demo',
        created_at=date.fromisoformat('2024-12-08'),
        updated_at=date.fromisoformat('2024-12-08')) 
    post_9 = Post(
        user_id=2, player_id='5cc51c05-06f5-4ae4-89a4-1d329fbbcdfb', 
        title='Zion Williamson: A Force of Nature', 
        body="When Zion Williamson is on the court, he's an unstoppable force of nature. His combination of power, speed, and agility is unmatched. Watching him throw down thunderous dunks and dominate the paint is exhilarating. What do you think are the keys to Zion staying healthy and reaching his full potential? #Zanos", 
        username='Marnie',
        created_at=date.fromisoformat('2024-12-09'),
        updated_at=date.fromisoformat('2024-12-09'))
    post_10 = Post(
        user_id=3, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6', 
        title="Devin Booker's Scoring Mastery", 
        body="Devin Booker's scoring ability is nothing short of spectacular. His smooth shooting stroke and clutch performances have made him one of the premier scorers in the NBA. That 70-point game is still fresh in my mind! How far do you think Booker can lead the Suns this season?", 
        username='Bobbie',
        created_at=date.fromisoformat('2024-12-10'),
        updated_at=date.fromisoformat('2024-12-10'))
    post_11 = Post(
        user_id=4, player_id='98136da3-452f-49dc-a794-1ee9c76443f2', 
        title="The Celtics' Rising Star", 
        body="Jayson Tatum continues to rise as one of the NBA's premier young talents. His smooth offensive game and ability to take over in clutch moments make him a true star. It's been incredible watching his growth each season. Can Tatum lead the Celtics to a championship in the near future?", 
        username='DunkMaster23',
        created_at=date.fromisoformat('2024-12-11'),
        updated_at=date.fromisoformat('2024-12-11'))
    post_12 = Post(
        user_id=4, player_id='98e2cdeb-69dc-499c-a853-84c32c714924', 
        title='Definitely the future GOAT!', 
        body="There's absolutely nothing youi can say to me to convince me that this man is not going to go down as the greatest player in NBA history when it's all said and done. He has all of the physical gifts and the drive to succeed. I just can't wait to see it happen.", 
        username='DunkMaster23',
        created_at=date.fromisoformat('2024-12-12'),
        updated_at=date.fromisoformat('2024-12-12'))
    post_13 = Post(
        user_id=1, player_id='98e2cdeb-69dc-499c-a853-84c32c714924', 
        title="The Next Big Thing", 
        body="Victor Wembanyama is the future of the NBA! Standing at 7'4\" with guard-like skills, he's a unicorn in the truest sense. His ability to shoot, dribble, and block shots makes him a nightmare for opponents. It's going to be exciting to see how he develops over the next few years. Is Wembanyama the most hyped prospect since LeBron?", 
        username='Demo',
        created_at=date.fromisoformat('2024-12-13'),
        updated_at=date.fromisoformat('2024-12-13'))
    post_14 = Post(
        user_id=2, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7', 
        title='Best European ever?', 
        body="There are some guys that might be able to make a claim for the title, but for me it's gotta be Luka ", 
        username='Marnie',
        created_at=date.fromisoformat('2024-12-14'),
        updated_at=date.fromisoformat('2024-12-14'))
    post_15 = Post(
        user_id=2, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3', 
        title='The new King of New York', 
        body="There's a new king in the Garden! Jalen Brunson has revitalized the Knicks, I can't believe the Mavs let him walk!! Big loss for them for sure!", 
        username='Marnie',
        created_at=date.fromisoformat('2024-12-15'),
        updated_at=date.fromisoformat('2024-12-15'))
    post_16 = Post(
        user_id=5, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1', 
        title='SGA All Day', 
        body="I never thought I would see a young OKC team like the KD, Westbrook and Harden team again but here we are! SGA is a young superstar and this team reminds me so much of that young team, hopefully they actually keep them together this time!", 
        username='HoopsHero',
        created_at=date.fromisoformat('2024-12-16'),
        updated_at=date.fromisoformat('2024-12-16'))
    post_17 = Post(
        user_id=6, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3', 
        title="My DPOY", 
        body="He's been robbed so many times! He definitely should have at least one DPOY, maybe two. I know people say he's always injured but he's only missed big time in a couple of seasons, he deserves one at some point.", 
        username='SlamDunkKing',
        created_at=date.fromisoformat('2024-12-17'),
        updated_at=date.fromisoformat('2024-12-17'))
    post_18 = Post(
        user_id=3, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1', 
        title="Did you know he's Canadian?", 
        body="I had no idea until I saw him playing for the Canadian Olympic team, seems like all the best players are from other countries these days.", 
        username='Bobbie',
        created_at=date.fromisoformat('2024-12-18'),
        updated_at=date.fromisoformat('2024-12-18'))
    post_19 = Post(
        user_id=5, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905', 
        title='The Greek Freak', 
        body="This man has all the tools and the drive to be great, I think him and Jokic are neck and neck for best players in the game today.", 
        username='HoopsHero',
        created_at=date.fromisoformat('2024-12-19'),
        updated_at=date.fromisoformat('2024-12-19'))
    post_20 = Post(
        user_id=6, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0', 
        title="The GOAT you never saw coming", 
        body="Nobody thought when he was drafted during a commercial break in the second round that this just might be the best player to ever lace them up. It's hard to believe sometimes even when you're watching. He just doesn't look the part, but he definitely has the skills.", 
        username='SlamDunkKing',
        created_at=date.fromisoformat('2024-12-20'),
        updated_at=date.fromisoformat('2024-12-20'))
    post_21 = Post(
        user_id=7, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d', 
        title='Klay Thompson: New Beginnings in Dallas', 
        body="Klay Thompson, widely known as a sharpshooting Warrior, joined the Dallas Mavericks for the 2024-25 season. Thompson, donning No. 31, has already made an impact by scoring 20+ points in several games, showing glimpses of his old form. Despite past injuries, he's proving to be a valuable asset to the team.", 
        username='ThreePointPro',
        created_at=date.fromisoformat('2024-12-21'),
        updated_at=date.fromisoformat('2024-12-21'))
    post_22 = Post(
        user_id=8, player_id='5e86a9c3-b4d0-4fe1-a551-acd83e5d60eb', 
        title="DeMar DeRozan Appreciation", 
        body="DeRozan's game is a beautiful blend of old-school mid-range mastery and modern versatility. Fans have witnessed countless clutch moments, including his historic back-to-back buzzer-beaters that wowed everyone", 
        username='ReboundRuler',
        created_at=date.fromisoformat('2024-12-22'),
        updated_at=date.fromisoformat('2024-12-22'))
    post_23 = Post(
        user_id=9, player_id='8ec91366-faea-4196-bbfd-b8fab7434795', 
        title='The Undisputed MVP of Our Hearts 💛🏀', 
        body="It's impossible to talk about basketball greatness without mentioning Stephen Curry. From his early days making Davidson college history, to revolutionizing the NBA with his shooting prowess, Steph has continuously left fans in absolute awe.", 
        username='CourtWarrior',
        created_at=date.fromisoformat('2024-12-23'),
        updated_at=date.fromisoformat('2024-12-23'))
    post_24 = Post(
        user_id=10, player_id='cfc1e41b-74ab-45ee-8132-aaf9ca7f8163', 
        title="The Speedster on the Rise", 
        body="Just wanted to shout out De'Aaron Fox for being an absolute ⭐ on the court! His blazing speed, slick moves, and clutch performances are pure 🔥. With every game, he shows why he's the heart and soul of the Kings.", 
        username='DribbleDynasty',
        created_at=date.fromisoformat('2024-12-24'),
        updated_at=date.fromisoformat('2024-12-24'))
    post_25 = Post(
        user_id=11, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9', 
        title="Tyrese Maxey: Our Rising Star", 
        body="Can we just take a moment to appreciate Tyrese Maxey? This guy has been an absolute joy to watch! From his explosive drives to the basket to his smooth shooting stroke, Maxey brings energy and excitement every time he steps on the court.", 
        username='AlleyOopAce',
        created_at=date.fromisoformat('2024-12-25'),
        updated_at=date.fromisoformat('2024-12-25'))
    post_26 = Post(
        user_id=12, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905', 
        title='Giannis Antetokounmpo: The Court Conqueror', 
        body="Giannis is simply phenomenal! His impressive dunks, defensive prowess, and unstoppable drives make every Bucks game a thrill to watch. The Greek Freak continues to redefine what's possible on the court. Keep soaring, Giannis!", 
        username='BuzzerBeaterBoss',
        created_at=date.fromisoformat('2024-12-26'),
        updated_at=date.fromisoformat('2024-12-26'))
    post_27 = Post(
        user_id=13, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd', 
        title="The Clutch King", 
        body="Damian Lillard is simply phenomenal! His deep three-pointers, clutch performances, and fearless leadership make every Blazers game a nail-biter. Dame continues to redefine what's possible in crunch time. Keep shining, Lillard!", 
        username='HoopDreamer',
        created_at=date.fromisoformat('2024-12-27'),
        updated_at=date.fromisoformat('2024-12-27'))
    post_28 = Post(
        user_id=14, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc', 
        title="The Beard is Fearsome", 
        body="James Harden is an offensive juggernaut! His step-back threes, crafty assists, and impressive scoring abilities make every game electrifying. The Beard continues to be a game-changer every time he hits the court.", 
        username='ThreePointKing',
        created_at=date.fromisoformat('2024-12-28'),
        updated_at=date.fromisoformat('2024-12-28')) 
    post_29 = Post(
        user_id=15, player_id='c12fb587-fc86-471c-8a84-19caf31325ce', 
        title='Kawhi Leonard: The Silent Assassin', 
        body="Kawhi Leonard is the epitome of cool under pressure! His clutch scoring, lockdown defense, and incredible versatility make him a true basketball maestro. The Silent Assassin continues to leave his mark, game after game.", 
        username='SlamDunkMaster',
        created_at=date.fromisoformat('2024-12-29'),
        updated_at=date.fromisoformat('2024-12-29'))
    post_30 = Post(
        user_id=16, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6', 
        title="The Future of the Thunder", 
        body="Chet Holmgren is an emerging force for the Oklahoma City Thunder. His shot-blocking ability, smooth shooting, and impressive rebounding skills make him a standout player2. Even through injuries, Holmgren's dedication and potential have fans excited for what's to come. Get well soon, Chet!", 
        username='BuzzerBeater',
        created_at=date.fromisoformat('2024-12-30'),
        updated_at=date.fromisoformat('2024-12-30'))
    post_31 = Post(
        user_id=17, player_id='254e42d7-df01-4c68-9264-bca06c83c2c1', 
        title="The Precision Playmaker", 
        body="Tyrese Haliburton is lighting up the court for the Indiana Pacers! His impressive vision, silky smooth passes, and clutch shooting make him a delight to watch. Whether he's orchestrating the offense or pulling up for a shot, Haliburton's skill and poise are undeniable.", 
        username='BasketballJunkie',
        created_at=date.fromisoformat('2024-12-31'),
        updated_at=date.fromisoformat('2024-12-31'))
    post_32 = Post(
        user_id=18, player_id='20f85838-0bd5-4c1f-ab85-a308bafaf5bc', 
        title="Aaron Gordon: The High-Flyer", 
        body="Aaron Gordon is electrifying the court with his jaw-dropping dunks, athleticism, and versatile game. Whether he's throwing down spectacular slams or playing lockdown defense, Gordon's energy and passion make him a fan favorite.", 
        username='NetNinja',
        created_at=date.fromisoformat('2025-01-01'),
        updated_at=date.fromisoformat('2025-01-01')) 
    post_33 = Post(
        user_id=19, player_id='9983bed6-e53c-4c65-a90a-51546a0e3352', 
        title='The Dynamic Dynamo', 
        body="Ja Morant's lightning speed, incredible athleticism, and fearless drives to the basket make every Memphis Grizzlies game a must-watch. His explosive plays and clutch performances electrify the crowd and keep us on the edge of our seats. Keep flying high, Ja!", 
        username='DribbleDynamo',
        created_at=date.fromisoformat('2025-01-02'),
        updated_at=date.fromisoformat('2025-01-02'))
    post_34 = Post(
        user_id=20, player_id='ffc5579c-783f-4d62-80ab-3c3dcb05a27d', 
        title="The Dunking Dynamo", 
        body="Jaylen Brown brings relentless energy and skill to the Boston Celtics! His high-flying dunks, clutch shooting, and tenacious defense make every game a spectacle. Jaylen's growth and determination continue to electrify fans.", 
        username='FreeThrowGuru',
        created_at=date.fromisoformat('2025-01-03'),
        updated_at=date.fromisoformat('2025-01-03'))
    post_35 = Post(
        user_id=21, player_id='942c53e3-7268-44e3-b0a9-fdff55a72c03', 
        title="Chris Paul: The Point God", 
        body="Chris Paul is a living legend! His court vision, clutch plays, and veteran leadership make him one of the greatest point guards in NBA history. Whether he's dishing out assists or knocking down crucial shots, CP3's impact is undeniable.", 
        username='BBallBro',
        created_at=date.fromisoformat('2025-01-04'),
        updated_at=date.fromisoformat('2025-01-04'))

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
    db.session.add(post_21)
    db.session.add(post_22)
    db.session.add(post_23)
    db.session.add(post_24)
    db.session.add(post_25)
    db.session.add(post_26)
    db.session.add(post_27)
    db.session.add(post_28)
    db.session.add(post_29)
    db.session.add(post_30)
    db.session.add(post_31)
    db.session.add(post_32)
    db.session.add(post_33)
    db.session.add(post_34)
    db.session.add(post_35)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
        
    db.session.commit()