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

    def refactoring_date(self):
       pass

    def __repr__(self):
        print(self._id,
              self.state,
              self.date,
              self.amount,
              self.name,
              self. description,
              self.from_,
              self.to
              )
