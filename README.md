# Using the App Store Reviews Fetcher Script

## Introduction
This document provides a comprehensive guide on how to use the App Store Reviews Fetcher Script. This Python script is designed to interact with the App Store Connect API to fetch customer reviews for a specific app, sort them by creation date, and save them to a CSV file.

## Prerequisites
Before using the script, ensure you have the following:
1. **Python Environment**: Python 3.x installed on your system.
2. **Required Libraries**: `requests` and `jwt` libraries installed. You can install these via pip:
   ```
   pip install requests PyJWT
   ```
3. **API Key from App Store Connect**: You must have an API key (`key_id` and `issuer_id`) and the associated private key file (`.p8` file).

## Setup
1. **Locate the Script**: Ensure the script is saved in a known directory.
2. **Private Key File**: Place the `.p8` private key file in the same directory as the script or update the `private_key_path` in the script to point to its location.

## Configuration
Modify the following variables in the script according to your needs:
- `key_id`: Your API Key ID from App Store Connect.
- `issuer_id`: Your Issuer ID from App Store Connect.
- `private_key_path`: Path to your `.p8` private key file.
- `app_id`: Add the App ID for which you want to fetch reviews.

## Running the Script
Execute the script by running the following command in the terminal or command prompt:
```
python3 ./export_script.py
```

## Output
The script will perform the following actions:
1. **Authenticate with App Store Connect API**: Using the provided API key and private key.
2. **Fetch Reviews**: Retrieve customer reviews for the specified app.
3. **Sort Reviews**: Sort the reviews by creation date in descending order.
4. **Save to CSV**: Output the reviews into a `reviews.csv` file in the same directory as the script. The CSV file includes columns for review number, ID, rating, title, body, reviewer nickname, creation date, and territory.

## Troubleshooting
- **Authentication Errors**: Ensure your API key, issuer ID, and private key file are correct and valid.
- **Library Not Found**: Make sure `requests` and `PyJWT` libraries are installed.
- **File Path Issues**: Verify the path to the private key file and the output CSV file.

## Conclusion
This script is a useful tool for developers and marketers to analyze customer feedback for their apps available on the App Store. By automating the process of fetching and sorting reviews, it saves time and provides valuable insights in a convenient format.

## Disclaimer
This script uses API keys and sensitive information. Ensure to keep this data secure and use the script responsibly according to the terms and conditions of the App Store Connect API.
