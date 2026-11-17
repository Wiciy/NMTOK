from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Movie, Link, Rating, Tag
from schemas import MovieCreate, MovieResponse
from sqlalchemy import func

app = FastAPI()

#ZADANIE 4

# Funkcja pomocnicza do pobierania sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#stara część z endpointami GET
#hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}

#movies
@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

#links
@app.get("/links")
def get_links(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Link).offset(skip).limit(limit).all()

#rating
@app.get("/ratings")
def get_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Rating).offset(skip).limit(limit).all()

#tags
@app.get("/tags")
def get_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Tag).offset(skip).limit(limit).all()

#Nowa częśc z endpointami POST
@app.post(
    "/movies",
    response_model=MovieResponse,
    status_code=status.HTTP_201_CREATED
)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    # 1. Tworzenie obiektu modelu SQLAlchemy na podstawie przekazanych danych
    max_id = db.query(func.max(Movie.movieId)).scalar() or 0
    db_movie = Movie(
        movieId=max_id + 1,
        title=movie.title,
        genres=movie.genres
    )

    # 2. Zapis w bazie SQLite
    db.add(db_movie)
    db.commit()

    # 3. Odświeżenie obiektu, aby pobrać nadany automatycznie klucz główny (movieId)
    db.refresh(db_movie)

    # 4. Zwrócenie zapisanego obiektu
    return db_movie