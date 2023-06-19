import json


def get_json(json_file):
    """"""
    with open(json_file, 'r', encoding="utf-8") as file:
        list_operations = json.load(file)

        return list_operations


def get_list_complited(list_operations):
    list_complited = []
    for dictionary in list_operations:
        if "state" in dictionary:
            if "from" in dictionary:
                if len(dictionary["from"]) != 0:
                    if "EXECUTED" in dictionary.values():
                        list_complited.append(dictionary)

    return list_complited


def refactoring_date(date_, i):
    return str(date_[i].date[8:10]) + '.' + str(date_[i].date[5:7]) + '.' + str(date_[i].date[:4])


def hide_numbers(count):
    if "Счет" in count:
        return count[:-20] + '**' + count[-4:]
    else:
        return count[:-16] + count[-16:-12] + ' ' + count[-12:-10] + '** **** ' + count[-4:]
