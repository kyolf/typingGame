# Typer-K

Typer-K is a console typing game in which you are prompted to type the sentence that is shown.
I made this in order to practice my python skills.

## Stack
**Programming Languages:** PostgreSQL, Python3
**Tools:** command line, Visual Studio Code, 

## How to use this?

1. Fork it into your repo and git clone it.
2. Make sure python3 and postgreSQL is downloaded
3. Do ` cd path/to/your/folder` in your terminal. 
4. Do ` pg_ctl status` in your terminal to see if a PostgreSQL local server is running.
5. If it is, do ` pg_ctl stop` in terminal to shut down server. If it is not, do ` pg_ctl start -l "$PGDATA/server.log` in terminal to start database.
6. Once the server is running, create a database typer with the user dev and password 123
7. Then run `psql -U dev -f ~/path-to-create_difficulty_tables.sql typer` and enter password. This is to create the tables in the database typer.
8. Then run `psql -U dev -f ~/path-to-sentences.sql typer` and enter password. This is to insert the values in the database typer.
9. Then run `python game.py` in the terminal where your typer folder is located at.
10. Play the game!
11. If you want to add more to the easy, normal, and hard list, remember to drop all the tables in the database by using `psql -U dev -f ~/path-to-drop_tables.sql typer` and run steps 7 and 8 again once you change the sentences.sql file.

## Need To Fix
* The Error Algorithm
