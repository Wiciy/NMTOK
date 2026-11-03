from pydantic import BaseModel

# Dane, które przysyła użytkownik (nie podaje movieId, bo baza generuje je sama)
class MovieCreate(BaseModel):
    title: str
    genres: str

# Dane, które API zwraca w odpowiedzi (zawierają już wygenerowane movieId)
class MovieResponse(MovieCreate):
    movieId: int

    class Config:
        from_attributes = True  # Pozwala Pydantic czytać obiekty ORM SQLAlchemy