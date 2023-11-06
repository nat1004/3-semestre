import pandas as pd
import numpy as np
from math import log

s = pd.Series(['matematicas', 'historia', 'economia', 'programacion', 'ingles'], dtype='string')
print(s)

s = pd.Series({'matematicas': 6.0, 'economia': 4.5, 'programacion': 8.5})

print(s)

s = pd.Series([1,2,2,3,3,3,4,4,4,4])
print(s.size)
print(s.index)
print(s.dtype)

print(s[1:3])

s= pd.Series([1,1,1,1,2,2,2,3,3,4])

print(s.count())
print(s.sum())
print(s.cumsum())
print(s.value_counts())
print(s.value_counts(normalize=True))
print(s.min())
print(s.mean())
print(s.std())
print(s.describe())

s = pd.Series([1,2,3,4])
print(s*2)
print(s%2)

s = pd.Series(['a', 'b', 'c'])
print(s*5)


from math import log
s = pd.Series([1,2,3,4])
print(s.apply(log))

s = pd.Series(['a','b','c'])
print(s.apply(str.upper))

s = pd.Series({'matematicas': 6.0, 'economia': 4.5, 'programacion': 8.5})
print(s[s > 5])
print(s.sort_values())
print(s.sort_index(ascending=False))

s = pd.Series(['a','b',None,'c',np.nan,'d'])
print(s)
print(s.dropna())


datos = {'nombre':['maria','luis','carmen','antonio'],
         'edad':[18,22,20,21],
         'grado':['economia','medicina','arquitectura','economia'],
         'correo':['maria@gmail.com','luis@yahoo.es','carmen@gmail.com','antonio@gmail.com']}
df = pd.DataFrame(datos)
print(df)

df = pd.DataFrame([['maria',18],['luis',22],['carmen',20]],columns=['nombre','edad'])
print(df)

df = pd.DataFrame([{'nombre':'maria','edad':18},{'nombre':'luis','edad':22},{'nombre':'carmen'}])
print(df)

df = pd.DataFrame(np.random.randn(4,3), columns=['a','b','c'])
print(df)

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
print(df.head())

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
df.info()
print(df.shape)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)

df = pd.read_csv(
'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.rename(columns={'nombre':'nombre y apellidos', 'altura':'estatura'}, index={0:1000, 1:1001, 2:1002}))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.reindex(index=[4, 3, 1], columns=['nombre', 'tensión', 'colesterol']))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.iloc[1, 3])
print(df.iloc[1, :2])

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.loc[2, 'colesterol'])
print(df.loc[:3, ('colesterol','peso')])
print(df['colesterol'])

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
df['diabetes'] = pd.Series([False, False, True, False, True])
print(df)

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df['altura']*100)
print(df['sexo']=='M')

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df['altura'].apply(log))

df = pd.DataFrame({'Name': ['María', 'Carlos', 'Carmen'], 'Nacimiento':['05-03-2000', '20-05-2001', '10-12-1999']})
print(pd.to_datetime(df.Nacimiento, format = '%d-%m-%Y'))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.describe())
print(df.describe(include='object'))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
edad = df.pop('edad')
print(df)
print(edad)

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
df = df.append(pd.Series(['Carlos Rivas', 28, 'H', 89.0, 1.78, 245.0], index=['nombre','edad','sexo','peso','altura','colesterol']), ignore_index=True)
print(df.tail())

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.drop([1, 3]))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df[(df['sexo']=='H') & (df['colesterol'] > 260)])

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.sort_values('colesterol'))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.dropna())

f = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.groupby('sexo').groups)
print(df.groupby(['sexo','edad']).groups)

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.groupby('sexo').get_group('M'))

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df.groupby('sexo').agg(np.mean))

datos = {'nombre':['María', 'Luis', 'Carmen'],
'edad':[18, 22, 20],
'Matemáticas':[8.5, 7, 3.5],
'Economía':[8, 6.5, 5],
'Programación':[6.5, 4, 9]}
df = pd.DataFrame(datos)
df1 = df.melt(id_vars=['nombre', 'edad'], 
var_name='asignatura', value_name='nota')
print(df1)

print(df1.pivot(index='nombre', 
columns='asignatura', values='nota'))










