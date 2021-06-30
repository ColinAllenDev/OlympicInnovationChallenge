# note this is a "scratch" python script i used to clean up some csvs
# I uploaded it to the repo just in case someone wanted to modify the
# dataset
import csv
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def read_movies(whichFile):
    with open('./resources/' + whichFile, newline = '', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        moviesList = []
        movieNum = 0
        for row in reader:
            if line_count == 0:
                # print(f'Columns: {", ".join(row)}')
                print(f'{[movieNum, row[1], row[9], row[6], row[5]]}')
            else:
                if ("USA" in row[7]):
                    if (isEnglish(row[9]) and isEnglish(row[1])):
                        movie = [movieNum, row[1], row[9], row[6], row[5]]
                        movieNum += 1
                        moviesList.append(movie)
            line_count += 1
        print(f'Num Lines: {line_count}')
        return moviesList

def write_movies(moviesList):
    with open('./resources/movies_cleaned.csv', mode="w", newline = '', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in moviesList:
            writer.writerow(row)


moviesList = read_movies("movies.csv")
print(moviesList)
write_movies(moviesList)

