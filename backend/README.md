# AidKo Backend - FastAPI + PostgreSQL

A robust Q&A platform backend built with FastAPI and PostgreSQL following clean architecture principles.

## Project Structure

```
app/
├── api/                 # API routers (endpoints)
│   ├── users.py        # User endpoints
│   ├── categories.py   # Category endpoints
│   ├── questions.py    # Question endpoints
│   └── answers.py      # Answer endpoints
├── core/               # Core configuration
│   └── config.py       # Settings and environment variables
├── db/                 # Database configuration
│   └── database.py     # SQLAlchemy setup and session management
├── models/             # SQLAlchemy ORM models
│   └── models.py       # All database models
├── repositories/       # Data access layer (repositories)
│   └── repositories.py # Database query methods
├── schemas/            # Pydantic validation schemas
│   └── schemas.py      # Request/response schemas
├── services/           # Business logic layer
│   └── services.py     # Service classes
├── utils/              # Utility functions
│   └── security.py     # Authentication & JWT utilities
└── main.py            # FastAPI application entry point
```

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- PostgreSQL 12+
- pip (Python package manager)

### 2. Install Dependencies

```bash
cd /Users/murtazo/SelfImprovementProjects/adinko-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Database Setup

Create PostgreSQL database:
```bash
createdb adinko_db
```

Or using psql:
```sql
CREATE DATABASE adinko_db;
```

### 4. Environment Configuration

Copy `.env.example` to `.env` and update values:
```bash
cp .env.example .env
```

Update `.env` with your database credentials:
```
DATABASE_URL=postgresql://username:password@localhost:5432/adinko_db
SECRET_KEY=your-secret-key-here
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

Server will be available at: `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Alternative Docs: `http://localhost:8000/redoc`

## API Endpoints

### Users
- `POST /api/v1/users/register` - Register new user
- `POST /api/v1/users/login` - User login
- `GET /api/v1/users/{user_id}` - Get user profile
- `GET /api/v1/users/` - Get all users
- `GET /api/v1/users/{user_id}/questions` - Get user's questions
- `GET /api/v1/users/{user_id}/answers` - Get user's answers
- `GET /api/v1/users/{user_id}/reputation` - Get user reputation

### Categories
- `GET /api/v1/categories/` - Get all categories
- `POST /api/v1/categories/` - Create category
- `GET /api/v1/categories/{category_id}` - Get category
- `GET /api/v1/categories/{category_id}/questions` - Get category questions

### Questions
- `POST /api/v1/questions/` - Create question
- `GET /api/v1/questions/` - Get questions (with filtering)
- `GET /api/v1/questions/featured` - Get featured questions
- `GET /api/v1/questions/recent` - Get recent questions
- `GET /api/v1/questions/{question_id}` - Get question details
- `PUT /api/v1/questions/{question_id}` - Update question
- `DELETE /api/v1/questions/{question_id}` - Delete question
- `POST /api/v1/questions/{question_id}/upvote` - Upvote question
- `POST /api/v1/questions/{question_id}/resolve` - Mark as resolved

### Answers
- `POST /api/v1/answers/` - Create answer
- `GET /api/v1/answers/{answer_id}` - Get answer
- `PUT /api/v1/answers/{answer_id}` - Update answer
- `DELETE /api/v1/answers/{answer_id}` - Delete answer
- `POST /api/v1/answers/{answer_id}/accept` - Accept answer
- `POST /api/v1/answers/{answer_id}/upvote` - Upvote answer

## Architecture

### Clean Architecture Layers

1. **API Layer** (`app/api/`)
   - HTTP endpoints
   - Request/response handling
   - Status codes and error handling

2. **Service Layer** (`app/services/`)
   - Business logic
   - Data validation
   - Complex operations

3. **Repository Layer** (`app/repositories/`)
   - Database queries
   - CRUD operations
   - Data access abstraction

4. **Models Layer** (`app/models/`)
   - SQLAlchemy ORM models
   - Database schema definition

5. **Schemas Layer** (`app/schemas/`)
   - Pydantic models for validation
   - Request/response DTOs

## Database Models

### Core Tables
- **users** - User accounts with reputation scores
- **categories** - Question categories
- **tags** - Question tags
- **questions** - Q&A questions
- **answers** - Answers to questions
- **comments** - Comments on questions/answers
- **reactions** - Votes and reactions
- **events** - Community events
- **blog_posts** - Platform blog articles

## Authentication

JWT-based authentication with token generation and validation:
- Login endpoint returns `access_token`
- Include token in `Authorization: Bearer <token>` header
- Tokens expire after 30 minutes (configurable)

## Development

### Run Tests
```bash
pytest
```

### Create Database Migrations
```bash
alembic upgrade head
```

### Format Code
```bash
black app/
isort app/
```

## Deployment

### Production Setup
1. Set `DEBUG=False` in settings
2. Use strong `SECRET_KEY`
3. Configure proper database URL
4. Use production ASGI server (gunicorn + uvicorn):
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
   ```

## Next Steps

1. ✅ Database models created
2. ✅ API routers set up
3. ⏳ Connect frontend to backend
4. ⏳ Add real-time features (WebSockets)
5. ⏳ Implement authentication guards
6. ⏳ Add pagination and filtering
7. ⏳ Add caching layer (Redis)
8. ⏳ Implement rate limiting

## Support

For issues or questions, refer to:
- FastAPI: https://fastapi.tiangolo.com
- SQLAlchemy: https://docs.sqlalchemy.org
- Pydantic: https://docs.pydantic.dev
