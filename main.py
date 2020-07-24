import csv
from sklearn import tree

x = []
y = []

with open('Book1.csv','r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[1:4])
        y.append(line[4])
    #print(x[0])
    #print(y[0])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[180,24,90],[170,24,65]]
answer = clf.predict(new_data)
print(answer[0])
print(answer[1])