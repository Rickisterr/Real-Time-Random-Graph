import matplotlib.pyplot as pt
from matplotlib.animation import FuncAnimation
import csv

# accessing csv file in reading mode
f = open(r"Data.csv", mode="r")
read = list(csv.reader(f))

# initializing axes variables
t_lis, y1_lis, y2_lis, y3_lis, y4_lis = [], [], [], [], []
for row in read:
    t_lis.append(float(row[1]))
    y1_lis.append(float(row[2]))
    y2_lis.append(float(row[3]))
    y3_lis.append(float(row[4]))
    y4_lis.append(float(row[5]))

# dividing canvas into 4 subsections for 4 graphs
figure, axis = pt.subplots(2,2)

# animate function
def animate(i):
    f_new = open(r"Data.csv", mode="r")
    new_read = list(csv.reader(f_new))
    if float(new_read[-1][1]) not in t_lis:
        t_lis.append(float(new_read[-1][1]))
        y1_lis.append(float(new_read[-1][2]))
        y2_lis.append(float(new_read[-1][3]))
        y3_lis.append(float(new_read[-1][4]))
        y4_lis.append(float(new_read[-1][5]))
    axis[0,0].clear()
    axis[0,1].clear()
    axis[1,0].clear()
    axis[1,1].clear()
    axis[0,0].plot(t_lis,y1_lis)
    axis[0,0].set_title("Graph 1")
    axis[0,1].plot(t_lis,y2_lis)
    axis[0,1].set_title("Graph 2")
    axis[1,0].plot(t_lis,y3_lis)
    axis[1,0].set_title("Graph 3")
    axis[1,1].plot(t_lis,y4_lis)
    axis[1,1].set_title("Graph 4")
    pt.tight_layout()

# assigning FuncAnimation class to a variable for execution until variable is erased (program end)
Ani_exec = FuncAnimation(pt.gcf(), animate, interval=10)

pt.tight_layout()
pt.show()