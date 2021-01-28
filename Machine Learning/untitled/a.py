import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('tips')

# Plotando todos os gráficos possiveis com as diversas combinações das variaveis
# presentes no data set
sns.pairplot(iris, hue = 'time')
print (iris)
plt.show()