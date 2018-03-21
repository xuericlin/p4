##import csv
##import pandas
##import numpy as np
##np.savetxt('data.csv', (1, 2, 3), delimiter=',')
### with open('names.csv', 'r') as csv_file:
###     csv_reader = csv.reader(csv_file)
##
##
###     with open('new_names.csv', 'w') as new_file:
###         csv_writer = csv.writer(new_file, delimiter = '\t')
##
###         for line in csv_reader:
###             csv_writer.writerow(line)
##
##poop = ["Allan", "Bob", "Cady", "Dan", "Eric", "Frank", "Gina", "Helen", "Ino", "Jack"]
##poop = [["Allan", "Bob"], ["Cady", "Dan", "Dood"], ["Eric", "Frank"], ["Gina", "Helen"], ["Ino", "Jack"]]
##poop = {'Name 1': ["bob", "cpp"], 'Name 2': ['adasd', 'asjkdas'] }
##
##df = pandas.DataFrame(poop)
##df.to_csv('listName.csv', index = False)
##
##with open('listName.csv', 'r') as csv_file:
##    csv_reader = csv.reader(csv_file)
##
##    for line in csv_reader:
##        for s in line:
##            if s != '':
##                print(s)
##
print("HELLO This is Eric")
