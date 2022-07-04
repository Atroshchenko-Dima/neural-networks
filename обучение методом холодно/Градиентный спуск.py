weight = 0.5
input = 0.5
goal_prediction = 0.8
for iteration in range(20):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2
    direction_and_amount = (prediction - goal_prediction) * input # Код сначала вычисляет чистую ошибку, а затем умножает ее на инпут 
    # чтобы выполнить масштабирование, обращение знака и остановку, превращая чистую ошибку в значение, пригодное для изменения weight
    weight = weight - direction_and_amount
    print("Error:", error, " Prediction:", prediction)