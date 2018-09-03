from flask import Flask

from app.fb_chat_controller import handle_message, handle_verification

main = Flask(__name__)


@main.route("/", methods=['GET'])
def token_verification():
    return handle_verification()


@main.route("/", methods=['POST'])
def returnOutputMessage():
    return handle_message()


if __name__ == '__main__':
    main.run(debug=True)
