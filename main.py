import datetime
import os

print("Hello world!")
print("Текущая дата: " + str(datetime.datetime.now().strftime('%Y/%m/%d')))
for file in os.listdir(): print(file)