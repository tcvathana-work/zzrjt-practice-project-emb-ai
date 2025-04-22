'''
This module contains a function to analyze the sentiment of a given text using the Watson NLP API.
'''
import requests
import jsons

def sentiment_analyzer(text_to_analyze):
    '''
    Analyzes the sentiment of the given text using the Watson NLP API.
    '''
    base_url = 'https://sn-watson-sentiment-bert.labs.skills.network'
    url = f'{base_url}/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = { "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock" }
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = body, timeout = 10)

    formatted_response = jsons.loads(response.text)

    label = None
    score = None
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}
