from sqlalchemy.orm import Session

from repositories.keywords import (
    get_keyword_by_name,
    add_keyword
)


def get_or_create_keyword(db: Session, name: str):

    keyword = get_keyword_by_name(db, name)

    if keyword:
        return keyword

    return add_keyword(db, name)