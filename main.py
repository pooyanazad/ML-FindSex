import csv
from sklearn import tree
height=input("Enter your Height in cm: ")
weight=input("Enter your Weight in kg: ")
#age=input("Enter your Age: ")
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

#This 24 is age,you can use it(usless here)

new_data = [[height,24,weight]]
#you can use 2 or 3 input with change this new_data = [[height,24,weight],[height1,24,weight1]]
answer = clf.predict(new_data)
print(answer[0])
#print second entry answer print(answer[1])
