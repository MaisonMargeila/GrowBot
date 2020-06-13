
#LIKEING
#session = InstaPy(username="viralism1", password="Viral@786")
#session = InstaPy(username="travelling.lad", password="Japan@786")
#session = InstaPy(username="mayankshivhare", password="Shivhare@786")

import datetime
import random
import time
from threading import Thread

from InstagramAPI import InstagramAPI

username = "travelling.lad"
password = "Japan@786"

NumberOfLikes = 100
NumberOfComment = 50
NumberofFollow = 200
MaxTimeLike = 1 * 30 * 60  ################2 stands for hours
MaxTimeComment = 1 * 30 * 60  ################2 stands for hours

api = InstagramAPI(username, password)


def Login():
    api.login()


def Logout():
    api.logout()


def Time():
    x = datetime.datetime.now()
    print(x.strftime("%X"))


commentList = [
    "Your Feeds are awesome",
    "That's a lovely Click :)",
    "Love This",
    "Awesome",
    "Nice Click",
    "Wow",
    "This is really Cool",
    "Well Captured",
    "This looks amazing",
    "Your content is awesome. Feel Free to look mine",
    "Your content is awesome, please have a look at mine content and give me your feedback :)",
    "Amazingly caputed, looking forward for more feeds like this",
    "Good job! You are going to be very famous",
    "Hey! you photos are getting better with time",
    "Captured Perfectly :)",
    "Hey! Good going you have one of the best galleries I have seen today. Do check mine too :)",
    "Amazing, Keep it up",
    "The best of the best",
    "This is absolutely awesome",
    "This shot looks really amazing...",
    "Lovely",
    "Amazing",
    "Beautiful Click",
    "This picture looks so good",
    "This picture is super awesome",
    "Nice",
    "Good One"

]


def PopularFeeds(WhatPopularFeed):
    api.getPopularFeed()
    feed = api.LastJson
    # print(feed)
    if (WhatPopularFeed == "user_id"):  ###### This will return Popular user_id
        ListOfPopularUserid = []
        for items in feed["items"]:
            for caption in items:
                if caption == "caption":
                    try:
                        UserID = (items[caption]['user_id'])
                        # print("user_id %s" % UserID)
                        int(UserID)
                        ListOfPopularUserid.append(UserID)
                    except:
                        # print("Cant get user_id")
                        print("")

        # print("This is the list of user_id that is getting returned %s" % ListOfPopularUserid)
        return ListOfPopularUserid

    if (WhatPopularFeed == "media_id"):  ###### This will return Popular media_id
        ListOfMediaId = []
        for items in feed["items"]:
            for caption in items:
                if caption == "caption":
                    try:
                        MediaId = (items[caption]['media_id'])
                        # print("Media_id %s" % MediaId)
                        int(MediaId)
                        ListOfMediaId.append(MediaId)
                    except:
                        # print("Cant get media id")
                        print("")

        # print("This is the list of media id that is getting returned %s" % ListOfMediaId)
        return ListOfMediaId


def MyFollowingFeeds():
    api.timelineFeed()
    feed = api.LastJson
    ListOfMyFollowingFeeds = []
    for items in feed["items"]:
        for caption in items:
            if caption == "caption":
                try:
                    MediaId = (items[caption]['media_id'])
                    # print("Media_id %s" % MediaId)
                    int(MediaId)
                    ListOfMyFollowingFeeds.append(MediaId)
                except:
                    # print("Cant get media id")
                    print("")

    # print("This is the list of user_id that is getting returned %s" % ListOfMyFollowingFeeds)
    return ListOfMyFollowingFeeds


def Like(MediaToLike):
    try:
        api.like(mediaId=MediaToLike)
        print("Liking Media %i" % MediaToLike)
        time.sleep(2)
    except:
        print("Cant Like Media %i" % MediaToLike)


def Comment(MediaToComment, CommentData):
    try:
        api.comment(MediaToComment, CommentData)
        print("commenting %i %s" % (MediaToComment, CommentData))
    except:
        print("Unable to comment %i %s" % (MediaToComment, CommentData))


def Follow(user_id):
    try:
        api.follow(user_id)
        print("Following %i" % user_id)
    except:
        print("Unable to follow user %i" % user_id)


def Unfollow(user_id):
    try:
        api.unfollow(user_id)
        print("Unfollowing %i" % user_id)
    except:
        print("Cant Unfollow %i" % user_id)


def GetFollowerlist():
    api.getTotalSelfFollowers()
    follower = api.LastJson
    usernameList = []

    for user in follower['users']:
        usernameOfFollower = (user['username'])
        usernameList.append(usernameOfFollower)
    return usernameList


