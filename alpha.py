weight, goal_pred, input, alpha = (0.5, 0.8, 2.0, 0.1)
for iteration in range(20):
    print("-----\nWeight:" + str(weight))
    pred = input * weight # Прогноз
    error = (pred - goal_pred) ** 2 # Чистая ошибка
    derivative = input * (pred - goal_pred)  
    weight = weight - (alpha * derivative)
    print("Error:" + str(error) + " Prediction:" + str(pred))
