# Set Associative Cache Simulator

## Overview

This repository contains a Cache Simulator implemented in Python. The simulator is designed to analyze cache performance metrics such as hit rate, miss rate, and hit/miss ratio under various configurations. The repository includes:

- `CacheSimulatorCode.py`: The main Python script for the cache simulator.
- `CacheSimulatorResults.xlsx`: The excel sheet which contains the hit/miss results for varying cache sizes, block sizes and number of cache ways
- `Report.pdf`: A detailed report explaining the design, implementation, and results of the cache simulator.
- `Input-Trace-Files/`: A folder containing trace files that can be used as input for the simulator.

## Features

The cache simulator can answer the following questions:

1. **Question A**: Calculate the hit rate, miss rate, and hit/miss ratio for a given cache configuration.
2. **Question B**: Analyze how varying the cache size affects the hit rate, miss rate, and hit/miss ratio.
3. **Question C**: Analyze how varying the block size affects the hit rate, miss rate, and hit/miss ratio.
4. **Question D**: Analyze how varying the number of cache ways affects the hit rate, miss rate, and hit/miss ratio.

## Usage

### Prerequisites

- Python 3.x
- Required Python packages: `numpy`, `matplotlib`

You can install the required packages using pip:

```bash
pip install numpy matplotlib 
```

### Running the Simulator

1. **Run the simulator**:

```bash
python CacheSimulator.py
```

2. **Follow the prompts**:

The code simulates the cache for each of the five trace files. The code always simulates the cache for the user-given input(Question A).
The simulator will prompt you to enter an integer corresponding to the question you want to analyze:

Enter an integer to view the answer to the respective question:

`1` **Question B**: Displays the Hit rate, Miss rate, and Hit/Miss ratio for the given cache when the cache size is varied from 128kB to 4096kB.  
`2` **Question C**: Displays the Hit rate, Miss rate, and Hit/Miss ratio for the given cache when the block size is varied from 1 byte to 128 bytes.  
`3` **Question D**: Displays the Hit rate, Miss rate, and Hit/Miss ratio for the given cache when the number of cache ways is varied from 1 to 64.  

Enter `-1` or any other value to **Exit**.


For each question, the code uses Matplotlib to plot the Hit/Miss ratio against the varying perimeter for each of the five trace files.

### Trace Files

The `Input-Trace-Files/` folder contains trace files that can be used as input for the simulator. These trace files are referenced in the `CacheSimulator.py` script.

## Excel Sheet

The `CacheSimulatorResults.xlsx` excel sheet contains all the results obtained by varying the perimeters in a tabulated form, for each of the cases.

## Report

For a detailed explanation of the cache simulator, including design decisions, implementation details, and analysis of results, please refer to the `Report.pdf` file.
