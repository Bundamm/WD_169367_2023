import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def zad1():
    df = pd.read_excel('imiona.xlsx')
    # imiona zaczynające się od k
    dfk = df[df['Imie'].str[0] == 'K']
    # unikalne imiona z k
    #u_dfk = dfk['Imie'].nunique()
    u_dfk = dfk['Imie'].unique()
    print('Liczba unikalnych imion zaczynających się od K.', len(u_dfk))
#zad1()

def zad2():
    df = pd.read_excel('imiona.xlsx')
    # name_c = df.groupby('Plec')['Imie'].value_counts()
    name_c = df.groupby(['Imie', 'Plec'])['Liczba'].sum().reset_index()
    #najczęszstsze damskie
    # common_m = name_c['M'].idxmax()
    k = name_c[name_c['Plec'] == 'K'].reset_index()
    k_max = k['Liczba'].idxmax()
    k_imie = k.iloc[k_max]['Imie']
    print(k_imie)
    #najczestsze meskie
    m = name_c[name_c['Plec'] == 'M'].reset_index()
    print(m)
    m_max = m['Liczba'].idxmax()
    m_imie = m.iloc[m_max]['Imie']
    print(m_imie)
zad2()

def zad3():
    fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(10,6))
    fig.suptitle('Liczba  narodzin w latach 2010-2015')
    ax1.set_title('Wykres w pandasie')
    ax2.set_title('Wykres w seaborn')
    df = pd.read_excel('imiona.xlsx')
    #filtrowanie po kolumnie 'Rok' (2010-2015)
    data = df[(df['Rok'] >= 2010) & (df['Rok'] <= 2015)]
    data_grouped = data.groupby('Plec')['Liczba'].sum()
    data_grouped.plot.bar(ax=ax1)
    ax1.legend()

    sns.barplot(data=data, x='Plec', y='Liczba', estimator=sum, errorbar=None, ax=ax2)


    plt.show()
zad3()

#reset_index se doczytam