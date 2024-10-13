from bedrock import bedrock_handler
from compMed import lambda_handler
import boto3
import json


def giveEvent (event, context):
    # Call the lambda_handler function directly
    response = lambda_handler(event, None)
    response2 = bedrock_handler({'text' : 'Turn the following information extracted into a JSON into a summary with specific possible diagnoses and convey it in some actionable form to the patient without using overly technical jargon. Make sure it is informal, not a bulleted list and very very concise. If diagnoses are low probability, say so. Do not explicitly say anything like "Here is a concise summary of your symptoms and diagnoses," just tell them. Take your time, take a deep breath. ' + str(response)}, None)
    # Assuming response2 contains the JSON data
    text = response2['output']['message']['content'][0]['text']
    result = {
        'text' : text
    }
    
    #test
'''if __name__ == '__main__':
    test_event = {
        'text': 'I am going through X medical condition.'
    }
    response = lambda_handler(test_event, None)
    response2 = bedrock_handler({'text' : 'Turn the following information extracted into a JSON into a summary with specific possible diagnoses and convey it in some actionable form to the patient without using overly technical jargon. Make sure it is informal, not a bulleted list and very very concise. If diagnoses are low probability, say so. Do not explicitly say anything like "Here is a concise summary of your symptoms and diagnoses," just tell them. Take your time, take a deep breath. ' + str(response)}, None)
    # Print the response
    # Assuming response2 contains the JSON data
    text = response2['output']['message']['content'][0]['text']
    print(text)'''