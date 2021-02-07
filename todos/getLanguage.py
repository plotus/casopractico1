import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

translate = boto3.client(service_name='translate', region_name='region', use_ssl=True)


def getLanguage(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    text = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    #Una vez tenemos el resultado llamaremos al endpoint que traduce

    language =  event['pathParameters']['language']

    if language == "en":

        result = translate.translate_text(text['Item'], 
                SourceLanguageCode="es", TargetLanguageCode="en")

    elif language == "fr":    

        result = translate.translate_text(text['Item'], 
                SourceLanguageCode="es", TargetLanguageCode="fr")
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result.get('TranslatedText'),
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
