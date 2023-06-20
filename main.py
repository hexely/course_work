from utils.code import get_json, get_list_complited, refactoring_date, refactoring_transaction
from cls.class_ import Transaction

json_file = "files/operations.json"

list_operation = get_json(json_file)

list_complited = get_list_complited(list_operation)


list_oject = []
# запись объектов Transaction и добавление в список выше
for data in list_complited:
    list_oject.append(Transaction(data["id"], data["state"], data["date"],
                                  data["operationAmount"]["amount"],
                                  data["operationAmount"]["currency"]["name"],
                                  data["description"], data["from"], data["to"]
                                  ))

# подсмотренная в инете функция сортировки объектов в списке по полю класса (date) в режиме reverse
list_complited = sorted(list_oject, key=lambda oject: oject.date, reverse=True)

# вывод последних 5-ти выполненных по дате операций.(первые 5 в отсортированном списке выше)
for count in range(5):

    # информация о дате совершения операции, описание типа перевода
    # откуда (может отсутстовать), куда
    # сумма операции и валюта
    print(refactoring_date(list_complited, count), list_complited[count].description)
    print(refactoring_transaction(list_complited[count].from_), '->', refactoring_transaction(list_complited[count].to))
    print(list_complited[count].amount, list_complited[count].name, '\n')
