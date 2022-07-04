input = 2.0
weight = 0.5
goal_pred = 0.8
alpha = 0.1
for iteration in range(20):

    pred = weight * input # прогноз
    error = (pred - goal_pred) ** 2 # чистая ошибка
    delta = pred - goal_pred # величина промаха
    weight_delta = input * delta # Производная
    weight -= alpha * weight_delta 
    print("Error:" + str(error) + " Prediction:" + str(pred))