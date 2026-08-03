#import flask, request object to parse the data, and jsonify object for python data
from flask import Flask, request, jsonify

#import uuid to make unique universal IDs
import uuid

#intialize flask instance, everything needed is in the program
app = Flask(__name__)

#store events in a dictionary while the service is running
local_db = {}

#app.route decorator to match functional requirement spec
@app.route('/calendar/events', methods=['POST'])
def create_event():

    #get_json parses the incoming JSON request data and returns it
    data = request.get_json()
    
    #assert that the data sent exists
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    #assert the required fields match functional requirement spec
    #Start time and end time, must be ISO8601 time format YYYY-MM-DDTHH:MM:SS
    required_fields = ['user_id', 'title', 'start_time', 'end_time']

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    #assert end time is not before the start time
    if data['end_time'] <= data['start_time']:
        return jsonify({"error": "End time must be later than start time"}), 400

    #generate universal unique ID ensure events with duplicate names times are still unique
    event_id = str(uuid.uuid4())

    #populate the event object
    new_event = {
        "event_id": event_id,
        "user_id": data['user_id'],
        "title": data['title'],
        "start_time": data['start_time'],
        "end_time": data['end_time'],
    }

    #assign the event to the uuid in the local_db
    local_db[event_id] = new_event

    #return the event and a 201 for status
    return jsonify(new_event), 201


#app.route decorator to match functional requirement spec
@app.route('/calendar/events/<string:event_id>', methods=['GET'])
def get_event(event_id):
    #provided a event_id return that event
    event = local_db.get(event_id)

    #return 404 if the event id is not found
    if not event:
        return jsonify("Event not found"), 404

    #return the event
    return jsonify(event),200


#app.route decorator to match functional requirement spec
@app.route('/calendar/events', methods=['GET'])
def list_events():

    #Start time and end time, must be ISO8601 time format YYYY-MM-DDTHH:MM:SS
    user_id = request.args.get('user_id')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    #assert end time is not before the start time
    if end_time <= start_time:
        return jsonify({"error": "End time must be later than start time"}), 400

    #matches will populate in the result array. no matches returns an empty array
    result_list =[]

    events = list(local_db.values())    

    for event in events:
        if user_id == event['user_id'] and start_time <= event['start_time'] and end_time >= event['end_time']:
            result_list.append(event)

    return jsonify(result_list), 200

if __name__ == '__main__':
    app.run(port=5002, debug=False)