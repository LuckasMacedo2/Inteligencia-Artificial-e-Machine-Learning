import pandas as pd

df = pd.read_csv('/home/lucas/Downloads/ms.csv')

df1 = df['bola 1'].value_counts()[:6]
df2 = df['bola 2'].value_counts()[:6]
df3 = df['bola 3'].value_counts()[:6]
df4 = df['bola 4'].value_counts()[:6]
df5 = df['bola 5'].value_counts()[:6]
df6 = df['bola 6'].value_counts()[:6]

#keys = ['1', '2', '3', '4', '5', '6', '7']

dfu = pd.concat([df1, df2, df2, df3, df4, df5, df6])

print(df2.append(df4))

print (dfu.index.value_counts())
#print (dfu.index.value_counts()[:6])

print(dfu)


#dfu = pd.merge(df1, df2)


#print (df['bola 1'].value_counts()[:6])
#print (df['bola 2'].value_counts()[:6])
#print (df['bola 3'].value_counts()[:6])
#print (df['bola 4'].value_counts()[:6])
#print (df['bola 5'].value_counts()[:6])
#print (df['bola 6'].value_counts()[:6])