import random
import time
import csv
import keyboard

# accessing CSV file in read mode
# for accessing last known serial number and t values
fr = open(r'C:\Users\sinha\OneDrive\Desktop\VS Code Projects\Real Time Random Graph\Data.csv', mode='r')
re = list(csv.reader(fr))
if re != []:
    serialno = int(re[-1][0]) + 1
    t = int(re[-1][1]) + 1
else:
    serialno = 1
    t = 0

# function for inputting data by the second
def Inp():
    # accessing CSV file in append mode
    fw = open(r'C:\Users\sinha\OneDrive\Desktop\VS Code Projects\Real Time Random Graph\Data.csv', mode='a+', newline='')
    wr = csv.writer(fw)
    
    global serialno
    global t
    wr.writerow([serialno, t, random.randrange(0,50), random.randrange(0, 30), random.randrange(0,40), random.randrange(0, 60)])
    serialno += 1
    t += 1
    time.sleep(1)
    fw.close()

# infinite loop until termination by holding q key for 1 second
while True:
    Inp()
    if keyboard.is_pressed('q'):
        break

fr.close()