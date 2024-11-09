# Python’s Built-in PRNG
import random
import matplotlib.pyplot as plt

# Set a fixed seed for reproducibility
random.seed(42)

# Generate a sequence of 100 random numbers using Python's built-in PRNG
prng_numbers = [random.randint(0, 2**31 - 1) for _ in range(100)]

# Plot the histogram of the generated numbers
plt.hist(prng_numbers, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Python’s Built-in PRNG Numbers')
plt.show()