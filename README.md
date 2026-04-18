FastAPI Learn 🚀
A hands-on learning project for building REST APIs with FastAPI and PostgreSQL, covering both raw SQL (psycopg2) and ORM-based (SQLAlchemy) approaches side by side.


🛠️ Tech Stack
FastAPI — Modern, fast Python web framework
PostgreSQL — Relational database
psycopg2 — Raw PostgreSQL adapter for Python
SQLAlchemy — Python ORM for database interaction
Pydantic — Data validation via schemas
Uvicorn — ASGI server for running the app


⚡ Getting Started
1. Clone the repository
bashgit clone https://github.com/yepMizu/FastAPI-learn.git
cd FastAPI-learn

2. Create and activate a virtual environment
bashpython -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies
bashpip install fastapi uvicorn sqlalchemy psycopg2-binary

4. Configure your database
Update the database URLs in app/database.py and app/psycopg2_db.py with your PostgreSQL credentials:
python# database.py
SQLALCHEMY_DATABASE_URL = "postgresql://your_user:your_password@localhost/your_database"

6. Run the server
bashcd app
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000

📖 API Documentation
FastAPI provides interactive docs out of the box:
ToolURLSwagger UIhttp://127.0.0.1:8000/docsReDochttp://127.0.0.1:8000/redoc


🗂️ API Endpoints
psycopg2 (Raw SQL)
MethodEndpointDescriptionGET/posts/Get all postsPOST/posts/Add a new studentGET/posts/{id}Get a post by IDDELETE/posts/{id}Delete a post by ID
SQLAlchemy (ORM)
MethodEndpointDescriptionGET/sqlalchemy/Test SQLAlchemy connection


📝 Notes
SQLAlchemy tables are auto-created on server startup via Base.metadata.create_all(bind=engine) in main.py
Both psycopg2 and SQLAlchemy connect to the same PostgreSQL instance but are kept separate for learning purposes
Run uvicorn from inside the app/ directory to avoid Python import issues


👤 Author
GitHub: @yepMizu
