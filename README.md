# Word Filter
  This Python script is a simple tool for filtering words from a file by removing those that already exist in another file. The result is saved in a new file.

## Functionality
  The script performs the following operations:

1. File Reading:
- Reads two lists of words from text files:
  - `teste.txt` (File_A): Contains the list of words to be filtered.
  - `teste2.txt`  (File_B): Contains the list of words to exclude from the result.

2. Filtering:
- Compares the words in File_A with those in File_B and creates a new list containing only the words not found in File_B.

3. Output:
- Save the filtered list in a new file called Subtracted.txt.

## Code Structure

- Use of Sets: Uses a set (`set`) to store existing words, allowing quick verification during filtering.

## Conclusion
  This script is a practical solution for managing word lists by ensuring that duplicate or already-existing words are excluded from a new list. It is especially useful when working with large files, as it handles extensive datasets efficiently.