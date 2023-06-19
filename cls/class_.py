class Transaction:

    def __init__(self, _id=None, state=None, date=None, amount=None, name=None, description=None, from_=None, to=None):
        self._id = _id
        self.state = state
        self.date = date
        self.amount = amount
        self.name = name
        self. description = description
        self.from_ = from_
        self.to = to
