# Frequency Traditional Model (FTM) - V1.4 (Stable)

## Overview

The **Frequency Traditional Model (FTM)** is a Python program designed to calculate and visualize beat frequencies resulting from multiple input frequencies. This model computes all possible beat frequencies between the provided frequencies and generates precise time stamps indicating when these beats occur within a one-second interval. It offers a comprehensive analysis by displaying the results in a color-coded table, highlighting coinciding beats for easy interpretation.

## Features

- **Multi-Frequency Input**: Accepts two or more unique frequencies entered by the user.
- **Beat Frequency Calculation**: Computes absolute differences (beat frequencies) between all pairs of input frequencies.
- **Time Stamp Generation**: Calculates reciprocals of beat frequencies to determine when beats occur within one second.
- **Color-Coded Visualization**:
  - **Cyan**: Highlights time stamps and headers for clarity.
  - **Red**: Marks coinciding beats occurring at the same time stamp.
  - **White**: Indicates individual beat occurrences.
- **User-Friendly Interface**: Interactive command-line input with error handling for invalid entries.

## How It Works

1. **Input Frequencies**:
   - The user is prompted to enter at least two frequencies separated by commas.
   - The program ensures that at least two unique, valid integers are provided.

2. **Beat Frequency Computation**:
   - Calculates the absolute differences between all pairs of input frequencies to find all possible beat frequencies.
   - Removes duplicate beat frequencies and sorts them for clarity.

3. **Time Stamp Calculation**:
   - Calculates the reciprocal of each unique beat frequency to determine the interval between beats.
   - Generates time stamps up to one second for each beat frequency by multiplying the reciprocal with incremental integers.

4. **Data Compilation**:
   - Collects all time stamps and organizes them into a Pandas DataFrame.
   - Each beat frequency is represented as a column in the table, marking where beats occur.

5. **Visualization**:
   - Displays the beat table in the console with color-coded formatting using the Colorama library.
   - Coinciding beats are highlighted in red to easily identify simultaneous occurrences.