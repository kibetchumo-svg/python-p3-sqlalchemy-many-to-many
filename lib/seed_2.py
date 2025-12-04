from models import User, Review, Game, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

u1 = User(name="Alice")
u2 = User(name="Bob")

session.add_all([u1, u2])
session.commit()

# Give Alice a review on Minecraft
minecraft = session.query(Game).filter_by(title="Minecraft").first()
rev = Review(score=10, comment="My favorite", user=u1, game=minecraft)

session.add(rev)
session.commit()

print("Seed 2 complete!")
