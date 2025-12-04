from models import Game, Review, engine, Base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

g1 = Game(title="Halo", genre="FPS", platform="Xbox", price=60)
g2 = Game(title="Minecraft", genre="Sandbox", platform="PC", price=30)

r1 = Review(score=9, comment="Amazing!", game=g1)
r2 = Review(score=8, comment="Fun game!", game=g2)

session.add_all([g1, g2, r1, r2])
session.commit()

print("Seed 1 complete!")
