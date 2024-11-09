# Analyze TRNG Data for Patterns
import matplotlib.pyplot as plt

# Load the TRNG data from the text file
trng_data = []
with open('trng_data.txt', 'r') as file:
    for line in file:
        # Split the line by any whitespace and filter out empty strings
        numbers = [int(num) for num in line.split() if num]
        trng_data.extend(numbers)

# Plot the histogram
plt.hist(trng_data, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of TRNG Data')
plt.show()