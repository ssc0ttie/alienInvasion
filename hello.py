##CAPTURING ALL ACTIVITIES IN STRAVA
# THIS UTILIZES STRAVA API
# LAST UPDATED 22-SEPT-2023

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    "client_id": "109430",
    "client_secret": "9f9bba1f50148b0b7a4996fe4d1e89a300aaeff5",
    "refresh_token": "60918cffb119360a53f6fa56701db6c9581cfd28",
    "grant_type": "refresh_token",
    "f": "json",
}


##THE REFRESH TOKEN IS FROM THE POST REQUEST##
##https://www.strava.com/oauth/token?client_id=109430&client_secret=9f9bba1f50148b0b7a4996fe4d1e89a300aaeff5&code=bf81d56e5a81ee7f6f42d8dddbe2fca99c359de3&grant_type=authorization_code


print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)

print(res.text)
print(res.status_code)


access_token = res.json()["access_token"]


print("Access Token = {}\n".format(access_token))

header = {"Authorization": "Bearer " + access_token}

# The first loop, request_page_number will be set to one, so it requests the first page. Increment this number after
# each request, so the next time we request the second page, then third, and so on...

request_page_num = 1
all_activities = []
my_dataset = []

while True:
    param = {"per_page": 200, "page": request_page_num}
    # initial request, where we request the first page of activities

    try:
        my_dataset = requests.get(activites_url, headers=header, params=param).json()
        print(my_dataset)

    except ValueError:
        print("Error occurred while parsing API response.")
        break

    # check the response to make sure it is not empty. If it is empty, that means there is no more data left. So if you have
    # 1000 activities, on the 6th request, where we request page 6, there would be no more data left, so we will break out of the loop

    if len(my_dataset) == 0:
        print(
            "breaking out of while loop because the response is zero, which means there must be no more activities"
        )
        break

    # if the all_activities list is already populated, that means we want to add additional data to it via extend.
    if isinstance(my_dataset, list):
        if all_activities:
            print("all_activities is populated")
            all_activities.extend(my_dataset)

        # if the all_activities is empty, this is the first time adding data so we just set it equal to my_dataset
        else:
            print("all_activities is NOT populated")
            all_activities = my_dataset

        request_page_num += 1
    else:
        print("my_dataset is not a list. Skipping this response.")
