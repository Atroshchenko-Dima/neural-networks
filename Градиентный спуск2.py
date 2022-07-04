weight, goal_pred, input = (0.0, 0.8, 1.1)
for iteration in range(4):
    print("-----\nWeight:" + str(weight))
    pred = input * weight # Прогноз
    error = (pred - goal_pred) ** 2 # Чистая ошибка
    delta = pred - goal_pred # Величина промаха(чистая разность между прогнозом и истинным значением)
    weight_delta = delta * input # Производная(как быстро изменится ошибка при изменении)
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
    print("Delta:" + str(delta) + " Weight Delta:" + str(weight_delta))