weight = 0.5
input = 0.5
goal_prediction = 0.8
step_amount = 0.001 # шаг изменения в каждой итерации
for iteration in range(1102): # Повторить обучение много раз, чтобы получить наименьшую ошибку
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2
    print("Error:", error, " Prediction:", prediction)

    up_prediction = input * (weight + step_amount) # попробовать увеличить
    up_error = (goal_prediction - up_prediction) ** 2 # вычисление среднеквадратичной ошибки

    down_prediction = input * (weight - step_amount) # попробовать увеличить
    down_error = (goal_prediction - down_prediction) ** 2

    if(down_error < up_error):
        weight = weight - step_amount # если уменьшение дало лучший результат, то уменьшить
    if(down_error > up_error):
        weight = weight + step_amount # если увеличение дало лучший результат, увеличить

