data = [(3, 4)
("amir", 10)
("brenda", 10)
("charlie", 10)
("amir", "brenda", 5)
("brenda", "charlie", 5)
("charlie", "amir", 20)
("charlie", "amir", 7)
]

class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount 
        