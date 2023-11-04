import pandas as pd
import numpy as np
"""
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
"""
df = pd.read_csv('https')
print(df.head())


