# 2024.12.07 Uyga vazifa


# 1 vazifa

# from decimal import Decimal, InvalidOperation
# import random
# from datetime import datetime
#
#
# class TemperatureDescriptor:
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)
#     def __set__(self, instance, value):
#         try:
#             decimal_value = Decimal(value)
#         except InvalidOperation:
#             raise ValueError("Harorat faqat raqam bo'lishi kerak.")
#         if not (-50 <= decimal_value <= 50):
#             raise ValueError("Harorat me’yordan chiqib ketdi: -50°C dan 50°C gacha.")
#         instance.__dict__[self.name] = decimal_value
#     def __set_name__(self, owner, name):
#         self.name = name
# class TemperatureStats:
#     temperature = TemperatureDescriptor()
#     def __init__(self):
#         self.readings = []
#     def add_reading(self, temperature, date=None):
#         if date is None:
#             date = datetime.now()
#         self.temperature = temperature
#         self.readings.append((self.temperature, date))
#     def display_readings(self):
#         for temp, date in self.readings:
#             print(f"Harorat: {temp}°C ({date.strftime('%Y-%m-%d')})")
# def generate_random_temperatures(count=1):
#     stats = TemperatureStats()
#     try:
#         temp = random.uniform(-10, 40)
#         date = datetime.now()
#         stats.add_reading(temp, date)
#     except ValueError as e:
#         print(e)
#     return stats
# temperature_stats = generate_random_temperatures(10)
# temperature_stats.display_readings()

# # 2 vazifa
#
# from decimal import Decimal, InvalidOperation
# from datetime import datetime
#
#
# class InsufficientFundsError(Exception):
#     """Maxsus exception - balans yetarli emasligini bildiradi."""
#     pass
#
#
# class TransactionAmount:
#     """Descriptor: faqat Decimal formatdagi qiymatni qabul qiladi."""
#
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, Decimal('0.00'))
#
#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#             if value < Decimal('0.00'):
#                 raise ValueError("Tranzaksiya summasi manfiy bo'lishi mumkin emas!")
#             instance.__dict__[self.name] = value
#         except (InvalidOperation, ValueError) as e:
#             raise ValueError(f"Yaroqsiz tranzaksiya qiymati: {e}")
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#
# class BankAccount:
#     transaction_amount = TransactionAmount()
#
#     def __init__(self, initial_balance):
#         """Bank hisobini ochish."""
#         self.balance = Decimal(initial_balance)
#         self.transactions = []
#
#     def deposit(self, amount):
#         """Pul qo'shish."""
#         self.transaction_amount = amount
#         self.balance += self.transaction_amount
#         self.__record_transaction("Deposit")
#
#     def withdraw(self, amount):
#         """Pul yechish."""
#         self.transaction_amount = amount
#         if self.transaction_amount > self.balance:
#             raise InsufficientFundsError(f"Xatolik: Balans yetarli emas! Joriy balans: {self.balance}")
#         self.balance -= self.transaction_amount
#         self.__record_transaction("Withdrawal")
#
#     def __record_transaction(self, transaction_type):
#         """Tranzaksiya tarixini yozish."""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.transactions.append({
#             'type': transaction_type,
#             'amount': self.transaction_amount,
#             'timestamp': timestamp,
#             'remaining_balance': self.balance
#         })
#
#     def show_balance(self):
#         """Balansni ko'rsatish."""
#         return f"Hisobingiz: {self.balance} UZS"
#
#     def transaction_history(self):
#         """Tranzaksiya tarixini ko'rsatish."""
#         if not self.transactions:
#             return "Tranzaksiyalar hali yo'q."
#         history = ["\nTranzaksiya tarixi:"]
#         for t in self.transactions:
#             history.append(
#                 f"{t['timestamp']} - {t['type']}: {t['amount']} UZS, Qolgan balans: {t['remaining_balance']} UZS")
#         return "\n".join(history)
# if __name__ == "__main__":
#     print("Bank hisob dasturiga xush kelibsiz!")
#     initial_balance = input("Hisobingizdagi boshlang'ich balansni kiriting (UZS): ")
#
#     try:
#         account = BankAccount(initial_balance)
#     except Exception as e:
#         print(f"Xato: {e}")
#         exit()
#
#     while True:
#         print("\nMenyu:")
#         print("1. Balansni ko'rish")
#         print("2. Pul qo'shish")
#         print("3. Pul yechish")
#         print("4. Tranzaksiya tarixini ko'rish")
#         print("5. Dasturdan chiqish")
#
#         choice = input("Tanlovingizni kiriting (1-5): ")
#
#         if choice == '1':
#             print(account.show_balance())
#         elif choice == '2':
#             amount = input("Qo'shmoqchi bo'lgan summani kiriting (UZS): ")
#             try:
#                 account.deposit(amount)
#                 print("Pul muvaffaqiyatli qo'shildi!")
#             except Exception as e:
#                 print(f"Xato: {e}")
#         elif choice == '3':
#             amount = input("Yechmoqchi bo'lgan summani kiriting (UZS): ")
#             try:
#                 account.withdraw(amount)
#                 print("Pul muvaffaqiyatli yechildi!")
#             except InsufficientFundsError as e:
#                 print(e)
#             except Exception as e:
#                 print(f"Xato: {e}")
#         elif choice == '4':
#             print(account.transaction_history())
#         elif choice == '5':
#             print("Dasturdan chiqmoqdasiz. Xayr!")
#             break
#         else:
#             print("Noto'g'ri tanlov! Iltimos, 1-5 oralig'idagi raqamni tanlang.")


