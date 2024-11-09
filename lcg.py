# Implement a Linear Congruential Generator (LCG) in Python
import matplotlib.pyplot as plt

# LCG parameters
m = 2**31 - 1
a = 1103515245
c = 12345

def lcg(seed, count=100):
    numbers = []
    X = seed
    for _ in range(count):
        X = (a * X + c) % m
        numbers.append(X)
    return numbers

# Generate the sequence with a fixed seed for repeatability
seed = 42  # You can choose any seed value
lcg_numbers = lcg(seed)

# Plot the histogram of the generated numbers
plt.hist(lcg_numbers, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of LCG Generated Numbers')
plt.show()