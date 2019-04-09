#titanic
import pandas as pd
passengers = pd.read_csv('titanic.csv')

count_passengers = len(passengers)
sex_count = passengers['Sex'].value_counts()
print("Number of males and females:", sex_count['male'], sex_count['female'])

print("Part of survived: {:.2f}".format(passengers['Survived'].value_counts()[1]/count_passengers*100))

print("Part of 1 Pclass passengers : {:.2f}".format(passengers['Pclass'].value_counts()[1]/count_passengers*100))

print("Average age and age's Median: {:.2f} {:.2f}".format(passengers['Age'].mean(), 
                                                           passengers['Age'].median()))

print("Pearson Correlation: {:.2f}".format(passengers['SibSp'].corr(passengers['Parch'], 
                                                                    method='pearson')))

women = pd.DataFrame(passengers, columns = ['Name', 'Sex'])
women = women.loc[women['Sex'] == 'female']
fnames = {}
for word in women['Name']:
    t = word.split('.')[1].split('(')[-1].split()[0]
    fnames[t] = fnames.get(t, 0) + 1
print("Most common female name:", sorted(fnames.items(), key=lambda x: x[1], reverse=True)[0][0])
