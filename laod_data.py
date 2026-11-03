from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Movie, Rating

app = FastAPI()

# Dependency do zarządzania sesją bazy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Przykład endpointu pobierającego filmy z bazy SQLite z użyciem SQLAlchemy[cite: 1]
@app.get("/movies")
def read_movies(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    movies = db.query(Movie).offset(skip).limit(limit).all()
    return movies

@app.get("/movies/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.movieId == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie