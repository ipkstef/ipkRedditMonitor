import praw
import requests

# Reddit credentials
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Discord webhook URL
webhook_url = 'your_webhook_url'

# Subreddit to monitor
subreddit_name = 'your_subreddit_name'

# Function to send the new post data to the Discord webhook
def send_to_discord(title, image_url):
    # Form the payload for the Discord webhook
    payload = {
        "username": "Subreddit Monitor",
        "avatar_url": "https://i.imgur.com/dKsdT9r.png",
        "embeds": [
            {
                "title": title,
                "image": {
                    "url": image_url
                }
            }
        ]
    }

    # Send the HTTP POST request to the Discord webhook
    response = requests.post(webhook_url, json=payload)

    # Check the response status code
    if response.status_code != 200:
        print(f'Error sending message to Discord: {response.status_code} - {response.reason}')
    else:
        print(f'Successfully sent message to Discord')

# Get the subreddit object
subreddit = reddit.subreddit(subreddit_name)

# Monitor the subreddit for new posts
while True:
    # Get the latest post from the subreddit
    submission = subreddit.new(limit=1)

    # Check if the post is a new one
    if submission.created_utc > time.time() - 60:
        # Get the post title and image URL
        title = submission.title
        image_url = submission.url

        # Send the post data to the Discord webhook
        send_to_discord(title, image_url)
