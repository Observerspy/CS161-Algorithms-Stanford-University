import numpy as np
import pandas as pd

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        mylist = f.readlines()
    weight = [int(i.split('\n')[0].split(' ')[0]) for i in mylist[1:]]
    length = [int(i.split('\n')[0].split(' ')[1]) for i in mylist[1:]]
    index = [i for i in range(1,10001)]
    data = pd.DataFrame({'weight':pd.Series(weight),'length':pd.Series(length)})
    data['diff'] = data['weight'] - data['length']
    data['div'] = data['weight'] / data['length']

    data = data.sort_values(by=['diff', 'weight'],ascending=[False,False]) #1
    # data = data.sort_values(by='div',ascending=False) #2
    l = 0
    sum = 0
    for i in range(len(data)):
        d = data.iloc[i]
        l += d['length']
        sum += l * d['weight']
    print(sum) #69119377652 67311454237
