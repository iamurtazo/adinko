from sqlalchemy.orm import Session
from app.repositories.repositories import (
    UserRepository, CategoryRepository, QuestionRepository, 
    AnswerRepository, CommentRepository, EventRepository, BlogPostRepository
)
from app.schemas.schemas import UserCreate, QuestionCreate, AnswerCreate, CommentCreate
from app.utils.security import get_password_hash
from typing import Optional, List

class UserService:
    """User business logic."""
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.db = db
    
    def create_user(self, user: UserCreate) -> dict:
        """Create new user with password hashing."""
        # Check if user already exists
        existing = self.repository.get_user_by_email(user.email)
        if existing:
            raise ValueError(f"User with email {user.email} already exists")
        
        existing_username = self.repository.get_user_by_username(user.username)
        if existing_username:
            raise ValueError(f"Username {user.username} already taken")
        
        # Hash password and create user
        hashed_password = get_password_hash(user.password)
        db_user = self.repository.create_user(user, hashed_password)
        
        return {
            "id": db_user.id,
            "email": db_user.email,
            "username": db_user.username,
            "full_name": db_user.full_name
        }
    
    def get_user_profile(self, user_id: int) -> dict:
        """Get user profile information."""
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        
        return {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "bio": user.bio,
            "avatar_url": user.avatar_url,
            "reputation_score": user.reputation_score,
            "location": user.location,
            "country": user.country,
            "joined_date": user.joined_date
        }

class CategoryService:
    """Category business logic."""
    
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)
        self.db = db
    
    def get_all_categories(self) -> List[dict]:
        """Get all categories."""
        categories = self.repository.get_all_categories()
        return [
            {
                "id": cat.id,
                "name": cat.name,
                "description": cat.description,
                "icon_url": cat.icon_url,
                "color_hex": cat.color_hex,
                "question_count": cat.question_count
            }
            for cat in categories
        ]

class QuestionService:
    """Question business logic."""
    
    def __init__(self, db: Session):
        self.question_repo = QuestionRepository(db)
        self.user_repo = UserRepository(db)
        self.db = db
    
    def create_question(self, question: QuestionCreate, author_id: int) -> dict:
        """Create new question."""
        db_question = self.question_repo.create_question(question, author_id)
        return self._format_question(db_question)
    
    def get_question(self, question_id: int) -> dict:
        """Get question details."""
        question = self.question_repo.get_question_by_id(question_id)
        if not question:
            raise ValueError(f"Question {question_id} not found")
        
        # Increment view count
        self.question_repo.increment_view_count(question_id)
        
        return self._format_question(question)
    
    def get_recent_questions(self, limit: int = 10) -> List[dict]:
        """Get recently created questions."""
        questions = self.question_repo.get_recent_questions(limit)
        return [self._format_question(q) for q in questions]
    
    def get_questions_by_category(self, category_id: int, skip: int = 0, limit: int = 20) -> List[dict]:
        """Get questions by category."""
        questions = self.question_repo.get_all_questions(skip, limit, category_id)
        return [self._format_question(q) for q in questions]
    
    def search_questions(self, search_term: str, skip: int = 0, limit: int = 20) -> List[dict]:
        """Search questions."""
        questions = self.question_repo.search_questions(search_term, skip, limit)
        return [self._format_question(q) for q in questions]
    
    def _format_question(self, question) -> dict:
        """Format question for API response."""
        return {
            "id": question.id,
            "title": question.title,
            "description": question.description,
            "author": {
                "id": question.author.id,
                "username": question.author.username,
                "full_name": question.author.full_name,
                "avatar_url": question.author.avatar_url,
                "reputation_score": question.author.reputation_score
            },
            "category": {
                "id": question.category.id,
                "name": question.category.name,
                "color_hex": question.category.color_hex
            },
            "tags": question.tags.split(",") if question.tags else [],
            "view_count": question.view_count,
            "vote_count": question.vote_count,
            "answer_count": len(question.answers),
            "is_resolved": question.is_resolved,
            "is_featured": question.is_featured,
            "created_at": question.created_at,
            "updated_at": question.updated_at
        }

class AnswerService:
    """Answer business logic."""
    
    def __init__(self, db: Session):
        self.answer_repo = AnswerRepository(db)
        self.db = db
    
    def create_answer(self, answer: AnswerCreate, author_id: int) -> dict:
        """Create new answer."""
        db_answer = self.answer_repo.create_answer(answer, author_id)
        return self._format_answer(db_answer)
    
    def get_question_answers(self, question_id: int, skip: int = 0, limit: int = 50) -> List[dict]:
        """Get all answers for a question."""
        answers = self.answer_repo.get_answers_by_question(question_id, skip, limit)
        return [self._format_answer(a) for a in answers]
    
    def _format_answer(self, answer) -> dict:
        """Format answer for API response."""
        return {
            "id": answer.id,
            "content": answer.content,
            "author": {
                "id": answer.author.id,
                "username": answer.author.username,
                "full_name": answer.author.full_name,
                "avatar_url": answer.author.avatar_url,
                "reputation_score": answer.author.reputation_score
            },
            "question_id": answer.question_id,
            "vote_count": answer.vote_count,
            "is_accepted": answer.is_accepted,
            "created_at": answer.created_at,
            "updated_at": answer.updated_at
        }

class CommentService:
    """Comment business logic."""
    
    def __init__(self, db: Session):
        self.comment_repo = CommentRepository(db)
        self.db = db
    
    def create_comment(self, comment: CommentCreate, author_id: int) -> dict:
        """Create new comment."""
        if not comment.question_id and not comment.answer_id:
            raise ValueError("Comment must be on either a question or answer")
        
        db_comment = self.comment_repo.create_comment(comment, author_id)
        return self._format_comment(db_comment)
    
    def _format_comment(self, comment) -> dict:
        """Format comment for API response."""
        return {
            "id": comment.id,
            "content": comment.content,
            "author": {
                "id": comment.author.id,
                "username": comment.author.username,
                "full_name": comment.author.full_name,
                "avatar_url": comment.author.avatar_url
            },
            "vote_count": comment.vote_count,
            "created_at": comment.created_at,
            "updated_at": comment.updated_at
        }
