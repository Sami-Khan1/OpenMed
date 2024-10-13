import boto3
import json

def bedrock_handler(event, context):
    AWS_ACCESS_KEY_ID  = "AKIAZQ3DTB7NELOHTCMK"
    AWS_SECRET_KEY_ID  = "f9vZqcpQB4X6MIGfIInxfp7IMlV1w05ySsXotwCm"
    AWS_DEFAULT_REGION = "us-west-2"
    bedrock = boto3.client(service_name='bedrock-runtime')
    system_prompts = [{"text": "Be as helpful as possible with your given prompt."}]
    
    user_input = event.get('text', '')
    user_prompt = [{
        "role": "user",
        "content": [{"text": user_input}]  # Content is a list of dicts with 'text' key
    }]

    if not user_prompt:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No text provided'})
        }
    
    try:
        # Call model via Bedrock 
        response = bedrock.converse(
            modelId = 'meta.llama3-1-405b-instruct-v1:0',
            messages = user_prompt,
            system = system_prompts
        )
        return response
        

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

