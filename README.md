# Readme

## Query i used to get movies data form https://query.wikidata.org/

```
SELECT ?film ?filmLabel ?imdb_id ?release_date WHERE {
  ?film wdt:P31 wd:Q11424.
  ?film wdt:P577 ?release_date.
  ?film wdt:P345 ?imdb_id.
  FILTER (year(?release_date) > 2013)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY ?release_date

```
Download the data into the Json format and put the downloaded file in project directory with  name "movies_data.json"  this will make things easy for you otherwise you will need to do change the name of the file in the views file with you file name.



# Installation

## Clone the project with the given command

```
git clone https://github.com/kpchoudhary65/movies.git
```


## It is good practice to use the Virtual Environment.

## step 1. Create Virtual Environment

## step 2. Activate Virtual Environment

## step 3. Go to project directory

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

Use the bellow command for install aal the dependencies
```
pip install -r requirements.txt 
```

# DATABASE

I used Postgres database so you need to create the postgres database. You can use DATABASE_NAME, DATABASE_USER Or DATABASE_PASSWORD as you want if you do this then you will need to replace the DATABASE_NAME, DATABASE_PASSWORD Or DATABASE_USER in the <__init__.py file>.

Otherwise just use this commands and you have no need to change anything in the code

#commands for creating the postgres database.
```
1. CREATE DATABASE movies;

2. CREATE USER movieusers WITH ENCRYPTED PASSWORD 'movieworld';

3. GRANT ALL PRIVILEGES ON DATABASE movies TO movieusers;

```

# Create admin

```
flask fab create-admin

Add your credentials like <username> <password>
```

# Run the application

```
export FLASK_APP=app
flask run 

```
You will get the url like <http://127.0.0.1:5000> go to the url and login with the your admin cresentials

# Upload Movies

Click on the Upload Movies this will upload movies in the database
After successfull insertion of the data you will get the success message and a clickable test to go to the list of the movies where you can do the following operations.

1. Insert Movie data 
2. Update Movie data 
3. Delete Movie data 