# 3 vazifa

# from decimal import Decimal, InvalidOperation
# from datetime import datetime, timedelta
# import random
# class TicketPrice:
#     """Descriptor: faqat Decimal formatdagi chipta narxini qabul qiladi."""
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, Decimal('0.00'))
#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#             if value <= Decimal('0.00'):
#                 raise ValueError("Chipta narxi manfiy yoki nol bo'lishi mumkin emas!")
#             instance.__dict__[self.name] = value
#         except (InvalidOperation, ValueError) as e:
#             raise ValueError(f"Yaroqsiz chipta narxi: {e}")
#     def __set_name__(self, owner, name):
#         self.name = name
# class Ticket:
#     price = TicketPrice()
#     def __init__(self, price):
#         """Chiptaning narxi va sotish sanasini o‘rnatish."""
#         self.price = price
#         self.sale_date = self.__generate_random_date()
#
#     @staticmethod
#     def __generate_random_date():
#         """Tasodifiy sotish sanasini generatsiya qilish."""
#         start_date = datetime.now()
#         random_days = random.randint(1, 30)  # Keyingi 30 kun ichidagi sanalar
#         random_date = start_date + timedelta(days=random_days)
#         return random_date.strftime("%Y-%m-%d")
#     def show_ticket_info(self):
#         """Chipta haqida ma'lumotni qaytarish."""
#         return f"Chipta narxi: {self.price} UZS. Sotish sanasi: {self.sale_date}."
# if __name__ == "__main__":
#     print("Chipta sotib olish dasturiga xush kelibsiz!")
#     while True:
#         try:
#             ticket_price = input("Chipta narxini kiriting (UZS): ")
#             ticket = Ticket(ticket_price)
#             print(ticket.show_ticket_info())
#         except ValueError as e:
#             print(f"Xato: {e}")
#         choice = input("Yana chipta yaratmoqchimisiz? (ha/yo'q): ").strip().lower()
#         if choice != 'ha':
#             print("Dasturdan chiqmoqdasiz. Xayr!")
#             break



# 4 vazifa

# from decimal import Decimal, InvalidOperation
# from datetime import datetime, timedelta
# import random
# class Salary:
#     """Descriptor: faqat Decimal formatdagi maoshni qabul qiladi."""
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, Decimal('0.00'))
#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#             if value <= Decimal('0.00'):
#                 raise ValueError("Oylik maosh manfiy yoki nol bo'lishi mumkin emas!")
#             instance.__dict__[self.name] = value
#         except (InvalidOperation, ValueError) as e:
#             raise ValueError(f"Yaroqsiz oylik maosh: {e}")
#
#     def __set_name__(self, owner, name):
#         self.name = name
# class Employee:
#     salary = Salary()
#     def __init__(self, name, salary):
#         """Ishchining ismi va oylik maoshini o‘rnatish."""
#         self.name = name
#         self.salary = salary
#         self.payment_date = self.__generate_random_date()
#     @staticmethod
#     def __generate_random_date():
#         """Tasodifiy to‘lov sanasini generatsiya qilish."""
#         start_date = datetime.now()
#         random_days = random.randint(1, 30)
#         random_date = start_date + timedelta(days=random_days)
#         return random_date.strftime("%Y-%m-%d")
#     def show_employee_info(self):
#         """Ishchi haqida ma'lumotni qaytarish."""
#         return f"Ishchi: {self.name}. Oylik maosh: {self.salary} UZS. To‘lov sanasi: {self.payment_date}."
# if __name__ == "__main__":
#     print("Ishchilar uchun oylik maosh hisoblash dasturiga xush kelibsiz!")
#     employees = []
#     while True:
#         try:
#             name = input("\nIshchining ismini kiriting: ").strip()
#             salary = input("Ishchining oylik maoshini kiriting (UZS): ").strip()
#             employee = Employee(name, salary)
#             employees.append(employee)
#             print(employee.show_employee_info())
#         except ValueError as e:
#             print(f"Xato: {e}")
#         choice = input("\nYana ishchi qo‘shmoqchimisiz? (ha/yo'q): ").strip().lower()
#         if choice != 'ha':
#             print("\nDastur tugadi. Quyidagi ishchilar qo‘shildi:")
#             for emp in employees:
#                 print(emp.show_employee_info())
#             break
