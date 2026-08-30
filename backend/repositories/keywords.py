import uuid

from sqlalchemy.orm import Session

from models.keyword import Keyword


def get_keyword_by_name(db: Session, name: str):
    return (
        db.query(Keyword)
        .filter(Keyword.name == name)
        .first()
    )


def add_keyword(db: Session, name: str):
    keyword = Keyword(
        id=str(uuid.uuid4()),
        name=name
    )

    db.add(keyword)
    db.flush()

    return keyword