import os

db_host = os.environ.get('DB_HOST', default='127.0.0.1')
db_name = os.environ.get('DB_NAME', default='notes')
db_username = os.environ.get('DB_USERNAME', default='notes')
db_password = os.environ.get('DB_PASSWORD', default='')
db_port = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
