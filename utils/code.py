import json


def get_json(json_file):
    """чтение файла jason  """
    with open(json_file, 'r', encoding="utf-8") as file:
        list_operations = json.load(file)

        return list_operations


def get_list_complited(list_operations):
    """отсортировывает по наличию, отсутствию
    ключей, значений список словарей """
    list_complited = []
    for dictionary in list_operations:
        if "state" in dictionary:
            if "EXECUTED" in dictionary.values():
                if "from" in dictionary:

                    list_complited.append(dictionary)
                # если отсутсвует ключ "from" добавляет его  с пустым строковым значением
                elif "from" not in dictionary.keys():
                    dictionary["from"] = ''
                    list_complited.append(dictionary)

    return list_complited


def refactoring_date(date_, i):
    """получает по индексу(i) списка значение поля(date) класса  и отдает отфарматированную строку """
    return str(date_[i].date[8:10]) + '.' + str(date_[i].date[5:7]) + '.' + str(date_[i].date[:4])


def refactoring_transaction(count):
    """форматирует описание типа перевода"""
    if "Счет" in count:
        return str(count[:-20] + '**' + count[-4:])
    if len(count) == 0:
        return ''
    else:
        return count[:-16] + count[-16:-12] + ' ' + count[-12:-10] + '** **** ' + count[-4:]
