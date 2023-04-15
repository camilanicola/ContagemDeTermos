import pandas as pd

df=pd.read_excel("Categorias dos Artigos.xlsx")
termos=df["PALAVRAS CHAVE"]
dicTermos={}

for x in range(len(termos)):
  frase=str(termos[x]).lower()
  frase=frase.replace('\n','').split(',') 
  
  for j in frase:
   if j.strip()!=None:          
    if (dicTermos.get(j)!=None):
        dicTermos[j]+=1
    else:
        dicTermos[j]=1

ordenado=sorted(dicTermos.items(),key=lambda x: x[1], reverse=True)
top_50=ordenado[:50]

for item in top_50:
     print(item)