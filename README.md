# Word Processing Tools

This project contains a collection of Python scripts designed for various word processing tasks, including filtering, removing duplicates, and generating passwords.

## Scripts Overview

### 1. Word Filter
This script filters words from a file by removing those that already exist in another file. The result is saved in a new file.

#### Functionality
The script performs the following operations:

1. **File Reading**:
   - Reads two lists of words from text files:
     - `teste.txt` (File_A): Contains the list of words to be filtered.
     - `teste2.txt` (File_B): Contains the list of words to exclude from the result.

2. **Filtering**:
   - Compares the words in File_A with those in File_B and creates a new list containing only the words not found in File_B.

3. **Output**:
   - Saves the filtered list in a new file called `Subtracted.txt`.

#### Code Structure
- **Use of Sets**: Uses a set (`set`) to store existing words, allowing quick verification during filtering.

### 2. Remove Duplicates
This script removes duplicate lines from a text file while preserving the order of the lines.

#### Functionality
The script performs the following operations:

1. **File Reading**:
   - Reads lines from the input file and stores unique lines in an ordered dictionary.

2. **Output**:
   - Writes the unique lines to the output file in the same order they appeared in the input file.

### 3. Password Generator
This script generates passwords based on a list of words, adding digits and special characters to create variations.

#### Functionality
The script performs the following operations:

1. **Password Generation**:
   - Generates passwords by appending digits and special characters to each word from the input file.

2. **Output**:
   - Saves the generated passwords to an output file.

## Conclusion
These scripts provide practical solutions for managing and processing word lists, including filtering, deduplication, and password generation. They are especially useful when working with large datasets, as they handle extensive data efficiently.