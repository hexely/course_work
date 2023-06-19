from utils import get_list_complited, refactoring_date, refactoring_transaction


def test_get_list_complited(coll):
    assert get_list_complited(coll)


def test_refactoring_transaction(coll_2):
    assert refactoring_transaction(coll_2)


def test_refactoring_date(coll_3):
    assert refactoring_date(coll_3, 0) == "26.08.2019"
