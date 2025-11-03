from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.schemas import AnswerCreate, AnswerResponse
from app.models.models import Answer, Question
from app.services.services import AnswerService

router = APIRouter()

@router.post("/", response_model=AnswerResponse, status_code=status.HTTP_201_CREATED)
def create_answer(answer: AnswerCreate, author_id: int = Query(...), db: Session = Depends(get_db)):
    """Create a new answer."""
    service = AnswerService(db)
    try:
        return service.create_answer(answer, author_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{answer_id}", response_model=AnswerResponse)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    """Get answer by ID."""
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer not found"
        )
    
    service = AnswerService(db)
    return service._format_answer(answer)

@router.put("/{answer_id}", response_model=AnswerResponse)
def update_answer(
    answer_id: int,
    content: str = Query(..., min_length=20),
    author_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Update an answer."""
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer not found"
        )
    
    if answer.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only edit your own answers"
        )
    
    answer.content = content
    db.commit()
    db.refresh(answer)
    
    service = AnswerService(db)
    return service._format_answer(answer)

@router.delete("/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(
    answer_id: int,
    author_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Delete an answer."""
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer not found"
        )
    
    if answer.author_id != author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own answers"
        )
    
    db.delete(answer)
    db.commit()
    return None

@router.post("/{answer_id}/accept", status_code=status.HTTP_200_OK)
def accept_answer(
    answer_id: int,
    question_author_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Mark answer as accepted."""
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer not found"
        )
    
    # Verify that the user accepting the answer is the question author
    question = db.query(Question).filter(Question.id == answer.question_id).first()
    if question.author_id != question_author_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the question author can accept answers"
        )
    
    # Unaccept other answers for this question
    db.query(Answer).filter(
        Answer.question_id == answer.question_id,
        Answer.id != answer_id
    ).update({"is_accepted": False})
    
    answer.is_accepted = True
    db.commit()
    
    return {"is_accepted": answer.is_accepted}

@router.post("/{answer_id}/upvote", status_code=status.HTTP_200_OK)
def upvote_answer(
    answer_id: int,
    user_id: int = Query(...),
    db: Session = Depends(get_db)
):
    """Upvote an answer."""
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer not found"
        )
    
    answer.vote_count += 1
    db.commit()
    
    return {"vote_count": answer.vote_count}
