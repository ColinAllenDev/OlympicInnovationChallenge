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
        MovieLength INTEGER NOT NULL,
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

    cur.execute('DROP TABLE IF EXISTS Comments')
    cur.execute('''
    CREATE TABLE Comments(
        UserID INTEGER NOT NULL,
        MovieID INTEGER NOT NULL,
        Comment VARCHAR(255) NOT NULL,
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    )
    ''')

    cur.execute('DROP TABLE IF EXISTS Ratings')
    cur.execute('''
    CREATE TABLE Ratings(
        UserID INTEGER NOT NULL,
        MovieID INTEGER NOT NULL,
        Rating Integer NOT NULL,
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    )
    ''')

    cur.execute('DROP TABLE IF EXISTS Friends')
    cur.execute('''
    CREATE TABLE Friends(
        UserID1 INTEGER NOT NULL,
        UserID2 INTEGER NOT NULL,
        Time DATE DEFAULT (datetime('now','localtime')),
        FOREIGN KEY (UserID1) REFERENCES Users(UserID),
        FOREIGN KEY (UserID2) REFERENCES Users(UserID)
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

    # for row in cur.execute("SELECT * FROM Users ORDER BY UserID"):
    #     print(row)

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

    # for row in cur.execute("SELECT * FROM Movies ORDER BY MovieID"):
    #     print(row)

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

    # for row in cur.execute("SELECT * FROM UserWatchesMovie ORDER BY UserID"):
    #     print(row)

def populate_comments():
    with open('./resources/comment.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        comments = []
        for row in reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
            else:
                if ("user_id" not in row):
                    comment = [int(row[0]), int(row[1]), row[2]]
                    comments.append(comment)
            line_count += 1

    cur.executemany("INSERT INTO Comments VALUES (?, ?, ?)", comments)

    for row in cur.execute("SELECT * FROM Comments ORDER BY UserID"):
        print(row)

def populate_ratings():
    with open('./resources/rating.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        ratings = []
        for row in reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
            else:
                if ("user_id" not in row):
                    rating = [int(row[0]), int(row[1]), int(row[2])]
                    ratings.append(rating)
            line_count += 1

    cur.executemany("INSERT INTO Ratings VALUES (?, ?, ?)", ratings)

    # for row in cur.execute("SELECT * FROM Ratings ORDER BY UserID"):
    #     print(row)

def populate_friends():
    with open('./resources/friendList.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        friends = []
        for row in reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
            else:
                if ("user_id" not in row):
                    friend = [int(row[0]), int(row[1]), None]
                    friends.append(friend)
            line_count += 1

    cur.executemany("INSERT INTO Friends VALUES (?, ?, ?)", friends)

    # for row in cur.execute("SELECT * FROM Friends ORDER BY UserID1"):
    #     print(row)

def show_name_movie_duration_length():
    for row in cur.execute("""
    SELECT U.FirstName, U.LastName, M.MovieTitle, UWM.DurationWatched, M.MovieLength
    FROM Users as U 
    INNER JOIN UserWatchesMovie as UWM ON U.UserID = UWM.UserID
    INNER JOIN Movies as M ON UWM.MovieID = M.MovieID
    """):
        print(row)

def show_name_movie_comment():
    for row in cur.execute("""
    SELECT U.FirstName, U.LastName, M.MovieTitle, C.Comment
    FROM Users as U 
    INNER JOIN Comments as C ON U.UserID = C.UserID
    INNER JOIN Movies as M ON C.MovieID = M.MovieID
    """):
        print(row)

def show_name_movie_rating():
    for row in cur.execute("""
    SELECT U.FirstName, U.LastName, M.MovieTitle, R.Rating
    FROM Users as U 
    INNER JOIN Ratings as R ON U.UserID = R.UserID
    INNER JOIN Movies as M ON R.MovieID = M.MovieID
    """):
        print(row)

def show_friends():
    # This might not be the right way to query this
    # Please confirm
    for row in cur.execute("""
    SELECT U1.FirstName, U1.LastName, U2.FirstName, U2.LastName
    FROM Friends as F
    JOIN Users as U1 ON F.UserID1 = U1.UserID
    JOIN Users as U2 ON F.UserID2 = U2.UserID
    """):
        print(row)
make_db()

populate_users()
populate_movies()
populate_user_watches_movie()
populate_comments()
populate_ratings()
populate_friends()

show_name_movie_duration_length()
show_name_movie_comment()
show_name_movie_rating()
show_friends()

con.commit()
con.close()
