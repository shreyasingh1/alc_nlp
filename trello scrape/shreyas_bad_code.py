import json
import csv
import pandas as pd

def read_json(file_name = 'test.json'):
    with open(file_name) as f:
        data = json.load(f)
    return data


def to_dict_actions(data):
    c = []

    for action in data['actions']:
        # card
        if "card" in action['data'].keys():
            if "name" in action['data']['card'].keys():
                card = action['data']['card']['name']
            else:
                card = "NO NAME"
        else:
            card = "NO CARD"
        # text
        if "text" in action['data'].keys():
            text = action['data']['text']
        else:
            text = "NO TEXT"
        # board
        if "board" in action['data'].keys():
            board = action['data']['board']['name']
        else:
            board = "NO BOARD"
        # list
        if "list" in action['data'].keys():
            list = action['data']['list']['name']
        elif "listAfter" in action['data'].keys():
            list = action['data']['listAfter']['name']
        else:
            list = 'NO LIST'
        # info about the action
        type = action['type']
        data = action['date']
        name = action['memberCreator']['fullName']

        x =  {"card" : card, "text" : text, "board": board, "list": list, "type": type, "data": data, "name": name}

        c.append(x)

    return c

def to_dict_card(data):
    c = []
    for card in data['cards']:
        if "desc" in card.keys():
            desc = card['desc']
        else:
            desc = "NO DESC"

        if "name" in card.keys():
            name = card['name']
        else:
            name = 'NO NAME'

        if "dateLastActivity" in card.keys():
            date = card['dateLastActivity']
        else:
            date = "NO DATE"

        x = {"name" : name, "desc": desc, 'date': date}
        c.append(x)

    return c

def to_dict_members(data):
    c = []
    for member in data['members']:
        if 'fullName' in member.keys():
            name = member['fullName']
        else:
            name = "NO NAME"

        if 'username' in member.keys():
            username = member['username']
        else:
            username = "NO USERNAME"


        x = {"name": name, "username": username}
        c.append(x)

    return c

data = read_json()

actions = to_dict_actions(data)
actions_df = pd.DataFrame(actions)
actions_df.to_csv("trello_actions.csv")

cards = to_dict_card(data)
cards_df = pd.DataFrame(cards)
cards_df.to_csv("trello_cards.csv")

members = to_dict_members(data)
members_df = pd.DataFrame(members)
members_df.to_csv("trello_members.csv")
