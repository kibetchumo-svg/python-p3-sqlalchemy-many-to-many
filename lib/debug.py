from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, User, Review

engine = create_engine('sqlite:///many_to_many.db')
Session = sessionmaker(bind=engine)
session = Session()

# First game and its users
game = session.query(Game).first()
print("Game:", game)
print("Users who reviewed this game:", game.users)

# First user and their games
user = session.query(User).first()
print("User:", user)
print("Games reviewed by this user:", user.games)

# First review and its game and user
review = session.query(Review).first()
print("Review:", review)
print("Game of review:", review.game)
print("User of review:", review.user)

session.close()
