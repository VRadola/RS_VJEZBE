from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Filmovi(BaseModel):
    naziv: str
    gerere: str
    godina: int

filmovi = [
  {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
  {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
  {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
  {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi")
def get_sve_filmove():
    return filmovi

@app.get("/filmovi/{naziv}")
def get_film_by_naziv(naziv: str):
    pronadeni_film = next((film for film in filmovi if film["naziv"] == naziv), None)
    return pronadeni_film

@app.post("/filmovi")
def post_novi_film(film: Filmovi):
    new_id = len(filmovi) + 1
    film_dict = film.model_dump()
    film_dict["id"] = new_id
    filmovi.append(film_dict)
    return film_dict