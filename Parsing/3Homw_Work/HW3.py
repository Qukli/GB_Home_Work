import json
from pymongo import MongoClient



with open('books.json', 'r', encoding='utf-8') as file:
  data = json.load(file)
# print(data[0])

client = MongoClient("mongodb://localhost:27017/")
db = client['my_books_database']



collection_name = "Список книг"
for item in data:
    collection = db[collection_name]
    collection.insert_one(item)

client.close()
# data = books_json['features']

client = MongoClient("mongodb://localhost:27017/")
db = client['my_books_database']
collection = db['Список книг']


# Получите общее количество книг в коллекции.
total_documents = collection.count_documents({})
print("Общее количество документов в коллекции:", total_documents)


# Запрос количества и названий книг, дороже 50 фунтов
query = {"Цена в фунтах стерлингов": {"$gt": 50.0}}

# Получения документов, соответствующих запросу
documents = collection.find(query)

print("Количество книг дороже 50 фунтов - ", collection.count_documents(query), ":")

# Отображение названий книг
for document in documents:
    print("Название книги:", document['Название'])

    ### Запрос для определения максимальной и минимальной цены книги в коллекции

# Определение конвеера для агрегации данных
pipeline = [
    {"$group": {"_id": None, "max_price": {"$max": "$Цена в фунтах стерлингов"}, "min_price": {"$min": "$Цена в фунтах стерлингов"}}}
]

# Применение конвеера
result = list(collection.aggregate(pipeline))

# Получение минимального и максимального значений
max_price = result[0]["max_price"]
min_price = result[0]["min_price"]

# Печать результатов
print("Минимальная цена:", min_price)
print("Максимальная цена:", max_price)


# Отфильтруйте документы по критерию "Количество в наличии", равному "20", и подсчитайте количество совпадающих документов.

query1 = {"Количество в наличии": {"$gt": 20}}
documents = collection.find(query1)
print("Количество книг = 20  - ", collection.count_documents(query1), ":")
