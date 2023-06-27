import uuid
import os
import openai
import json

# initialize the OpenAI API client
openai.api_key = os.getenv("GPTAPIKEY")

def handler(event, context):
    print('received event:')
    print(event)

    # Start the game
    prompt = """
    The player begins their adventure at the bottom of a multi-level cave. Their goal is to escape through the top, collecting as much treasure as possible along the way. 
    Each turn, the player can either loot the current level or grapple up to the next one, using a total of three actions. 
    Lingering on a level for more than three actions causes a mysterious fog to appear, slowly crawling up from below. 
    If the player is inside the fog, they have a 50% chance of losing the game with each action until they ascend to the next level.
    As the AI, you'll guide and narrate their journey through a web browser interface, responding to their text prompts with your own messages. 
    Now, begin the game with a three-sentence introduction that sets the scene and instructs the player on their first possible actions.
    """
    
    try:
        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
          ]
        )

        generated_message = completion.choices[0].message['content']
        print(generated_message)
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'message': generated_message,
                'gameId': str(uuid.uuid4())  # generate a new UUID each time the function is called
            })
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'message': 'An error occurred',
                'error': str(e)
            })
        }
