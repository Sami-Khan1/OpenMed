import boto3
import json

def bedrock_handler(event, context):

    AWS_ACCESS_KEY_ID  = "AKIAZQ3DTB7NELOHTCMK"
    AWS_SECRET_KEY_ID  = "f9vZqcpQB4X6MIGfIInxfp7IMlV1w05ySsXotwCm"
    AWS_DEFAULT_REGION = "us-west-2"

    
    user_prompt = event.get('text', '')

    if not user_prompt:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No text provided'})
        }
    
    try:
        # Call Claude 3.5 via Bedrock
        response = bedrock.invoke_model(
            modelId='anthropic.claude-3-sonnet-20240229-v1:0',  # or claude-v2 if that's your model version
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                "prompt": user_prompt,  # Input prompt for Claude
                "max_tokens": 500       # Limit on the response size
            })
        )
        
        # Extract the generated text from the response
        response_body = json.loads(response['body'])
        generated_text = response_body['completions'][0]['data']['text']

        return {
            'statusCode': 200,
            'body': json.dumps({'response': generated_text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }