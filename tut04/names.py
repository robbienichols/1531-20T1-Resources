import math
import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

names = []

def dateToAge(timestamp):
    '''This function takes the number of seconds as a timestamp, 
    and uses this to find the persons age in years

    Parameters:
        - timestamp int: the unix style timestamp. Seconds since Jan 1, 1970.
    Returns:
        - age int: the number of years the person has been alive.
    '''
    # generate a datetime object from a timestamp
    dt = datetime.datetime.fromtimestamp(timestamp)
    # generate a datetime object for the current time
    now = datetime.datetime.now()
    # Take the difference between them
    diff = now - dt
    # Convert days to the number of years to get the age
    return math.floor(diff.days / 365)

@app.route('/addname', methods=['POST'])
def addname():
    global names 
    # how we get the json from the request coming from the frontend
    # allows us to index into 'data' like a dictionary
    data = request.get_json()  
    # add the new dictionary into the 'names' list
    names.append({
        'name': data['name'],
        'age': dateToAge(int(data['dob']))
    })
    # return empty dictionary to mark success
    return {}

@app.route('/getnames', methods=['GET'])
def getnames():
    # return the list of dictionaries in json format to the frontend
    return jsonify(names)

if __name__ == '__main__':
    app.run()
