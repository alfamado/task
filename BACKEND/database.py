from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os

load_dotenv()

# db_url = dialect+driver://dbuser:dbpassword@dbhost:dbpost/dbname
db_url = f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"
# print(db_url)

engine = create_engine(
    db_url,
    connect_args = {"client_flag": CLIENT.MULTI_STATEMENTS}
    )

session = sessionmaker(bind=engine)

db = session()

# query = text("select * from user")
# users = db.execute(query).fetchall()

# print(users)

create_table_query = text("""
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR (150) NOT NULL,
    email VARCHAR (100) NOT NULL,
    password VARCHAR (100) NOT NULL
    );


CREATE TABLE IF NOT EXISTS courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR (150) NOT NULL,
    level VARCHAR (100) NOT NULL
    );


CREATE TABLE IF NOT EXISTS enrollments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    courseid INT,
    FOREIGN KEY (userid) REFERENCES users(id),
    FOREIGN KEY (courseid) REFERENCES courses(id)
    );
""")

db.execute(create_table_query)
# db.execute(create_courses)
# db.execute(create_enrollment)