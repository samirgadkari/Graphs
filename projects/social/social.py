import random
import collections


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[
                userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(i)

        # Create friendships
        combinations = [(i, j) for i in range(1, numUsers + 1)
                        for j in range(i, numUsers + 1) if i < j]
        random.shuffle(combinations)
        used_friendships = 0
        for i in range(numUsers):
            max_num_friendships = min(avgFriendships, numUsers)
            num_friendships = random.randint(0, max_num_friendships)
            friendships = combinations[used_friendships:used_friendships +
                                       num_friendships]
            for j in range(len(friendships)):
                self.addFriendship(friendships[j][0], friendships[j][1])
            used_friendships += num_friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}
        # paths = {}
        # cur_path = []
        # level = 0
        # q = collections.deque([(userID, level)])
        # while len(q) > 0:
        #     e, l = q.popleft()

        #     if e.name not in visited.keys():

        #         level += 1
        #         friends = collections.deque(
        #             [(x.name, level) for x in self.friendships[e.name]])
        #         level -= 1
        #         visited[e.name] = level
        #         q.extend(friends)
        #         paths[e.name] = cur_path[:level + 1].append(e.name)

        # return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    exit(0)
    connections = sg.getAllSocialPaths(1)
    print(connections)
