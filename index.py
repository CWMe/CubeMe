import json
import datetime

def handler(event, context):
    # Python program to run a Cube Function
    body = json.loads(event['body'])
    number_to_cube = body['number_to_cube']
    # check if the number is negative, positive or zero
    if number_to_cube < 0:
        print("Sorry, cube does not exist for negative numbers")
    elif number_to_cube == 0:
        print("The cube of 0 is 0")
    elif number_to_cube > 9000:
        print("Scouter says its over 9000")
    else:
        num_cubed = number_to_cube ** 3
        print("The cube of ", number_to_cube, "is", num_cubed)

    data = {
        'output': 'The cube of ' + num + ' is ' + num_cubed ,
        'timestamp': datetime.datetime.utcnow().isoformat()

    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
