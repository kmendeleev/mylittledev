# Вам нужно реализовать базовую логику этого модуля. Создайте класс BankAccount, который будет представлять счет клиента.

# 1. При создании объекта класса BankAccount ему должны передаваться два параметра: owner_name (имя владельца) и initial_balance (начальный баланс).
# 2. Реализуйте метод deposit(amount), который увеличивает баланс на указанную сумму.
# 3. Реализуйте метод withdraw(amount), который уменьшает баланс. Метод не должен позволять снять больше денег, чем есть на счете, и в таком случае должен выводить в консоль сообщение "Недостаточно средств".
# 4. Реализуйте метод get_balance(), который возвращает текущий баланс и имя владельца в формате: "Баланс счета для [Имя Владельца]: [Сумма]".

# Для проверки создайте два экземпляра счета, например, для клиентов "Иван" и "Мария". Проведите несколько операций пополнения и снятия, включая попытку снять сумму, превышающую баланс. После всех операций выведите в консоль итоговый баланс обоих счетов.

class BankAccount:
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return f"Баланс счета для {self.owner_name}: {self.balance}"
    

    def transfer(self, amount, recipient):    
        if self.balance >= amount:        
            self.withdraw(amount)        
            recipient.deposit(amount)    
        else:        
            print("Недостаточно средств для перевода")

account1 = BankAccount("Алексей", 2000)
account2 = BankAccount("Ольга", 5000)
account3 = BankAccount("Петр", 1000)
account1.transfer(1000, account2)
account3.transfer(1500, account2)

print(account1.get_balance())
print(account2.get_balance())
print(account3.get_balance())



# 2. Создайте три экземпляра класса BankAccount: account1 (владелец "Алексей", начальный баланс 2000), account2 (владелец "Ольга", начальный баланс 5000) и account3 (владелец "Петр", начальный баланс 1000).
# 3. Переведите 1000 с account2 на account1.
# 4. Попытайтесь перевести 1500 с account3 на account2.
# 5. Выведите в консоль итоговые балансы всех трех счетов, используя метод get_balance().