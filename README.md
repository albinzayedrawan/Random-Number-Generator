# Random-Number-Generator

## True Random Number Generator (TRNG):
- Use an online TRNG service (e.g., random.org) or system-based entropy source (e.g., /dev/random) to collect 100 random numbers.
- Record these numbers in a text file for analysis.
- Plot the collected TRNG numbers on a histogram to visualize their distribution.
- Comment on whether the numbers appear evenly distributed or show any discernible patterns.

## Linear Congruential Generator (LCG):
- Implement an LCG, a common PRNG algorithm, in Python using any parameters of your choice.
- Generate a sequence of 100 numbers using the LCG, and record the results.
- Use a fixed seed to ensure repeatability, and plot the distribution of the generated numbers.

## Pseudo-Random Number Generator (PRNG):
- Use Python’s built-in PRNG (random module) to generate another sequence of 100 numbers.
- Set a fixed seed to make the results reproducible.
- Record and plot the distribution of these numbers alongside the LCG-generated numbers.
