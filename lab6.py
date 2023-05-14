import pandas as pd
import numpy as np

# s = pd.Series([1, 3, 5, None, 4])
# print(s)
#
# data = [['Jabłka', 9], ['Banany', 8]]
# df = pd.DataFrame(data)
# df.columns = 'Owoce', 'Ilosc'
# print(df)
# print(df.iloc[[0], [0]])
# print(df.loc[[0], ['Owoce']])
#
# data2 = {'Kraj': ["Polska", "Niemcy"], "stolica": ["Warszawa", "Berlin"], "populacja": [235234534, 4235234643]}
# df2 = pd.DataFrame(data2)
# print(df2)

#zad1
df = pd.read_excel('imiona.xlsx') #read zamienia od razu w data frame
#zad2
#a
print(df[df['Liczba']>1000])
#b
print(df[df['Imie']=='TOMASZ'])
#c
print('\nc)\n')
print(df['Liczba'].sum())
#d
print('\nd)\n')
print(df.groupby(['Rok'])['Liczba'].sum())
#e
print('\ne)\n')
e = df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
e2 = e['Liczba'].sum()
print(e2)
#f
print('\nf)\n')
print(df.groupby(['Plec'])['Liczba'].sum())
#g
print('\ng)\n')
g = df.groupby(['Plec', 'Imie'])['Liczba'].sum()
print(g.loc[g.groupby('Plec').idxmax()])
#h
print('\nh)\n')
h = df.groupby(['Plec', 'Imie', 'Rok'])['Liczba'].sum()
print(h.loc[h.groupby(['Plec', 'Rok']).idxmax()])

#zad3
df2 = pd.read_csv('../../git_uwm/WD_169367_2023/zamowienia.csv', delimiter=';')
#a
print('a)')
print(df2['Sprzedawca'].unique())
#b
print('b)')
print(df2['Utarg'].nlargest(5))
#c
print('c)')
print(df2['Sprzedawca'].value_counts())
#d
print('d)')
print(df2.groupby('Kraj')['Utarg'].sum())
#e
print('e)')
print(df2[(df2['Data zamowienia'].str.contains('2005')) & (df2['Kraj']=='Polska')]['Utarg'].sum())
#f
print('f)')
print(df2[df2['Data zamowienia'].str.contains('2004')]['Utarg'].mean())
#g
print('g)')
order_2004 = df2[df2['Data zamowienia'].str.contains('2005')]
order_2005 = df2[df2['Data zamowienia'].str.contains('2004')]

order_2004.to_csv('zamowienia_2004.csv', index=False)
order_2005.to_csv('zamowienia_2005.csv', index=False)