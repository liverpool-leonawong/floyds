<p id="#readme-top">

# Floyd's Algorithm Implementation

This repository implements Floyd's Algorithm for finding shortest routes in a weighted graph using both recursive and iterative approaches. The implementation includes unit tests and performance comparision.

</p>

## Purpose

To address the neighborhood’s need for efficient travel from So Kwun Wat to various Tuen Mun malls in Hong Kong or vice-versa

## Features

1. Recursive and Iterative Floyd-Warshall Algorithm
2. Unit Tests
   - Shortest Path Accuracy
   - Consistency between Recursive and Iterative Versions
   - Self-Distance Handling
   - One-Way Route Scenario
3. Performance Test
   The performance test compares both implementations across different graph sizes:
   - Time Complexity
   - Memory Usage
   - Scalability Comparison

## Prerequisites

#### Required Software
- Python (>= 3.8)
- Anaconda or Miniconda
- Git

#### For Mac

1. Install Homebrew (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python
   ```bash
   brew install python
   ```
3. Install Anaconda
   ```bash
   brew install --cask anaconda
   ```
4. Add Conda to Path
   ```bash
    echo 'export PATH="/usr/local/anaconda3/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
   ```

#### For Windows

1. Download and install Python from Python Official Website
2. Download and install Anaconda from Anaconda Official Website
3. Ensure Python and Conda are added to PATH during installation

## Installation 

1. Clone the repository:
   ```sh
   git clone https://github.com/liverpool-leonawong/floyds.git
   ```
   ```sh
   cd [your-directory]
   ```
2. Create and Activate Conda Environment

#### For Mac & Windows

1. Create new environment
   ```sh
   conda create -n <environment-name> python=3.8
   ```
2. Activate environment
   ```sh
   conda activate <environment-name>
   ```
3. Install Required Packages
   ```sh
   # Install required packages using conda
   conda install numpy pytest coverage memory_profiler

   # Or using pip within conda environment
   pip install -r requirements.txt
   ```

## Usage

### Running the Algorithm

1. To run the recursive version:
   ```sh
   # Mac/Linux
   python src/recursion/recursive_floyd.py

   #Windows
   python src\recursion\recursive_floyd.py
   ```
2. To run the iterative version:
   ```sh
   # Mac/Linux
   python src/iterative/iterative_floyd.py

   # Windows
   python src\iterative\iterative_floyd.py
   ```
   
### Running Tests

1. To run unit tests:
   ```sh
   # Mac/Linux
   python src/tests/unittests.py

   # Windows
   python src\tests\unittests.py
   ```
2. To run performance tests:
   ```sh
   # Mac/Linux
   python src/tests/performance_test.py

   # Windows
   python src\tests\performance_test.py
   ```

## Requirements

This repository requires the following Python packages:
- numpy >= 1.24.0 (for array operations)
- pytest >= 7.4.0 (for testing framework)
- coverage >= 7.2.7 (for test coverage reporting)
- memory_profiler >= 0.61.0 (for memory usage analysis)

## References

`Homebrew`
<br/>https://brew.sh/

`Conda User Guide`
<br/>https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

`Python`
<br/>https://www.python.org/downloads/

## License

GNU GENERAL PUBLIC LICENSE Version 3 (29 June 2007)
<br/>See `LICENSE.txt` for more information.

## Contact

Leona Wong 

(<a href="https://github.com/liverpool-leonawong">Github</a>)
(<a href="https://www.linkedin.com/in/leonawong/">Linkedin</a>)
(<a href="https://leonawong.com">Website</a>)