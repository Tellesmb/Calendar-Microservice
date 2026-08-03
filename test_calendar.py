import requests

print("PROGRAM TO TEST calendar_service.py")

#server is running at this url
url = "http://127.0.0.1:5002/calendar/events"

print("This test will send requests to: ", url)


event_id_list = []



print("--- CREATE_EVENT ---------------------------------------------------------------")
print("")
print("--- Creating first JSON payload ---")
payload = {
    "user_id": "user1",
    "title": "study",
    "start_time": "2026-06-01T14:00:00",
    "end_time": "2026-06-01T15:00:00",
}

response = requests.post(url, json=payload)

#print the status 201
print("Response status is: ", response.status_code)

#store the unique event_id
created_event= response.json()
event_id = created_event["event_id"]
event_id_list.append(event_id)

#print the event_id just to show / validate
print("The unique event_id is: ", event_id)





print("")
print("--- Creating 2nd JSON payload ---")
payload = {
    "user_id": "user2",
    "title": "party",
    "start_time": "2026-06-02T13:00:00",
    "end_time": "2026-06-03T00:00:00",
}

response = requests.post(url, json=payload)

#print the status 201
print("Response status is: ", response.status_code)

#store the unique event_id
created_event= response.json()
event_id = created_event["event_id"]
event_id_list.append(event_id)

#print the event_id just to show / validate
print("The unique event_id is: ", event_id)





print("")
print("--- Creating 3rd JSON payload ---")
payload = {
    "user_id": "user1",
    "title": "dinner",
    "start_time": "2026-06-01T16:00:00",
    "end_time": "2026-06-01T17:00:00",
}

response = requests.post(url, json=payload)

#print the status 201
print("Response status is: ", response.status_code)

#store the unique event_id
created_event= response.json()
event_id = created_event["event_id"]
event_id_list.append(event_id)

#print the event_id just to show / validate
print("The unique event_id is: ", event_id)


print("")
print("--- Creating a BAD JSON payload ---")
payload = {
    "user_id": "user2",
    "title": "impossible",
    "start_time": "2026-06-01T17:00:00",
    "end_time": "2026-06-01T16:00:00",
}

response = requests.post(url, json=payload)

#print the status 201
print("Response status is: ", response.status_code)





print("")
print("")
print("")
print("--- GET_EVENT ------------------------------------------------------------------")

print("")
print("--- Successful GET Event 1 ---")
#GET the the event by using the unique event id as stored in event_id_list
get_response = requests.get(url + "/" + event_id_list[0])
print("Event: ", get_response.json())
print("Response status is: ", response.status_code)




print("")
print("--- Successful GET Event 2 ---")
#GET the the event by using the unique event id as stored in event_id_list
get_response = requests.get(url + "/" + event_id_list[1])
print("Event: ", get_response.json())
print("Response status is: ", response.status_code)



print("")
print(" --- Successful GET Event 3 --- ")
#GET the the event by using the unique event id as stored in event_id_list
get_response = requests.get(url + "/" + event_id_list[2])
print("Event: ", get_response.json())
print("Response status is: ", response.status_code)



print("")
print(" --- Fail to GET --- ")
#Failure case
get_response = requests.get(url + "/" + "bad_id")
print("Event: ", get_response.json())
print("Response status is: ", response.status_code)



print("")
print("")
print("")
print("--- LIST_EVENT -----------------------------------------------------------------")

print("Creating params for GET")
payload = {
    "user_id": "user1",
    "start_time": "2026-06-01T012:00:00",
    "end_time": "2026-06-01T18:00:00"
}


get_response = requests.get(url, params=payload)

print("")
print("List of events: ", get_response.json())
print("Response status is: ", get_response.status_code)
