from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.database import engine, Base
from app.models.models import User, Question, Answer, Comment, Category, Tag, Event, BlogPost, Reaction
from app.api import questions, answers, categories, users

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A Q&A platform for expats in Korea",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    users.router,
    prefix=f"{settings.API_V1_STR}/users",
    tags=["users"]
)

app.include_router(
    categories.router,
    prefix=f"{settings.API_V1_STR}/categories",
    tags=["categories"]
)

app.include_router(
    questions.router,
    prefix=f"{settings.API_V1_STR}/questions",
    tags=["questions"]
)

app.include_router(
    answers.router,
    prefix=f"{settings.API_V1_STR}/answers",
    tags=["answers"]
)

# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to AidKo Q&A Platform API",
        "version": "1.0.0",
        "docs": "/docs",
        "api_version": settings.API_V1_STR
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
