from sqlmodel import create_engine


SQLMODEL_DATABASE_URL = "sqlite:///chefster.db"

engine = create_engine(SQLMODEL_DATABASE_URL, echo=True,)
