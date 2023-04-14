# ContagemDeTermos
This code's main goal is to count the terms that apper the most in an excel sheet, printing the 50 most recurring.
The column in question is named "PALAVRAS CHAVE" and had it's cells padronized, so all terms are separated by ",". Further padronizations,such as lowering case to avoid duplicates, are made inside the code. 

#Implementation choices
Having in mind that the goal is to count how many times each term appears, so the dictionary was the best data structure, since it adds the terms as keys and has values related to it. 
Another choice made, as said before, was to change every word to exclusevely lower case, to avoid duplicates of terms written different, like "neural network" and "Neural network".
