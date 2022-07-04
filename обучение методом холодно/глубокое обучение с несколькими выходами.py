# Чистая сеть с несколькими выходными данными
weights = [0.3, 0.2, 0.9]

def neural_network(input, weights):
    pred = scalar_ele_mul(input, weights)
    return pred
# вычисление каждого приращения weight_delta и коррекция каждого веса
def scalar_ele_mul(number, vector):
    output = [0,0,0]
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output
# получение прогноза и вычисление ошибки разности
wlrec = [0.65, 0.8, 0.8, 0.9]
hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad =[0.1, 0.0, 0.1, 0.2]

input = wlrec[0]
true = [hurt[0], win[0], sad[0]]
pred = neural_network(input, weights)

error = [0,0,0]
delta = [0,0,0]

for i in range(len(true)):
    error[i] = (pred[i] - true[i]) ** 2
    delta[i] = pred[i] - true[i]

# Корректировка весов
weight_deltas = scalar_ele_mul(input, weights)

alpha = 0.1
for i in range(len(weights)):
    weights[i] -= (weight_deltas[i]* alpha)
print("Weights:" + str(weights))
print("Weight Deltas:" + str(weight_deltas))