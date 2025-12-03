purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    total = 0
    for i in purchases:
        total += i['price'] * i['quantity']
    return total


def items_by_category(purchases):
    category = {}
    for i in purchases:
        if i['category'] in category:
            category[i['category']].append(i['item'])
        else:
            category[i['category']] = [i['item']]
    return category

def expensive_purchases(purchases, min_price):
    return [i for i in purchases if i['price'] >= min_price]

def average_price_by_category(purchases):
    avg_price = {}
    category = items_by_category(purchases)
    for k, v in category.items():
        if len(v) <= 1:
            avg_price[k] = [item["price"] for item in purchases if item["item"] == v[0]][0]
        else:
            total_price_fruit = 0
            for purchase in purchases:
                if purchase["item"] in v:
                    total_price_fruit += purchase["price"]     
            avg_price[k] = total_price_fruit / len(v)
    return avg_price
    
def most_frequent_category(purchases):
    return max(purchases, key=lambda x: x['quantity'])['category']
 
print(f"Общая выручка: {total_revenue(purchases)}")   
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {1.0}: {expensive_purchases(purchases, 1)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")