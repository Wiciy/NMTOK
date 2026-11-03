from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Movie
from schemas import MovieCreate, MovieResponse

app = FastAPI()


# Funkcja pomocnicza do pobierania sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/movies",
    response_model=MovieResponse,
    status_code=status.HTTP_201_CREATED
)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    # 1. Tworzenie obiektu modelu SQLAlchemy na podstawie przekazanych danych
    db_movie = Movie(
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