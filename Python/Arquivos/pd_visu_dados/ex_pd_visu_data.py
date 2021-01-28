import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')

# --- 1 ---
#df3.plot.scatter(x = 'a', y = 'b', color = 'red', figsize=(12, 5))

# --- 2 ---
#df3['a'].hist()

# --- 3 ---
#plt.style.use('ggplot')

#df3['a'].plot.hist(bins=30, alpha = 0.5)

# --- 4 ---
#df3[['a', 'b']].plot.box()

# --- 5 ---
#df3['d'].plot.kde()

# --- 6 ---
#df3['d'].plot.kde(lw = 5, ls = '--', color = 'red')

# --- 7 ---
# ix[inicio:fim], fatia o dataframe

#df3.ix[:30].plot.area(alpha = 0.5)

# --- bonus ---
# Tirar legenda de dentro do grafico
f = plt.figure()
df3.ix[:30].plot.area(alpha = 0.5)
plt.legend(loc='center left', bbox_to_anchor = (1.0, 0.5))
plt.show()