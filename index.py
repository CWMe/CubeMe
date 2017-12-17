import json
import datetime

def handler(event, context):
    # Python program to run a Cube Function
    body = json.loads(event['body'])
    number_to_cube = body['number_to_cube']
    # check if the number is negative, positive or zero
    if number_to_cube < 0:
        return respond(ValueError("Sorry, cube does not exist for negative numbers"))
    elif number_to_cube == 0:
        return respond(None, create_response(0,0))
    elif number_to_cube > 9000:
        return respond(ValueError("Scouter says its over 9000. Too High"))
    else:
        num_cubed = number_to_cube ** 3
        return respond(None, create_response(number_to_cube,num_cubed))

def respond (err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {'Content-Type': 'application/json'}
    }

def create_response (number_to_cube, num_cubed) :
    data = {
        'output': 'The cube of ' + number_to_cube + ' is ' + str(num_cubed),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }