import os
import csv

from schemas.users import UserSchema

"""
csv 파일을 불러와 스키마로 파싱하는 클래스
"""


class DataParser:
    # 파일이 있는 주소를 여기에 입력해주세요
    filepath = f"{os.getcwd()}/csv_files"

    def import_csv(self, filename: str) -> list[list]:
        f = open(f"{self.filepath}/{filename}", 'r')
        reader = csv.reader(f)

        origin_data = []
        for line in reader:
            origin_data.append(line)

        return origin_data

    def parser(self, filename: str) -> list:
        # 1. csv 불러오기
        origin_data = self.import_csv(filename)

        # 2. 데이터 파싱
        parsed_data = []
        for data in origin_data:
            #---------- 이 지점에 각 데이터를 파싱하는 로직이 들어갑니다
            # example
            new_nickname = f"test - {data[7]}"

            # 스키마에 각 데이터를 넣어줍니다
            model = UserSchema(
                created_at=data[0],
                updated_at=data[1],
                birthday=data[2],
                email=data[3],
                last_login_at=data[4],
                login_id=data[5],
                major=data[6],
                nickname=new_nickname,  # 이렇게 따로 처리한 데이터를 넣을 수도 있습니다
                password=data[8],
                student_card=data[9],
                student_number=data[10],
                user_name=data[11],
                user_profile=data[12],
                user_role_id=data[13],
                deleted_at=data[14],
                last_nickname_updated_at=data[15],
                is_blacklist=data[16],
                point_balance=data[17],
            )

            # 만들어진 스키마는 리스트에 저장됩니다
            parsed_data.append(model)

        return parsed_data

