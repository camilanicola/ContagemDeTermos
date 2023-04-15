# ContagemDeTermos
The main objective of this code is to count the most frequently occurring terms in an Excel sheet, and to print the top 50. The relevant column in the sheet is named "PALAVRAS CHAVE," and its cells have been standardized, so that all terms are separated by commas. The code also standardizes the text further by converting all words to lowercase, which helps to avoid issues with duplicate terms (such as "neural network" and "Neural network").

To achieve this goal, the code uses a dictionary as the best data structure. This is because the dictionary allows the terms to be added as keys, with corresponding values representing the frequency of occurrence.
