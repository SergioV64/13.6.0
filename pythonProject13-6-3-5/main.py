list_ = [-5, -2, 4, 8, 12, 7, -5]
index_negative = None
for i, value in enumerate(list_):
    if value < 0:
        index_negative = i  # перезаписываем значение индекса
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
