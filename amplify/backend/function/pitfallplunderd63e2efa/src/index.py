import os
import openai
import json

# initialize the OpenAI API client
openai.api_key = os.getenv("GPTAPIKEY")

def handler(event, context):
    print('received event:')
    print(event)

    # extract the user input from the event
    user_input = event['body']

    # call the OpenAI API
    response = openai.Completion.create(
      engine="text-davinci-004",
      prompt=user_input,
      max_tokens=150
    )

    # extract the AI's response from the response
    ai_response = response.choices[0].text.strip()

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(ai_response)  # return the AI's response
    }