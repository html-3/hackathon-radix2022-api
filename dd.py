from app.extensions import db
from app.users.model import User
from app.bundles.model import Bundle
from app.oilrigs.model import OilRig
from app.items.model import Item
from app.ships.model import Ship
from datetime import datetime
import bcrypt
from random import randint

def create_dd(app):
    with app.app_context():
        db.create_all()
        db.session.commit()

        if not User.query.first():
            user = User(name="Pedro Rocha",
                email="pedro.rocha1980@gmail.com",
                pw_hash=bcrypt.hashpw("senha456".encode(), bcrypt.gensalt()))
            

            db.session.add(user)
            db.session.commit()

        if not OilRig.query.first():
            oilrig = [None] * 3
            for i in range(3):
                oilrig[i] = OilRig(name=f"OilRig {i+1}",
                    width=float(randint(1000, 1500)),
                    length=float(randint(1000, 1500)),
                    weight=float(randint(1000, 1500)))
                

                db.session.add(oilrig[i])
            db.session.commit()

        if not Ship.query.first():
            ship = [None] * 3
            for i in range(3):
                ship[i] = Ship(name=f"Ship {i+1}",
                    width=float(randint(10, 150)),
                    length=float(randint(10, 150)),
                    weight=float(randint(10, 150)))
                

                db.session.add(ship[i])
            db.session.commit()

        if not Bundle.query.first():
            bundle = [None] * 15
            for i in range(15):
                bundle[i] = Bundle(height=float(randint(10, 150)),
                    width=float(randint(10, 150)),
                    length=float(randint(10, 150)),
                    weight=float(randint(10, 150)),
                    oilrig=oilrig[15 % 3])
                

                db.session.add(bundle[i])
            db.session.commit()
        
        
        if not Item.query.first():
            for i in range(15):
                _ = Item(name=f"Item {i+1}",
                    height=float(randint(10, 150)),
                    width=float(randint(10, 150)),
                    length=float(randint(10, 150)),
                    weight=float(randint(10, 150)),
                    bundle=bundle[15 % 3],
                    oilrig=oilrig[15 % 3])
                

                db.session.add(_)
            db.session.commit()

        db.session.commit()
               