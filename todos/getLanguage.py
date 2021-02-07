import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

translate = boto3.client(service_name='translate')

def getLanguage(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    language = event['pathParameters']['language']

    # fetch todo from the database hola
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
