import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def rem(remove_value, values):
    removes_values = []
    for i in values:
        if remove_value in i[0]:
            removes_values.append(i)
    for i in removes_values:
        values.remove(i)

with open('mes_grupo.txt', encoding='utf-8') as fp:
    text = fp.read()

matches = np.array(re.findall(r'\d\d/\d\d/2020 \d\d:\d\d - (.*?):', text))
unique, counts = np.unique(matches, return_counts=True)
resut = list(zip(unique, counts))
resut = sorted(resut, key=lambda item: item[1], reverse=True)
rem('\u200e', resut)
print("*Resultado levantamento de atividade no grupo de 12-05 a 12-06*")
for uniq, count in resut:
    print(f'{uniq}: {count}')