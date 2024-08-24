## 템플릿 사용법

1. `database.py` 안에 데이터베이스 정보를 설정합니다
   - `db_id` : 계정 id
   - `db_password` : 계정 비밀번호
   - `database_url` : 마이그레이션할 데이터베이스 url, port, 스키마명

2. `models` 폴더 안에 마이그레이션을 할 테이블의 모델을 만듭니다
    - `users.py` 예시를 참고해주세요
    - `model`은 database table과 1대1 매칭되는 형태입니다

3. 마찬가지로 `schemas` 폴더 안에 마이그레이션을 할 테이블의 스키마를 만듭니다
    - `schema`는 `model`에 넣을 데이터의 타입을 1차적으로 검증해줍니다 (string을 datetime으로 바꾼다거나..)
    - `null_filter` 함수는 새로운 schema에 그대로 복사해서 넣어주세요

4. `csv_files` 폴더 안에 csv를 넣어주세요

5. `parser.py` 파일 안에 `parser` 함수를 수정해주세요
    - csv 데이터를 schema로 만들어주어야 합니다. csv 컬럼과 schema의 속성을 1대1 매칭시켜주세요
    - 필요할 경우, csv 데이터를 변환하는 로직을 작성해주세요

6. `main.py` 파일 내에 파일명을 수정해주세요
    - csv_files에 넣은 파일명을 넣어주면 됩니다

7. (필요할 경우)`insert_data.py` 파일에서는 대량의 데이터를 100개 단위로 끊어 bulk insert를 해줍니다. 이 100이라는 값을 수정하고 싶다면 `BATCH_SIZE`를 수정해주세요 