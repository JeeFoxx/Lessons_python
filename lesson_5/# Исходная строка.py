test_results = {
    'Петя': 2,
    'Маша': 5,
    'Вася': 4,
}

marks = test_results.values()
marks_sum = 0

# Накапливаем сумму, добавляя по одной оценке за раз
for mark in marks:
    marks_sum = marks_sum + mark

average_result = marks_sum / len(test_results)
print('Средний бал:', average_result)