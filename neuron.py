from numpy import exp, array, random, dot
import future

if __name__ == '__main__':
    training_set_input = array([
        [0,0,1,0],
        [1,1,1,1],
        [1,0,1,0],
        [1,0,0,0],
        [0,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ])

training_set_outputs = array([[1,1,1,0,1,0,0]]).T

# programming discovery
random.seed(1)

synaptic_weights = random.random((4, 1)) * 2 - 1

print(synaptic_weights)

for i in range(99999):
    output = 1/(1 + exp(-(dot(training_set_input, synaptic_weights))))
    synaptic_weights += dot(training_set_input.T, (training_set_outputs - output)*output*(1 - output))
    print(synaptic_weights)

test_data = array([1, 0, 0, 0])
print(1/(1 + exp(-dot(test_data, synaptic_weights))))