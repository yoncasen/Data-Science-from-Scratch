from collections import Counter,defaultdict

""""""
"""FINDING KEY CONNECTORS"""
""""""
users = [{"id": 0, "name": "Hero" },
         {"id": 1, "name": "Dunn" },
         {"id": 2, "name": "Sue" },
         {"id": 3, "name": "Chi" },
         {"id": 4, "name": "Thor" },
         {"id": 5, "name": "Clive" },
         {"id": 6, "name": "Hicks" },
         {"id": 7, "name": "Devin" },
         {"id": 8, "name": "Kate" },
         {"id": 9, "name": "Klein" },
         ]

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

#And loop over the friendship pairs to populate it
for i, j in friendship_pairs:
  friendships[i].append(j)
  friendships[j].append(i)

#print(friendships)

def number_of_friends(user):
  """ How many friends does _user_ have? """
  user_id = user["id"]
  friend_ids = friendships[user_id]
  return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) #24 

num_users = len(users)                                #length of the users list
avg_connections = total_connections / num_users        #24 / 10 = 2.4

#print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users] 

num_friends_by_id.sort(key= lambda id_and_friends: id_and_friends[1],   #sort the list by number_of_friends 
                       reverse=True)                                    #largest to smallest

#print(num_friends_by_id) # network metric degree centrality

""""""
"""DATA SCIENTISTS YOU MAY KNOW"""
""""""

#friends_may_know = {user["id"]: [] for user in users}

""" my test for listing friends id user may know"""
# def find_friends_may_know(user):
#   user_id = user["id"]
#   friend_ids = friendships[user_id]
#   friends = [each_friend_id for each_friend in friend_ids for each_friend_id in friendships[each_friend]]
#   return friends

# friends_may_know = {user["id"]: find_friends_may_know(user) for user in users}

# print(friends_may_know)

def foaf_ids_bad(user): 
  """foaf is shorf for "friend of a friend" """
  user_id = user["id"]
  return Counter(foaf_id 
          for friend_id in friendships[user["id"]]  #for each of my friens,
          for foaf_id in friendships[friend_id]     #find their friends
          if foaf_id != user_id                     #who aren't me
          and foaf_id not in friendships[user_id])  #and aren't my friends

#print(foaf_ids_bad(users[3])) # Counter({0: 2, 5: 1})
#print(list(foaf_ids_bad(users[3]).keys())) # [0,5]


""" my code for just listing friends id user may know """
def foaf_ids(user): 
  user_id = user["id"]
  foaf_list = []
  for friend_id in friendships[user["id"]]:  #for each of my friens,
    for foaf_id in friendships[friend_id]:     #find their friends
        if foaf_id != user_id  and foaf_id not in friendships[user_id] and foaf_id not in foaf_list:  #who aren't me and aren't my friends
          foaf_list.append(foaf_id)   
  return foaf_list

#print(foaf_ids(users[3])) 

interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"),(0, "Storm"),(0, "Cassandra"),
             (1, "NoSQL"), (1, "MongoDB"), (1, "HBase"), (1, "Cassandra"), (1, "Postgres"),
             (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"),(2, "pandas"),
             (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
             (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
             (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"),(5, "programming languages"),
             (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
             (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
             (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
             (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
             ]


def data_scientists_who_like(target_interest):
  """ Find the ids of all users who like the target interest """
  return [user_id
          for user_id, user_interest in interests
          if user_interest == target_interest]

#keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
  user_ids_by_interest[interest].append(user_id)

#keys are user ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
  interests_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
  return Counter(
    interested_user_id
    for interest in interests_by_user_id[user["id"]]
    for interested_user_id in user_ids_by_interest[interest]
    if interested_user_id != user["id"]
  )

print(most_common_interests_with(users[0]))

""""""
""" TOPICS OF INTERESTS """
""""""

words_and_counts = Counter(word
                           for user,interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
  if count > 1:
    print(word, count)

""""""