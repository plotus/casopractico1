import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

translate = boto3.client(service_name='translate')

def getLanguage(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    language = event['pathParameters']['language']

    # fetch todo from the database holad
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    texto = result['text']

    response = result['text']

    if language == "en":

        response = translate.translate_text(Text="hola", 
                SourceLanguageCode="es", TargetLanguageCode="en")

    elif language == "fr":    

        response = translate.translate_text(Text=texto, 
                SourceLanguageCode="es", TargetLanguageCode="fr")

    # create a responseff
    response = {
        "statusCode": 200,
        "body": json.dumps(response,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
