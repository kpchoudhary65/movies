from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .models import Movie
from . import db, appbuilder

import datetime
import json

from flask_appbuilder import BaseView, ModelView, expose

class MovieView(ModelView):
    datamodel = SQLAInterface(Movie)


class InsertMovies(BaseView):
    default_view = "insert_movies"

    @expose("/insert_movies/")
    def insert_movies(self):
        """
            This is the function for inserting the data into the databse
        """

        with open('movies_data.json') as json_file:  
            row_data = json.load(json_file)
        
        for data in row_data:
            release_date = datetime.datetime.strptime(data['release_date'], "%Y-%m-%dT%H:%M:%SZ")
            formatted_release_date = release_date.strftime("%Y-%m-%d")
            movie = Movie(
                movie=data['film'],
                movie_name=data['filmLabel'],
                imdb_id=data['imdb_id'],
                release_date=formatted_release_date
            )

            db.session.add(movie)
            db.session.commit()

        return self.render_template("success_page.html", context={'message':'Data inserted into the database successfully.'})

# Create db
db.create_all()
