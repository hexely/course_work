from utils.code import get_list_complited, refactoring_date, refactoring_transaction


def test_get_list_complited(coll):
    assert get_list_complited(coll) == [
      {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
      }]


def test_get_list_complited_2(coll_2):
    assert get_list_complited(coll_2) == [
      {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": '',
        "to": "Счет 64686473678894779589"
      }]


def test_refactoring_transaction():
    assert refactoring_transaction("Счет 64686473678894779589") == "Счет **9589"
    assert refactoring_transaction("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert refactoring_transaction('') == ''


def test_refactoring_date(coll_3):
    assert refactoring_date(coll_3, 0) == "26.08.2019"
