from datetime import datetime, timezone
from app.extensions import db
from sqlalchemy import exc


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc).replace(microsecond=0))
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc).replace(microsecond=0))

    def create(self, commit = True) -> object:
        db.session.add(self)
        if commit:
            try:
                db.session.commit()

            except exc.IntegrityError as err:
                db.session.rollback()

    def update(self, soft = False) -> None:
        if not soft:
            now = datetime.now(timezone.utc).replace(microsecond=0)
            self.updated_at  = now
            
        db.session.commit()

    def delete(self, commit = True) -> None:
        db.session.delete(self)
        if commit:
            db.session.commit()