import requests
import jwt
import time
import csv
from datetime import datetime

# Appstore Connect API Key details for authentication
key_id = 'YOUR_KEY_ID'
issuer_id = 'YOUR_ISSUER_ID'
private_key_path = './private.p8'

# Loading the private key from a file
with open(private_key_path, 'r') as key_file:
    private_key = key_file.read()

# Preparing to generate a JWT token
algorithm = 'ES256'
header = {
    "alg": algorithm,
    "kid": key_id,
    "typ": "JWT"
}

payload = {
    'iss': issuer_id,
    'exp': int(time.time()) + 1200,  # Token expiry set to 20 minutes from now
    'aud': 'appstoreconnect-v1'
}

# Generating the JWT token
token = jwt.encode(payload, private_key, algorithm=algorithm, headers=header)

# Defining the base URL for the API request
base_url = f'https://api.appstoreconnect.apple.com/v1/apps/375539359/customerReviews?limit=200'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

all_reviews = []

# Fetching the first page of reviews
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    data = response.json()
    all_reviews.extend(data['data'])

    # Handling pagination, limited to 1000 pages
    page_counter = 1
    while 'next' in data['links'] and page_counter < 1000:
        next_url = data['links']['next']
        response = requests.get(next_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            all_reviews.extend(data['data'])
            page_counter += 1
        else:
            print(f"Error {response.status_code}: {response.text}")
            break
else:
    print(f"Error {response.status_code}: {response.text}")

# Sorting reviews by creation date in descending order
all_reviews.sort(key=lambda x: datetime.strptime(x['attributes']['createdDate'], "%Y-%m-%dT%H:%M:%S%z"), reverse=True)

# Saving the reviews to a CSV file
with open('reviews.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Writing the CSV header
    writer.writerow(["Number", "ID", "Rating", "Title", "Body", "Reviewer Nickname", "Created Date", "Territory"])

    # Writing each review as a row in the CSV
    for index, review in enumerate(all_reviews, 1):
        review_id = review['id']
        rating = review['attributes']['rating']
        title = review['attributes']['title']
        body = review['attributes']['body']
        reviewer_nickname = review['attributes']['reviewerNickname']
        created_date = review['attributes']['createdDate']
        territory = review['attributes']['territory']

        writer.writerow([index, review_id, rating, title, body, reviewer_nickname, created_date, territory])
