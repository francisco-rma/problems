from collections import deque

from heaps.heap import MaxHeap


class User:
    def __init__(self, id: int):
        self.id = id
        self.followers = set()
        self.followees = set()
        self.tweets: list[tuple[int, int]] = []


class Twitter:
    def __init__(self):
        self.tweetCount: int = 0
        self.users: dict[int, User] = {}

    def createUser(self, userId: int):
        new_user = User(userId)
        self.users[userId] = new_user

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.createUser(userId)
        user = self.users[userId]
        self.tweetCount += 1

        user.tweets.append((self.tweetCount, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            self.createUser(userId)
            # raise ValueError(f"User {userId} not found")
        user = self.users[userId]

        feed = MaxHeap(source=[], limit=10)

        # TODO
        # initialize user followers and followees to contain themselves
        # and remove this ugly ad hoc first for loop
        for ord, id in user.tweets:
            feed.heap_push([ord, id])
        for followeeId in user.followees:
            followee = self.users[followeeId]
            for ord, id in followee.tweets:
                feed.heap_push([ord, id])

        result = []
        while feed:
            result.append(feed.heap_pop()[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.createUser(followerId)
            # raise ValueError(f"User {followerId} not found")
        if followeeId not in self.users:
            self.createUser(followeeId)
            # raise ValueError(f"User {followeeId} not found")
        if followerId == followeeId:
            return

        follower = self.users[followerId]
        followee = self.users[followeeId]

        follower.followees.add(followeeId)
        followee.followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.createUser(followerId)
            # raise ValueError(f"User {followerId} not found")
        if followeeId not in self.users:
            self.createUser(followeeId)
            # raise ValueError(f"User {followeeId} not found")
        if followerId == followeeId:
            return

        follower = self.users[followerId]
        followee = self.users[followeeId]

        if followeeId in follower.followees:
            follower.followees.remove(followeeId)
        if followerId in followee.followers:
            followee.followers.remove(followerId)


# TODO
# implement all of these as heap test cases
# (making sure the pop deletes the smallest item)


def case1():
    twitter = Twitter()
    twitter.postTweet(1, 10)
    twitter.postTweet(2, 20)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.follow(1, 2)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))


def case2():
    twitter = Twitter()
    twitter.postTweet(1, 100)
    twitter.follow(1, 1)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 1)
    print(twitter.getNewsFeed(1))


def case3():
    twitter = Twitter()
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 4)
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 6)
    twitter.postTweet(1, 7)
    twitter.postTweet(1, 8)
    twitter.postTweet(1, 9)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 11)

    print(twitter.getNewsFeed(1))

    twitter.follow(2, 1)

    print(twitter.getNewsFeed(2))

    twitter.unfollow(2, 1)

    print(twitter.getNewsFeed(2))


def case4():
    twitter = Twitter()
    twitter.postTweet(7, 23)
    twitter.postTweet(7, 24)
    twitter.postTweet(7, 25)
    twitter.postTweet(7, 26)

    twitter.follow(8, 7)

    print(twitter.getNewsFeed(8))

    twitter.follow(8, 7)

    twitter.unfollow(8, 7)

    print(twitter.getNewsFeed(8))

    twitter.postTweet(7, 27)

    twitter.unfollow(8, 7)

    print(twitter.getNewsFeed(8))


def case5():
    twitter = Twitter()
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 4)
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 6)
    twitter.postTweet(1, 7)
    twitter.postTweet(1, 8)
    twitter.postTweet(1, 9)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 11)
    twitter.postTweet(1, 12)

    print(twitter.getNewsFeed(1))


if __name__ == "__main__":
    # case1()
    # case2()
    # case3()
    # case4()
    case5()
