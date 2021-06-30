import names
import csv
import random


def generateUsers():
    # open/create csv 
    with open('names.csv', 'w', newline='') as csvfile:

        fieldnames = ['first_name', 'last_name', 'user_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        

        # create 100 users with random first and last names.
        for x in range(100):
            firstName = names.get_first_name()
            lastName = names.get_last_name()
            #write to csv file
            writer.writerow({'first_name': firstName, 'last_name': lastName,'user_id': x})



def generateFriends():

     # open/create csv 
    with open('friendList.csv', 'w', newline='') as csvfile:

        fieldnames = ['user_id', 'user_id_2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        friendList = {}

        #loop through all users
        for x in range(100):
            #return a list of random numbers between 0-99 and of a length between 0-5
            friendList[x] = random.sample(range(0,100),random.randrange(6))

            #Remove x from list as a user cannot be friends with themselves.
            try:
                friendList[x].remove(x)
            except ValueError:
                pass

            # remove duplicate tuples ex: (mark,john)  & (john,mark), 
            for k in friendList[x]:
                if k in friendList:
                    if x in friendList[k]:
                        friendList[x].remove(k)
        
        for user in friendList:
            for friend in friendList[user]:
                writer.writerow({'user_id': user, 'user_id_2': friend})
            

def generateRatings():
    
    ratingList = {}

    for user in range(100):
        # a list of 5 movies with id 0-99 of list len 0-5
        ratingList[user] = random.sample(range(0,100),random.randrange(6))


    with open('rating.csv', 'w', newline='') as csvfile:

        fieldnames = ['user_id', 'movie_id','rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


        #for each user that has made a rating 
        for user in ratingList:
            for movie_id in ratingList[user]:

                writer.writerow({'user_id': user, 'movie_id': movie_id, 'rating': random.randrange(1,6)})
                generateComments(user,movie_id)
                generateUserViews(movie_id,user)

def generateComments(userId, mediaId):

    positiveAdj = ['amazing', 'awesome','entertaining','riveting','compelling', 'beautiful','dazzling', 'passionate', 'funny','stunning','thrilling','breathtaking','brilliant','bold','magical','inspiring','emotional']
    noun = ['experience.', 'picture.', 'flick.', 'time.', 'epic.','visual.', 'story', 'journey',]
    subject = ['very', 'The most','An unforgettable', 'A unmissiable', 'A good','A nice', 'What a memorable', 'Such a fun', 'Absolutely', 'Absolutely the most','Flawless', 'Innovative', 'Creative', 'A smooth', 'A colorful, vibrant','A clever', 'A surprisingly vibrant', 'The greatest', 'The most soulful']


    with open('comment.csv', 'a', newline='') as csvfile:

        fieldnames = ['user_id', 'movie_id','comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        comment = random.choice(subject) + ' ' + random.choice(positiveAdj) + ' ' + random.choice(noun)

        writer.writerow({'user_id': userId, 'movie_id': mediaId, 'comment': comment})
        

def generateUserViews(mediaId, userId):
     with open('userViews.csv', 'a', newline='') as csvfile:

        fieldnames = ['user_id', 'movie_id','duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 
        writer.writerow({'user_id': userId, 'movie_id': mediaId, 'duration':random.randrange(0,90) })
            


generateFriends()
generateRatings()







