import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

translate = boto3.client(service_name='translate')


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

        response = translate.translate_text("hola", 
                SourceLanguageCode="es", TargetLanguageCode="en")

    elif language == "fr":    

        response = translate.translate_text("hola", 
                SourceLanguageCode="es", TargetLanguageCode="fr")
    
    # create a response
    

    return response
