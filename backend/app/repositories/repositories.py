from sqlalchemy.orm import Session
from sqlalchemy.sql import select, func
from app.models.models import User, Question, Answer, Comment, Category, Tag, Event, BlogPost, Reaction
from app.schemas.schemas import UserCreate, QuestionCreate, AnswerCreate, CommentCreate
from typing import Optional, List

class BaseRepository:
    """Base repository class with common CRUD operations."""
    
    def __init__(self, db: Session):
        self.db = db

class UserRepository(BaseRepository):
    """User data access layer."""
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.db.query(User).filter(User.username == username).first()
    
    def create_user(self, user: UserCreate, hashed_password: str) -> User:
        """Create new user."""
        db_user = User(
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            hashed_password=hashed_password,
            bio=user.bio,
            location=user.location,
            country=user.country
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination."""
        return self.db.query(User).offset(skip).limit(limit).all()
    
    def update_reputation(self, user_id: int, points: int) -> None:
        """Update user reputation score."""
        user = self.get_user_by_id(user_id)
        if user:
            user.reputation_score += points
            self.db.commit()

class CategoryRepository(BaseRepository):
    """Category data access layer."""
    
    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        """Get category by ID."""
        return self.db.query(Category).filter(Category.id == category_id).first()
    
    def get_all_categories(self) -> List[Category]:
        """Get all categories."""
        return self.db.query(Category).order_by(Category.question_count.desc()).all()
    
    def create_category(self, name: str, description: Optional[str] = None, 
                       icon_url: Optional[str] = None, color_hex: Optional[str] = None) -> Category:
        """Create new category."""
        category = Category(
            name=name,
            description=description,
            icon_url=icon_url,
            color_hex=color_hex
        )
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

class QuestionRepository(BaseRepository):
    """Question data access layer."""
    
    def get_question_by_id(self, question_id: int) -> Optional[Question]:
        """Get question by ID."""
        return self.db.query(Question).filter(Question.id == question_id).first()
    
    def get_all_questions(self, skip: int = 0, limit: int = 20, 
                         category_id: Optional[int] = None) -> List[Question]:
        """Get all questions with optional filtering."""
        query = self.db.query(Question)
        if category_id:
            query = query.filter(Question.category_id == category_id)
        return query.order_by(Question.created_at.desc()).offset(skip).limit(limit).all()
    
    def get_recent_questions(self, limit: int = 10) -> List[Question]:
        """Get recently created questions."""
        return self.db.query(Question).order_by(Question.created_at.desc()).limit(limit).all()
    
    def get_featured_questions(self) -> List[Question]:
        """Get featured questions."""
        return self.db.query(Question).filter(Question.is_featured == True).all()
    
    def create_question(self, question: QuestionCreate, author_id: int) -> Question:
        """Create new question."""
        db_question = Question(
            title=question.title,
            description=question.description,
            author_id=author_id,
            category_id=question.category_id,
            tags=question.tags
        )
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)
        return db_question
    
    def increment_view_count(self, question_id: int) -> None:
        """Increment question view count."""
        question = self.get_question_by_id(question_id)
        if question:
            question.view_count += 1
            self.db.commit()
    
    def get_questions_by_author(self, author_id: int, skip: int = 0, limit: int = 20) -> List[Question]:
        """Get questions by specific author."""
        return self.db.query(Question).filter(
            Question.author_id == author_id
        ).order_by(Question.created_at.desc()).offset(skip).limit(limit).all()
    
    def search_questions(self, search_term: str, skip: int = 0, limit: int = 20) -> List[Question]:
        """Search questions by title or description."""
        return self.db.query(Question).filter(
            (Question.title.ilike(f"%{search_term}%")) |
            (Question.description.ilike(f"%{search_term}%"))
        ).order_by(Question.created_at.desc()).offset(skip).limit(limit).all()

class AnswerRepository(BaseRepository):
    """Answer data access layer."""
    
    def get_answer_by_id(self, answer_id: int) -> Optional[Answer]:
        """Get answer by ID."""
        return self.db.query(Answer).filter(Answer.id == answer_id).first()
    
    def get_answers_by_question(self, question_id: int, skip: int = 0, limit: int = 50) -> List[Answer]:
        """Get all answers for a question."""
        return self.db.query(Answer).filter(
            Answer.question_id == question_id
        ).order_by(Answer.created_at.desc()).offset(skip).limit(limit).all()
    
    def create_answer(self, answer: AnswerCreate, author_id: int) -> Answer:
        """Create new answer."""
        db_answer = Answer(
            content=answer.content,
            author_id=author_id,
            question_id=answer.question_id
        )
        self.db.add(db_answer)
        self.db.commit()
        self.db.refresh(db_answer)
        return db_answer
    
    def accept_answer(self, answer_id: int) -> None:
        """Mark answer as accepted."""
        answer = self.get_answer_by_id(answer_id)
        if answer:
            answer.is_accepted = True
            self.db.commit()

class CommentRepository(BaseRepository):
    """Comment data access layer."""
    
    def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        """Get comment by ID."""
        return self.db.query(Comment).filter(Comment.id == comment_id).first()
    
    def create_comment(self, comment: CommentCreate, author_id: int) -> Comment:
        """Create new comment."""
        db_comment = Comment(
            content=comment.content,
            author_id=author_id,
            question_id=comment.question_id,
            answer_id=comment.answer_id
        )
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment

class EventRepository(BaseRepository):
    """Event data access layer."""
    
    def get_all_events(self, skip: int = 0, limit: int = 20) -> List[Event]:
        """Get all upcoming events."""
        return self.db.query(Event).order_by(Event.start_date.asc()).offset(skip).limit(limit).all()
    
    def get_featured_events(self) -> List[Event]:
        """Get featured events."""
        return self.db.query(Event).filter(Event.is_featured == True).all()

class BlogPostRepository(BaseRepository):
    """BlogPost data access layer."""
    
    def get_published_posts(self, skip: int = 0, limit: int = 20) -> List[BlogPost]:
        """Get published blog posts."""
        return self.db.query(BlogPost).filter(
            BlogPost.is_published == True
        ).order_by(BlogPost.published_at.desc()).offset(skip).limit(limit).all()
    
    def get_featured_posts(self) -> List[BlogPost]:
        """Get featured blog posts."""
        return self.db.query(BlogPost).filter(
            BlogPost.is_featured == True,
            BlogPost.is_published == True
        ).all()
