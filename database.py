from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# 연결할 db url
DB_ID = ""
DB_PASSWORD = ""
SQLALCHEMY_DATABASE_URL = f"mysql://{DB_ID}:{DB_PASSWORD}@localhost:3306/snorose"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class SessionContext:
    session = None

    def __enter__(self):
        self.session = Session(engine)
        return self.session

    def __exit__(self, *args):
        self.session.commit()
        self.session.close()
