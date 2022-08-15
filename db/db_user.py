from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DBUser
from fastapi import HTTPException, status

def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DBUser).all()

def get_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'User with id {id} not found')
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'User with username {username} not found')
    return user # make new display model for the current user

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'User with id {id} not found')
    user.update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "ok"

def delete_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return "User deleted"
