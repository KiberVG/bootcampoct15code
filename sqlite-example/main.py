import sqlite3
from data import movies















# Connects to the database if it exists, otherwise it creates a new one
con = sqlite3.connect("tutorial.db")

# Need a cursor to interact with the database
cur = con.cursor()

# Use the cursor to execute commands, dropping this table to create a new one
cur.execute("DROP TABLE movies")

# Use the CREATE TABLE (table name)((table fields)) to create a new table
cur.execute("CREATE TABLE movies(title, year, score)")

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

cur.executemany("INSERT INTO movies VALUES(?, ?, ?)", data)

# Now we want to insert all of our data
cur.executemany("INSERT INTO movies VALUES (?,?,?)", movies)

# If you just want to insert one or a couple of rows
cur.execute("""
    INSERT INTO movies VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

# Make sure to commit any changes, inserting automatically opens a transaction
con.commit()

# You can use select queries to get results and do whatever you want with them
res = cur.execute("SELECT title, year FROM movies WHERE score > 5 and year = 2003")

for tup in res:
    print(f"Movie Name: {tup[0]}, Year: {tup[1]}")


# Additional SQL queries we won't go over, but are still important

# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;

# DELETE FROM table_name WHERE condition;
