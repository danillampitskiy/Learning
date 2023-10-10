

from setup_database import Film, session

films_to_add = [
    Film(title='Film 1', director='Director 1', release_year=2000),
    Film(title='Film 2', director='Director 2', release_year=2010),
    Film(title='Film 3', director='Director 3', release_year=2020)
]

session.add_all(films_to_add)
session.commit()


film_to_update = session.query(Film).filter(Film.title == 'Film 1').first()
if film_to_update:
    film_to_update.release_year = 2005
    session.commit()


films = session.query(Film).all()
for film in films:
    print(f"Film ID: {film.id}, Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}")

session.query(Film).delete()
session.commit()