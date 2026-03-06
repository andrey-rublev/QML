import numpy as np

testString = input("Enter encoded string: ")
frequencies = np.zeros(128)

for i in range(128):
    frequencies[i] = testString.count(chr(i))
    
frequencies = frequencies / np.linalg.norm(frequencies)
print(frequencies)
