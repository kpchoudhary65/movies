from sqlalchemy import Column, String, Date, Integer
from flask_appbuilder import Model



class Movie(Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    movie = Column(String(255), nullable=False)
    movie_name = Column(String(255), nullable=False)
    imdb_id = Column(String(255), nullable=False)
    release_date = Column(Date, nullable=False)
