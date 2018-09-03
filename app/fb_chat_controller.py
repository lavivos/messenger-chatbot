import os

from flask import request
from app.main_service import get_message, get_quote, onInit
from app.bot_service import get_bot

onInit()


def handle_verification():
    token_sent = request.args.get("hub.verify_token")
    return verify_fb_token(token_sent)


def handle_message():
    try:
        output: dict = request.get_json()
        message: dict = output['entry'][0]['messaging'][0]
        handle_current_msg(message)
        handle_postback_msg(message)
        return "Succès"
    except:
        return 'Nous rencontrons un problème à recevoir votre message'


def handle_current_msg(message: dict):
    if message.get('message'):
        recipient_id: str = message['sender']['id']
        if message['message'].get('text'):
            text: str = message['message'].get('text')
            output_msg = get_message(text)
            if output_msg["has_buttons"]:
                send_message_with_buttons(recipient_id, output_msg["message"], output_msg["buttons"])
            else:
                send_message(recipient_id, output_msg["message"])
    return "Succès"


def handle_postback_msg(message: dict):
    if message.get('postback'):
        recipient_id = message['sender']['id']
        if message['postback'].get('payload'):
            text = message['postback'].get('payload')
            send_message(recipient_id, get_quote(text))
    return 'Succès'


def verify_fb_token(token_sent: str):
    if token_sent == os.getenv('VERIFY_TOKEN'):
        return request.args.get("hub.challenge")
    return 'le token de validation est incorrect'


def send_message(recipient_id: str, response: str):
    bot = get_bot()
    bot.send_text_message(recipient_id, response)
    return 'réalisation avec succès'


def send_message_with_buttons(recipient_id: str, response: str, buttons: list):
    bot = get_bot()
    bot.send_button_message(recipient_id, response, buttons)
    return 'réalisation avec succès'
