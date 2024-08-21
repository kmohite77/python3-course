""" Problem Statement:
JSON is a commonly used format for returning objects from API calls (e.g., when we get data from Twitter, Instagram, Facebook, etc). Below, we have provided a hypothetical string userProfilesString in JSON format that contains information about 5 user profiles
Read the userProfilesString string as a python object userProfiles using json functions.
Suppose it's been 3 days since you got the Twitter profile data. In the past 3 days, the following twitter activity happened:
Iman tweeted 5 times and liked 5 tweets.
Allan tweeted once.
Xinyan tweeted 10 times, followed 17 people and got 25 new followers.
Add the Twitter activity from the last 3 days to userProfiles

Convert the updated userProfiles python object back to a string in JSON format

Print the updated JSON string, sorted in alphabetical order, and in a human-readable format (hint: try indent=4).
"""
import json
userProfilesString = '{"profiles": \n{"Iman"\n\n: {"tweets": 450, "likes": 2500, "followers": 190, "following": 300},\n\n"Allan"\n\n: {"tweets": 200, "likes": 700, "followers": 150, "following": 100},\n\n"Xinyan"\n\n: {"tweets": 1135, "likes": 3000, "followers": 400, "following": 230},\n\n"Hao"\n\n: {"tweets": 645, "likes": 800, "followers": 300, "following": 500},\n"Harman"\n\n: {"tweets": 300, "likes": 1750, "followers": 200, "following": 400}}}'

userProfiles = json.loads(userProfilesString)

print("----original Data ------")

print(userProfiles)


print("\n-----Iman-------")
userProfiles['profiles']['Iman']['tweets'] = userProfiles['profiles']['Iman']['tweets']*5
userProfiles['profiles']['Iman']['likes'] = userProfiles['profiles']['Iman']['likes'] + 5
print(userProfiles['profiles']['Iman'])

print("-----Allan------")
userProfiles['profiles']['Allan']['tweets'] = userProfiles['profiles']['Allan']['tweets'] + 1
print(userProfiles['profiles']['Allan'])

print("\n-----Xinyan-----")
userProfiles['profiles']['Xinyan']['tweets'] = userProfiles['profiles']['Xinyan']['tweets'] *10
userProfiles['profiles']['Xinyan']['following'] = userProfiles['profiles']['Xinyan']['following'] + 17
userProfiles['profiles']['Xinyan']['followers'] = userProfiles['profiles']['Xinyan']['followers'] + 25

print(userProfiles['profiles']['Xinyan'])

print("\n----updated data after 3 days-----")
print(userProfiles)

userProfilesUpdatedString = json.dumps(userProfiles,sort_keys= True, indent = 4)
print(userProfilesUpdatedString)
