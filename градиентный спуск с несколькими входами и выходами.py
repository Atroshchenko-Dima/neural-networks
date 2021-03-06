import numpy
# чистая сеть с несколькими входами и выходами
weights = [ [0.1, 0.1, -0.3],
            [0.1, 0.2, 0.0],
            [0.0, 1.3, 0.1] ]

def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    output = [0,0,0]
    for i in range(len(vect)):
        output[i] = w_sum(vect,matrix[i])
        return output

def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred
# Прогноз: получение прогноза и вычисление ошибки и разности
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

input = [toes[0], wlrec[0], nfans[0]]
true = [hurt[0], win[0], sad[0]]
pred = neural_network(input, weights)

error = [0,0,0]
delta = [0,0,0]

for i in range(len(true)):
    error[i] = (pred[i] - true[i]) ** 2
    delta = pred[i] - true[i]

# Сравнение: вычисление каждого приращения weight_delta и коррекции каждого веса
import numpy as np
def outer_prod(a, b):
    
    # just a matrix of zeros
    out = np.zeros((len(a), len(b)))

    for i in range(len(a)):
        for j in range(len(b)):
            out[i][j] = a[i] * b[j]
    return out

weight_deltas = outer_prod(delta,input)

for i in range(len(weights)):
    for j in range(len(weights[0])):
        weights[i][j] -= alpha * weight_deltas[i][j]

weight_deltas = outer_prod(input, delta)