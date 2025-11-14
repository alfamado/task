from database import db
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt
from enum import Enum
from middleware import create_token, verify_token

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

token_time = int(os.getenv("token_time"))

class Simple(BaseModel):
    name: str = Field(..., example="Abdulmalik Adedotun")
    email: str = Field(..., example="lionelmado@mail.com")
    password: str = Field(..., example="123")
    userType: str = Field(..., example="student")
    gender: str = Field(..., example="male")

@app.post("/signup")
def sign_up(input: Simple):
    try:
        duplicate_query = text("""
            SELECT * FROM users
            WHERE email = :email
                           """)
        existing = db.execute(duplicate_query,  {"email": input.email}).fetchone()
        if existing:
            #print("Email aready exist")
            raise HTTPException(status_code=400, detail="Email already exist")
        
        query = text("""
            INSERT INTO users(name, email, password, userType, gender)   
            VALUES(:name, :email, :password, :userType, :gender)    
        """)

        salt = bcrypt.gensalt()
        hashedpassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        # print(hashedpassword)

        db.execute(query, {"name": input.name, "email": input.email, "password": hashedpassword, "userType": input.userType, "gender": input.gender})
        db.commit()

        return {"Message": "User created successfully", "data": {'name':input.name, 'email': input.email, 'userType': input.userType, "gender": input.gender}}
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))

class LoginRequest(BaseModel):
    email: str = Field(..., example="dami@email.com")
    password: str = Field(..., example="dami123")

@app.post("/login")
def login(input: LoginRequest):
    try:
        query = text("""
            SELECT * FROM users WHERE email = :email
        """)
        result = db.execute(query, {"email": input.email}).fetchone()

        if not result:
            raise HTTPException(status_code=500, detail="invalid email or password")
        
        verify_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))

        if not verify_password:
            raise HTTPException(status_code=404, detail="invalid email or password")
    
        encoded_token = create_token(details={
            "email": result.email,
            "userType": result.userType
        }, expiry = token_time)
        
        return {
            "Message": "Login successfully",
            "token": encoded_token
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
class courseRequest(BaseModel):
    title: str = Field(..., example="Backend Course")
    level: str = Field(..., example="Beginner")

@app.post("/courses")
def addcourses(input: courseRequest, user_data = Depends(verify_token)):
    try:
        print(user_data)

        if user_data["userType"] != "admin":
            raise HTTPException(status_code=401, detail="You are not authorized to add a course")
        query = text("""
            INSERT INTO courses(title, level)   
            VALUES(:title, :level)    
        """)

        db.execute(query, {"title": input.title, "level": input.level})
        db.commit()

        return {"Message": "course successfully added", "data": {'title':input.title, 'level': input.level}}
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))

class courseId(BaseModel):
    courseId: int = Field(..., example=1)  
    


@app.post("/enrollment")
def enrollment(input: courseId, user_data= Depends(verify_token)):
    print(user_data)
    check_course = text('''
                        SELECT * FROM courses WHERE id = :courseId LIMIT 1
                        ''')
    result = db.execute(check_course, {"courseId": input.courseId}).fetchone()
    
    if result :
        if user_data['userType'] != 'admin':
            check_enrollment_exist = text('''
                        SELECT * FROM enrollments WHERE userId = :userId AND courseId = :courseId  LIMIT 1
                        ''')
            check_result = db.execute(check_enrollment_exist, {"userId":  user_data['id'], "courseId": input.courseId}).fetchone()
            if check_result:
               return {
                "message": 'You have enrolled for this course before now, just enter class! '
                }
            else:
                query = text("""
                    INSERT INTO enrollments (userId, courseId)
                    VALUES (:userId, :courseId)
                """)
                db.execute(query, {"userId":  user_data['id'], "courseId": input.courseId})
                db.commit()
                return {
                "data": 'success! '
                }
        else:
            return {
            "message": 'Only Students can enrollment! '
            }
    else:
         return {
            "message": 'Invalid course ID! '
            }

if __name__=="__main__":
     uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))