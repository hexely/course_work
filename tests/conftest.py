import pytest


@pytest.fixture
def coll():
    return [
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


@pytest.fixture
def coll_2():
    return [
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
        "to": "Счет 64686473678894779589"
      }]


@pytest.fixture
def coll_3():
    class Test:
        def __init__(self, date):
            self.date = date

    test = [Test("2019-08-26T10:50:58.294041")]
    return test
