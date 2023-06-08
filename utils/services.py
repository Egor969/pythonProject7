import json
from datetime import datetime


def load_json(filename: str) -> list[dict, ...]:

    with open(filename, 'r', encoding="utf8") as f:
        json_dict = json.load(f)
    return json_dict

def date_format(data_str: str, formatted_date: str = '%d.%m.%Y %H:%M:%S'):
    parsed = datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%S:%f')
    formatted_date = parsed.strftime(formatted_date)
    return formatted_date

def get_last_five_successful_operations(sort_list: list) -> list:
    successful_operations = [op for op in sort_list if op["state"] == "EXECUTED"]
    last_five_successful_operations = successful_operations[:5]
    return last_five_successful_operations


def sort_by_date(json_dict=None):
    sort_list = sorted(json_dict, key=lambda x: x.get("date"), reverse=True)
    return sort_list

def mask_card(operation_credintials: str) -> str:

    if operation_credintials:

        credintials_name = " ".join(operation_credintials.split(" ")[:-1])

        credintials_number = operation_credintials.split(" ")[:-1]

        if len(credintials_number) == 16:

            number_hide = credintials_number[:6] + "*" * 6 + credintials_number[:-4]

            number_sep = [number_hide[i:i + 4] for i in range(0, len(credintials_number), 4)]

            return f'{credintials_name} {" ".join(number_sep)}'

        elif len(credintials_number) == 20:

            return f'{credintials_name} {credintials_number.replace(credintials_number[:-4], "**")}'


    return "N/A"


def print_info(operations):
    for op in operations:
        print(f"{date_format(op['date'])} {op['description']}\n"
              f"{mask_card(op.get('from'))} -> {mask_card(op.get('to'))}\n")