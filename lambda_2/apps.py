import boto3
import json
from datetime import datetime


def lambda_handler(event, context):
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    dt = datetime.now()
    res = client.get_object(Bucket='bucketfincaraiz',
                            Key="landing-casas-"+str(dt.date())+'.html')
    res_dec = res['Body'].read().decode('utf-8')
    results = json.loads(res_dec)
    csv = "FechaDescarga,Barrio,Valor,NumHabitaciones,NumBanos,mts2\n"
    for house in results['hits']['hits']:
        mt2 = house['_source']['listing']['area']
        price = house['_source']['listing']['price']
        barrio = (house['_source']['listing']['locations']
                       ['neighbourhoods'][0]['name'])
        nhabs = house['_source']['listing']['rooms']['id']
        nbath = house['_source']['listing']['baths']['id']
        csv += str(dt.date())+","+str(barrio)+","+str(price)+","+str(nhabs)\
            + ","+str(nbath)+","+str(mt2)+"\n"

    s3 = boto3.resource('s3')
    s3.Object('zappa-tmtvhlyzs',
              "casas-final-"+str(dt.date())+'.csv').put(Body=csv)
