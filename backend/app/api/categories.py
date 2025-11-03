from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.schemas import CategoryCreate, CategoryResponse
from app.models.models import Category
from app.services.services import CategoryService

router = APIRouter()

@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    """Get all categories."""
    service = CategoryService(db)
    return service.get_all_categories()

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """Create new category (admin only)."""
    db_category = Category(
        name=category.name,
        description=category.description,
        icon_url=category.icon_url,
        color_hex=category.color_hex
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """Get category by ID."""
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return category

@router.get("/{category_id}/questions")
def get_category_questions(category_id: int, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Get all questions in a category."""
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    from app.models.models import Question
    questions = db.query(Question).filter(
        Question.category_id == category_id
    ).offset(skip).limit(limit).all()
    
    return questions
