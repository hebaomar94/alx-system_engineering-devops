#!/usr/bin/python3
"""
returns the total number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Function to query subscribers on a given Reddit subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
