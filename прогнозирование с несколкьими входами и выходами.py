def w_sum(a, b):
    output = 0
    assert(len(a) == len(b))
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

def vect_mal_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    output =[0, 0, 0]
    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix[i]) # последовательно находит 3 взвешенных суммы и сохраняет в output
    return output

weights = [ [0.1, 0.1, -0.3],
            [0.1, 0.2, 0.0],
            [0.0, 1.3, 0.1] ]
def neural_network(input, weights):
    pred = vect_mal_mul(input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)
print(pred)