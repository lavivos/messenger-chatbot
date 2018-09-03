from app_skeleton import _main
import random as rd
import json


def json_loader(path: str) -> dict:
    return json.load(open(path, 'r', encoding='utf-8'))


def get_message(text):
    data = json_loader('./src/data.json')
    scores_list = update_scores(text)
    max_score = max(scores_list[1])
    highly_scored_list = [scores_list[0][i] for i in range(len(scores_list[0])) if scores_list[1][i] == max_score]
    if len(highly_scored_list) == 1 and highly_scored_list[0] != "citation":
        message = rd.choice(data["greeting"]["responses"])
        return {"message": message, "has_buttons": False}
    else:
        buttons = []
        for writer in data["citation"]["responses"]:
            buttons.append({
                "type": "postback",
                "title": writer,
                "payload": writer
            })
        return {"message": 'Vous voulez une citation de quel auteur : ', "has_buttons": True, "buttons": buttons}


def update_scores(text):
    data = json_loader('./src/data.json')
    word_list = text.split()
    scores = dict()
    for key in data:
        scores[key] = 0
    for word in word_list:
        for key in data:
            if word in data[key]["keywords"]:
                scores[key] += 1
    keys = list(data.keys())
    values = [scores[key] for key in keys]
    return [keys, values]


def get_quote(writer):
    data = json_loader('./src/data.json')
    return data["citation"]["responses"][writer]


def onInit():
    _main()
