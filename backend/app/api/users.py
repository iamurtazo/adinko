from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.schemas import UserCreate, UserResponse, Token
from app.services.services import UserService
from app.utils.security import verify_password, create_access_token
from app.models.models import User
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    service = UserService(db)
    try:
        created_user = service.create_user(user)
        # Fetch full user object for response
        db_user = db.query(User).filter(User.email == user.email).first()
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    """Login user and get access token."""
    user = db.query(User).filter(User.email == email).first()
    
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User account is inactive"
        )
    
    access_token = create_access_token({"sub": user.email})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.get("/", response_model=list[UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all users with pagination."""
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/{user_id}/questions")
def get_user_questions(user_id: int, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Get questions by a specific user."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    from app.models.models import Question
    questions = db.query(Question).filter(
        Question.author_id == user_id
    ).offset(skip).limit(limit).all()
    
    return questions

@router.get("/{user_id}/answers")
def get_user_answers(user_id: int, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Get answers by a specific user."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    from app.models.models import Answer
    answers = db.query(Answer).filter(
        Answer.author_id == user_id
    ).offset(skip).limit(limit).all()
    
    return answers

@router.get("/{user_id}/reputation")
def get_user_reputation(user_id: int, db: Session = Depends(get_db)):
    """Get user reputation score."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {
        "user_id": user.id,
        "username": user.username,
        "reputation_score": user.reputation_score
    }
