#!/usr/bin/python3
"""
queries the reddit api and prints the titles of posts
"""
import requests


def top_ten(subreddit):
    """function that returns the top ten posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()["data"]["children"]
    for post in data:
        print(post["data"]["title"])
