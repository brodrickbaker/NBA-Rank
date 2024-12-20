from .db import db, environment, SCHEMA, add_prefix_for_prod

class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    player_id = db.Column(db.String(40), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False, primary_key=True)

    # Relationships
    user = db.relationship("User", back_populates="likes")

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'user_id': self.user_id
        }
