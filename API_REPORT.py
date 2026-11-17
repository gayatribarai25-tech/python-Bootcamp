import requests
import json

# 1. Get all users and print the count
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print("Users:", len(users))


# 2. Get posts of user 1 using query parameters
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
posts = response.json()
print("Posts by user 1:", len(posts))


# 3. POST a new post
new_post = {
    "title": "HTTP report",
    "body": "Done",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
created_post = response.json()
created_post_id = created_post["id"]
print("Created:", response.status_code, created_post_id)


# 4. Request /users/99 with raise_for_status and print User 99 not found on an error; then save a report dictionary (users, posts_by_user_1, created_post_id) to report.json and print it
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/99"
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("User 99 not found")


# Create report dictionary
report = {
    "users": len(users),
    "posts_by_user_1": len(posts),
    "created_post_id": created_post_id
}
#Save report dictionary to report.json
with open("report.json", "w") as file:
    json.dump(report, file, indent=4)
print(report)
