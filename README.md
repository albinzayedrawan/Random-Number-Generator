# Random-Number-Generator

## True Random Number Generator (TRNG):
- Use an online TRNG service (e.g., random.org) or system-based entropy source (e.g., /dev/random) to collect 100 random numbers.
- Record these numbers in a text file for analysis.
- Plot the collected TRNG numbers on a histogram to visualize their distribution.
- Comment on whether the numbers appear evenly distributed or show any discernible patterns.

## Linear Congruential Generator (LCG):
-Implement an LCG, a common PRNG algorithm, in Python using the following parameters:
▪ Modulus m=2^31−1
▪ Multiplier a=1103515245
▪ Increment c=12345
- Generate a sequence of 100 numbers using the LCG, and record the results.
-Use a fixed seed to ensure repeatability, and plot the distribution of the generated
numbers.
