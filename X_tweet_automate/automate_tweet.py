from requests_oauthlib import OAuth1Session
import json
import schedule
import time
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

# Your app credentials
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

# File to save/retrieve tokens
TOKEN_FILE = "access_tokens.json"

def get_saved_tokens():
    """Load access tokens from a file."""
    try:
        with open(TOKEN_FILE, "r") as f:
            tokens = json.load(f)
            return tokens["access_token"], tokens["access_token_secret"]
    except FileNotFoundError:
        return None, None

def save_tokens(access_token, access_token_secret):
    """Save access tokens to a file."""
    with open(TOKEN_FILE, "w") as f:
        json.dump({"access_token": access_token, "access_token_secret": access_token_secret}, f)

def authenticate():
    """Authenticate and return access tokens."""
    # Get request token
    request_token_url = "https://api.x.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
    fetch_response = oauth.fetch_request_token(request_token_url)

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")

    # Get authorization
    base_authorization_url = "https://api.x.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")

    # Get the access token
    access_token_url = "https://api.x.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Save tokens for future use
    save_tokens(access_token, access_token_secret)
    return access_token, access_token_secret

def post_tweet():
    """Post a tweet."""
    # Get saved tokens or authenticate
    access_token, access_token_secret = get_saved_tokens()
    if not access_token or not access_token_secret:
        print("No saved tokens found. Authenticating...")
        access_token, access_token_secret = authenticate()

    # Create OAuth1 session
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # Define the tweet
    payload = {"text": f"This is tweet posted on{datetime.datetime.now().isoformat()} "}

    # Post the tweet
    response = oauth.post(
        "https://api.x.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        print(
            f"Request returned an error: {response.status_code} {response.text}"
        )
    else:
        print("Tweet posted successfully!")
        print(json.dumps(response.json(), indent=4, sort_keys=True))

# Schedule the script to run every 3 hours
schedule.every(20).seconds.do(post_tweet)

# Keep the script running
print("Starting the tweet scheduler...")
while True:
    schedule.run_pending()
    time.sleep(1)

