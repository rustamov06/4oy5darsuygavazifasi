# 2024.12.07 Uyga vazifa


# 1 vazifa

from decimal import Decimal, InvalidOperation
import random
from datetime import datetime


class TemperatureDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)
    def __set__(self, instance, value):
        try:
            decimal_value = Decimal(value)
        except InvalidOperation:
            raise ValueError("Harorat faqat raqam bo'lishi kerak.")
        if not (-50 <= decimal_value <= 50):
            raise ValueError("Harorat me’yordan chiqib ketdi: -50°C dan 50°C gacha.")
        instance.__dict__[self.name] = decimal_value
    def __set_name__(self, owner, name):
        self.name = name
class TemperatureStats:
    temperature = TemperatureDescriptor()
    def __init__(self):
        self.readings = []
    def add_reading(self, temperature, date=None):
        if date is None:
            date = datetime.now()
        self.temperature = temperature
        self.readings.append((self.temperature, date))
    def display_readings(self):
        for temp, date in self.readings:
            print(f"Harorat: {temp}°C ({date.strftime('%Y-%m-%d')})")
def generate_random_temperatures(count=1):
    stats = TemperatureStats()
    try:
        temp = random.uniform(-10, 40)
        date = datetime.now()
        stats.add_reading(temp, date)
    except ValueError as e:
        print(e)
    return stats
temperature_stats = generate_random_temperatures(10)
temperature_stats.display_readings()