def GetFollowingList():
    api.getTotalSelfFollowings()
    following = api.LastJson
    followingList = []

    for user in following['users']:
        usernameOfFollowing = (user['username'])
        followingList.append(usernameOfFollowing)
    return followingList

def FeedsofPopularUser():
    popularUser = PopularFeeds("user_id")
    # print(popularUser)
    api.getUserFeed(popularUser[1])
    feedsofPopularUser = api.LastJson

    ListOfMediaIds = []
    # print(feedsofPopularUser)
    for items in feedsofPopularUser["items"]:
        for caption in items:
            if caption == "caption":
                try:
                    MediaId = (items[caption]['media_id'])
                    # print("Media_id %s" % MediaId)
                    int(MediaId)
                    ListOfMediaIds.append(MediaId)
                    # print(ListOfMediaIds)
                except:
                    # print("Cant get media id")
                    print("")
    return ListOfMediaIds

class Like_logic(Thread):
    def run(self):
        likeNumber = 0
        while likeNumber <= NumberOfLikes:        # fir total number of likes in one run
            i = 0                                 # for liking 15-20 media in a single loop
            while i <= random.randint(15, 20):
                popularfeed = PopularFeeds("media_id")
                randomPopularFeedForLike = random.sample(popularfeed, 1)
                Like(randomPopularFeedForLike[0])
                likeNumber += 1
                i += 1

                print("Like Number %i" % likeNumber)  # Sleeping for min 3 and max 10 seconds
                time.sleep(random.randint(3, 10))  # Sleeping between two likes

                followingFeeds = MyFollowingFeeds()
                randomFollowingFeedForLike = random.sample(followingFeeds, 1)
                Like(randomFollowingFeedForLike[0])
                likeNumber += 1
                print("Like Number %i" % likeNumber)
                i += 1

                popularUserFeed=FeedsofPopularUser()           #liking first 7 media of popular accounts
                for firstfewmedia in range(7):
                    Like(popularUserFeed[firstfewmedia])
                    likeNumber += 1
                    print("Like Number %i" % likeNumber)
                    i += 1


                sleepingtime = random.randint(60, 120)  # sleeping for min 1  max 2 minutes
                # sleepingtime = random.randint(6, 12)  # sleeping for min 1  max 2 minutes
                print("Sleeping for %i" % sleepingtime)  # sleeping time between two likes
                time.sleep(sleepingtime)

            print(likeNumber)
            sleepingtime = random.randint(1800, 3600)  # sleep of 30 minutes to 1 hour between 1 cycle
            # sleepingtime = random.randint(18, 36)  # sleep of 30 minutes to 1 hour between 1 cycle
            print("Sleeping for %i" % sleepingtime)
            time.sleep(sleepingtime)  # sleep of 30 minutes to 1 hour between 1 cycle


class Comment_logic(Thread):
    def run(self):
        commentNumber = 0
        while commentNumber <= NumberOfComment:
            popularfeed = PopularFeeds("media_id")
            randomPopularFeedForComment = random.sample(popularfeed, 1)
            randomComment = random.sample(commentList, 1)

            formattedComment = str(randomComment[0])
            Comment(randomPopularFeedForComment[0], formattedComment)
            commentNumber += 1
            print("Comment Number %i" % commentNumber)

            print(commentNumber)
            sleepingtime = random.randint(1800, 2400)  # sleeping for 30-40 minutes between each comment
            # sleepingtime = random.randint(18, 24)  # sleeping for 30-40 minutes between each comment
            print("Sleeping for %i" % sleepingtime)
            time.sleep(sleepingtime)


class Follow_logic(Thread):
    def run(self):
        followNumber = 0
        while followNumber <= NumberofFollow:
            popularUser = PopularFeeds("user_id")
            randomPopularFeedForFollow = random.sample(popularUser, 1)
            Follow(randomPopularFeedForFollow[0])
            followNumber += 1
            print("Follow Number %i" % followNumber)

            print(followNumber)
            sleepingtime = random.randint(1800, 2400)  # sleeping for 30-40 minutes between each Follow
            # sleepingtime = random.randint(18, 24)  # sleeping for 30-40 minutes between each Follow
            print("Sleeping for %i" % sleepingtime)
            time.sleep(sleepingtime)


if __name__ == '__main__':
    try:
        Login()
        print(Time())
        t1 = Like_logic()
        t2 = Comment_logic()


        t1.start()
        t2.start()


        t1.join()
        t2.join()




    except:

        print(Time())
        print("Logging Out")
        input("Program has ended")
        Logout()
