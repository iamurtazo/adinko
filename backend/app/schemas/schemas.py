from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    full_name: str
    bio: Optional[str] = None
    location: Optional[str] = None
    country: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    country: Optional[str] = None
    avatar_url: Optional[str] = None

class UserResponse(UserBase):
    id: int
    reputation_score: int
    is_active: bool
    is_verified: bool
    avatar_url: Optional[str]
    joined_date: datetime
    last_login: Optional[datetime]
    
    class Config:
        from_attributes = True

# Category Schemas
class CategoryBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    icon_url: Optional[str] = None
    color_hex: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    question_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Tag Schemas
class TagBase(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = None

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: int
    usage_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Question Schemas
class QuestionBase(BaseModel):
    title: str = Field(..., min_length=10, max_length=300)
    description: str = Field(..., min_length=20)
    category_id: int
    tags: Optional[str] = None

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    tags: Optional[str] = None

class QuestionResponse(QuestionBase):
    id: int
    author_id: int
    author: UserResponse
    category: CategoryResponse
    view_count: int
    vote_count: int
    is_resolved: bool
    is_featured: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Answer Schemas
class AnswerBase(BaseModel):
    content: str = Field(..., min_length=20)

class AnswerCreate(AnswerBase):
    question_id: int

class AnswerUpdate(BaseModel):
    content: str = Field(..., min_length=20)

class AnswerResponse(AnswerBase):
    id: int
    author_id: int
    author: UserResponse
    question_id: int
    vote_count: int
    is_accepted: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Comment Schemas
class CommentBase(BaseModel):
    content: str = Field(..., min_length=5)

class CommentCreate(CommentBase):
    question_id: Optional[int] = None
    answer_id: Optional[int] = None

class CommentUpdate(BaseModel):
    content: str = Field(..., min_length=5)

class CommentResponse(CommentBase):
    id: int
    author_id: int
    author: UserResponse
    question_id: Optional[int]
    answer_id: Optional[int]
    vote_count: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Event Schemas
class EventBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: str
    location: Optional[str] = None
    start_date: datetime
    end_date: datetime
    image_url: Optional[str] = None

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    image_url: Optional[str] = None

class EventResponse(EventBase):
    id: int
    attendee_count: int
    is_featured: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# BlogPost Schemas
class BlogPostBase(BaseModel):
    title: str = Field(..., min_length=10, max_length=300)
    slug: str = Field(..., max_length=300)
    content: str = Field(..., min_length=50)
    excerpt: Optional[str] = None
    featured_image_url: Optional[str] = None

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    excerpt: Optional[str] = None
    featured_image_url: Optional[str] = None
    is_featured: Optional[bool] = None

class BlogPostResponse(BlogPostBase):
    id: int
    author_id: int
    author: UserResponse
    view_count: int
    is_featured: bool
    is_published: bool
    published_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Reaction Schema
class ReactionCreate(BaseModel):
    reaction_type: str  # "upvote", "downvote", "useful", "bookmark"
    question_id: Optional[int] = None
    answer_id: Optional[int] = None
    comment_id: Optional[int] = None

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class TokenData(BaseModel):
    email: Optional[str] = None
