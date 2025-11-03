from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.schemas import QuestionCreate, QuestionResponse, QuestionUpdate
from app.models.models import Question
from app.services.services import QuestionService

router = APIRouter()

@router.post("/", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
def create_question(question: QuestionCreate, author_id: int = Query(...), db: Session = Depends(get_db)):
    """Create a new question."""
    service = QuestionService(db)
    try:
        return service.create_question(question, author_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=list[QuestionResponse])
def get_questions(
    skip: int = 0,
    limit: int = 20,
    category_id: int = Query(None),
    search: str = Query(None),
    db: Session = Depends(get_db)
):
    """Get questions with optional filtering and search."""
    service = QuestionService(db)
    
    if search:
        return service.search_questions(search, skip, limit)
    elif category_id:
        return service.get_questions_by_category(category_id, skip, limit)
    else:
        questions = db.query(Question).offset(skip).limit(limit).all()
        return [service._format_question(q) for q in questions]

@router.get("/featured", response_model=list[QuestionResponse])
def get_featured_questions(db: Session = Depends(get_db)):
    """Get featured questions."""
    service = QuestionService(db)
    questions = db.query(Question).filter(Question.is_featured == True).all()
    return [service._format_question(q) for q in questions]

@router.get("/recent", response_model=list[QuestionResponse])
def get_recent_questions(limit: int = 10, db: Session = Depends(get_db)):
    """Get recently created questions."""
    service = QuestionService(db)
    return service.get_recent_questions(limit)

@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    """Get question by ID."""
    service = QuestionService(db)
    try:
        return service.get_question(question_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(
    question_id: int,
    question_update: QuestionUpdate,
    author_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Update a question."""
    question = db.query(Question).filter(Question.id == question_id).first()
    
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found"
        )
    
    if question.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only edit your own questions"
        )
    
    # Update fields
    if question_update.title:
        question.title = question_update.title
    if question_update.description:
        question.description = question_update.description
    if question_update.category_id:
        question.category_id = question_update.category_id
    if question_update.tags:
        question.tags = question_update.tags
    
    db.commit()
    db.refresh(question)
    
    service = QuestionService(db)
    return service._format_question(question)

@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(
    question_id: int,
    author_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Delete a question."""
    question = db.query(Question).filter(Question.id == question_id).first()
    
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found"
        )
    
    if question.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own questions"
        )
    
    db.delete(question)
    db.commit()
    return None

@router.post("/{question_id}/upvote", status_code=status.HTTP_200_OK)
def upvote_question(
    question_id: int,
    user_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Upvote a question."""
    question = db.query(Question).filter(Question.id == question_id).first()
    
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found"
        )
    
    question.vote_count += 1
    db.commit()
    
    return {"vote_count": question.vote_count}

@router.post("/{question_id}/resolve", status_code=status.HTTP_200_OK)
def resolve_question(
    question_id: int,
    author_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Mark question as resolved."""
    question = db.query(Question).filter(Question.id == question_id).first()
    
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found"
        )
    
    if question.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the question author can resolve it"
        )
    
    question.is_resolved = True
    db.commit()
    
    return {"is_resolved": question.is_resolved}
