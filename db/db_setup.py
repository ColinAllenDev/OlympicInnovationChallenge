import sqlite3
import csv
con = sqlite3.connect('teamolympic.db')
cur = con.cursor()

def make_db():
    cur.execute('DROP TABLE IF EXISTS Users')
    cur.execute('''
    CREATE TABLE Users(
        UserID INTEGER NOT NULL,
        LastName TEXT,
        FirstName TEXT,
        PRIMARY KEY (UserID)
    )
    ''')

    for row in cur.execute('SELECT * FROM Users ORDER BY UserID'):
        print(row)

    cur.execute('DROP TABLE IF EXISTS Movies')
    cur.execute('''
    CREATE TABLE Movies(
        MovieID INTEGER NOT NULL,
        MovieTitle VARCHAR(255) NOT NULL,
        MovieDirector VARCHAR(255),
        MovieLength VARCHAR(255) NOT NULL,
        MovieGenre VARCHAR(255),
        PRIMARY KEY (MovieID)
    )
    ''')

    cur.execute('DROP TABLE IF EXISTS UserWatchesMovie')
    cur.execute('''
    CREATE TABLE UserWatchesMovie(
        MovieID INTEGER NOT NULL,
        UserID INTEGER NOT NULL,
        DurationWatched Integer NOT NULL,
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    )
    ''')

def populate_users():
    with open('./resources/names.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        reorderedUsers = []
        for row in reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
            else:
                theUser = [int(row[2]), row[0], row[1]]
                # print(f'Row: {row}')
                reorderedUsers.append(theUser)
            line_count += 1

    cur.executemany("INSERT INTO Users VALUES (?, ?, ?)", reorderedUsers)

    for row in cur.execute("SELECT * FROM Users ORDER BY UserID"):
        print(row)


def populate_movies():
    with open('./resources/movies_cleaned.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        moviesList = []
        line_count = 0
        for row in reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
            elif line_count > 1000:
                break
            else:
                moviesList.append(row)
            line_count += 1

    cur.executemany("INSERT INTO Movies VALUES (?, ?, ?, ?, ?)", moviesList)

    for row in cur.execute("SELECT * FROM Movies ORDER BY MovieID"):
        print(row)

def populate_user_watches_movie():
    with open('./resources/userViews.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        reorderedViews = []
        for row in reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
            else:
                if ("user_id" not in row):
                    view = [int(row[1]), int(row[0]), int(row[2])]
                    reorderedViews.append(view)
            line_count += 1

    cur.executemany("INSERT INTO UserWatchesMovie VALUES (?, ?, ?)", reorderedViews)

    for row in cur.execute("SELECT * FROM UserWatchesMovie ORDER BY UserID"):
        print(row)

make_db()
populate_users()
populate_movies()
populate_user_watches_movie()

con.commit()
con.close()
