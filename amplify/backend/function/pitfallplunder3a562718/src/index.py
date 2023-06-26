import json
import uuid

#Start Game

def handler(event, context):
  print('received event:')
  print(event)
  
  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps({
        'message': 'Welcome to the game!',
        'gameId': str(uuid.uuid4())  # generate a new UUID each time the function is called
      })
  }