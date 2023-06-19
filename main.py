from utils.utils import get_json, get_list_complited, refactoring_date, hide_numbers
from cls.class_ import Transaction

json_file = "files/operations.json"

f = get_json(json_file)

a = get_list_complited(f)

print(a)

list_oject = []

c = 0

for i in a:
    c += 1
    print(i["id"])
    list_oject.append(Transaction(i["id"], i["state"], i["date"],
                                  i["operationAmount"]["amount"],
                                  i["operationAmount"]["currency"]["name"],
                                  i["description"], i["from"], i["to"]
                                  ))

print(c)

#print(list_oject[2].__repr__)

a = sorted(list_oject, key=lambda list_oject: list_oject.date, reverse=True)
print("ok")
print(a[0]._id)

for i in range(5):
    print(refactoring_date(a, i), a[i].description)
    print(hide_numbers(a[i].from_), '->', hide_numbers(a[i].to))
    print(a[i].amount, a[i].name, '\n')
