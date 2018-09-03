from pymessenger import Bot
from flask import Flask, request

initial_main = Flask(__name__)

ACCESS_TOKEN = "EAAMkKKXDGTcBALe8zej7FKW3B7MtFfFprF08GgK0Rzkr3dWalkDmTm6WI5K5QoZAW3HTz48pKqtf6Yacq7t6464ty8F7e1wIVn14z5fvuYFsVqP8cpNygLBeZAE5QmttZAY1gxLwDKL6d2pSlbkIVRE8SikooR2up7b4rTnWAZDZD"
VERIFY_TOKEN = "123456"


@initial_main.route("/", methods=['GET'])
def handle_verification():
    token_sent = request.args.get("hub.verify_token")
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'le token de validation est incorrect'


@initial_main.route("/", methods=['POST'])
def returnOutputMessage():
    try:
        output: dict = request.get_json()
        message: dict = output['entry'][0]['messaging'][0]
        if message.get('message'):
            recipient_id: str = message['sender']['id']
            if message['message'].get('text'):
                text: str = message['message'].get('text')
                output_msg = text
                bot = Bot(ACCESS_TOKEN)
                bot.send_text_message(recipient_id, output_msg)
        return 'réalisation avec succès'
    except:
        return 'Nous rencontrons un problème à recevoir votre message'


if __name__ == '__main__':
    initial_main.run(debug=True)
