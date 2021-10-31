import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    tableMensagens = dynamodb.Table('MensagensChat')

    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    remetente = str(event['from'])
    destinatario = str(event['to'])
    mensagem = str(event['msg'])

    try:
        tableMensagens.put_item(
            Item={
                'data_hora': data_hora,
                'remetente': remetente,
                'destinatario': destinatario,
                'mensagem': mensagem
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Mensagem inserida no Banco de Dados!')
        }
    except:
        print('Erro: lambda function terminada sem sucesso')
        return {
                'statusCode': 400,
                'body': json.dumps('Erro ao tentar processar mensagem')
        }