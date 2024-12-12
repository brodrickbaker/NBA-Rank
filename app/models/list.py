from .db import db, environment, SCHEMA, add_prefix_for_prod

class List(db.Model):
    __tablename__ = 'lists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False, primary_key=True)
    player_1 = db.Column(db.Integer, nullable=True)
    player_2 = db.Column(db.Integer, nullable=True)
    player_3 = db.Column(db.Integer, nullable=True)
    player_4 = db.Column(db.Integer, nullable=True)
    player_5 = db.Column(db.Integer, nullable=True)


    # Relationships
    user = db.relationship("User", back_populates="list")

def to_dict(self):
        return {
            'user_id': self.user_id,
            'player_1': self.player_1,
            'player_2': self.player_2,
            'player_3': self.player_3,
            'player_4': self.player_4,
            'player_5': self.player_5
        }
