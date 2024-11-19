# Twitter Posting: Automation Script

This script allows users to automate posting tweets to Twitter (X) every x number of hrs/min/sec. To get started, you need to set up a Twitter Developer account and obtain your **Consumer Key** and **Consumer Secret**.

---

## How to Get Your Twitter API Keys

Follow these steps to get your **Consumer Key** and **Consumer Secret**:

### Step 1: Create a Twitter Developer Account
1. Go to the [Twitter Developer Portal](https://developer.twitter.com/).
2. Log in with your Twitter account.
3. Apply for a developer account (if you don’t already have one):
   - Click on **Apply** and follow the instructions.
   - Provide the required details about how you intend to use the API.
   - Wait for approval (this usually takes a few minutes to a day).

---

### Step 2: Create a Twitter App
1. Once your developer account is approved, go to the [Twitter Developer Dashboard](https://developer.twitter.com/en/apps).
2. Click on the **Create an App** button.
3. Fill in the app details:
   - **App Name**: Choose a name for your app (e.g., "My Tweet Bot").
   - **App Description**: Describe the purpose of your app.
   - **Website URL**: Provide a valid URL (you can use `https://example.com` if you don’t have one).
   - **Callback URL**: Use `oob` (Out-of-Band) if you don’t need a web app integration.

---

### Step 3: Generate API Keys
1. After creating the app, go to the **Keys and Tokens** section.
2. Under **API Key and Secret**, click **Generate** to get your:
   - **API Key (Consumer Key)**.
   - **API Secret Key (Consumer Secret)**.
3. Copy these keys and save them securely. You will need them for the script.

---


## Setting Up the Script

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/devams23/automation_scripts_python.git
   cd automation_scripts_python
   
2. Make a .env file having keys mentioned in the .env.sample file and paste the consumer key and secret which you saved it earlier.

3. Install the required Python libraries:
   ```bash
   pip install -r requirements. txt
   cd X_tweet_automate
   
4. Run the script:
   ```bash
   python automate_tweet.py
