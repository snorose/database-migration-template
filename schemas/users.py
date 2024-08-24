from datetime import datetime, date

from pydantic import BaseModel, model_validator


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

    @model_validator(mode="before")
    def null_filter(cls, values: dict) -> dict:
        for key, value in values.items():
            if value == "":
                values[key] = None

        return values
