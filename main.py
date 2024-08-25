from sqlalchemy.orm import Session

from database import SessionContext
from insert_data import Service
from parser import DataParser

if __name__ == '__main__':
    # 파일명을 수정해주세요
    schemas = DataParser().parser(filename="snorose_users.csv")

    with SessionContext() as session:
        service = Service(session)
        service.insert_data(schemas)
