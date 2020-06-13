import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def removeIfContain(remove_value, values):
    removes_values = []
    for i in values:
        if remove_value in i[0]:
            removes_values.append(i)
    for i in removes_values:
        values.remove(i)


def getCountList(text):
    matches = np.array(re.findall(r'\d\d/\d\d/\d\d\d\d \d\d:\d\d - (.*?):', text))
    unique, counts = np.unique(matches, return_counts=True)
    result = list(zip(unique, counts))
    result = sorted(result, key=lambda item: item[1], reverse=True)
    removeIfContain('\u200e', result)
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Count Interation in group')
    parser.add_argument('filename', metavar='file', type=str, nargs=1,
                        help='Filename with whatsapp name')
    args = parser.parse_args()
    filename = args.filename[0]

    with open(filename, encoding='utf-8') as fp:
        text = fp.read()
    result = getCountList(text)
    print("*Resultado levantamento de atividade no grupo de 12-05 a 12-06*")
    for uniq, count in result:
        print(f'{uniq}: {count}')
