import requests
import json

def emotion_detector(text_to_analyze):
    # URL y headers del servicio de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Formato del JSON de entrada
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Enviar la solicitud POST
    response = requests.post(url, json=input_json, headers=headers)
    
    # 1. Convertir el texto de la respuesta en un diccionario usando la librería json
    response_dict = json.loads(response.text)
    
    # 2. Extraer los puntajes de las emociones de la estructura de respuesta de Watson
    scores = response_dict['emotionPredictions'][0]['emotion']['scores']
    
    # 3. Encontrar la emoción dominante (la clave con el valor más alto en el diccionario 'scores')
    dominant_emotion = max(scores, key=scores.get)
    
    # 4. Retornar el diccionario con el formato exacto solicitado
    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant_emotion
    }