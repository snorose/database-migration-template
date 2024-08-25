from sqlalchemy import insert
from sqlalchemy.orm import Session

from models.users import Users
from schemas.users import UserSchema

# 데이터의 양이 많기 때문에 한번에 넣는 데이터 양을 조절합니다.
# 이 값은 커스텀하게 지정할 수 있습니다
BATCH_SIZE = 100


class Service:
    def __init__(self, session: Session):
        self.session = session

    def insert_data(self, schemas: list[UserSchema]):
        count = 0

        while count <= len(schemas):
            print(f"Insert Data {count} ~ {count + BATCH_SIZE - 1}")
            try:
                insert_data = [schema.dict() for schema in schemas[count: count + BATCH_SIZE]]
                self.session.bulk_insert_mappings(Users, insert_data)       # 첫번째 인자는 생성한 model을 입력해주세요. 두번째 인자는 건드리지 않아도 됩니다

                self.session.flush()
            except Exception as e:
                print(f"!!!!!!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!!!!!!")
                print(f"{count} ~ {count + BATCH_SIZE - 1}에서 오류가 발생했습니다")
                print(e)

            count += BATCH_SIZE
