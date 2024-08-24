from datetime import datetime, date

from sqlalchemy import Column
from sqlalchemy import String, BigInteger, Date, Boolean, DateTime

from database import Base

"""
실제 db table과 일치하는 형태의 model을 구성해주세요
아래는 예시입니다
"""


class Users(Base):
    __tablename__ = 'users'     # db table명

    id = Column(BigInteger, primary_key=True)    # id는 직접 작성하지 않는다면 생략
    created_at = Column(DateTime, nullable=False)   # nullable이 False인 경우 파라미터 전달
    updated_at = Column(DateTime)
    birthday = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    last_login_at = Column(DateTime)
    login_id = Column(String(50), nullable=False)
    major = Column(String(50), nullable=False)
    nickname = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)
    student_card = Column(String(2048))
    student_number = Column(String(10), nullable=False)
    user_name = Column(String(100), nullable=False)
    user_profile = Column(String(2048), nullable=False)
    user_role_id = Column(BigInteger, nullable=False)
    deleted_at = Column(DateTime)
    last_nickname_updated_at = Column(DateTime)
    is_blacklist = Column(Boolean, nullable=False)
    point_balance = Column(BigInteger, nullable=False)
