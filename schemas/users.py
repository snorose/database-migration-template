from datetime import datetime, date

from pydantic import BaseModel, model_validator


"""
실제 db table과 일치하는 형태의 schema를 구성해주세요
아래는 예시입니다
"""

class UserSchema(BaseModel):
    created_at: datetime
    updated_at: datetime
    birthday: date
    email: str
    last_login_at: datetime | None
    login_id: str
    major: str
    nickname: str
    password: str
    student_card: str | None
    student_number: str | None
    user_name: str
    user_profile: str | None
    user_role_id: str
    deleted_at: datetime | None
    last_nickname_updated_at: datetime | None
    is_blacklist: bool
    point_balance: int

    # 이 함수는 그대로 복사해서 가져가주세요
    @model_validator(mode="before")
    def null_filter(cls, values: dict) -> dict:
        for key, value in values.items():
            if value == "":
                values[key] = None

        return values
