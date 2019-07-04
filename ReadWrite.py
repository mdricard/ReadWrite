'''
This example is from Python for the Lab
https://www.pythonforthelab.com/blog/introduction-to-storing-data-in-files/
'''
import numpy as np

x = np.linspace(0, 1, 201)
y = np.random.random(201)

data = np.column_stack((x, y))

# save a simple text file
header = "X-Column, Y-Column\n"
np.savetxt('D:\AB_data.dat', data, header=header)

# now read the text file
data = np.loadtxt('D:\AB_data.dat')
x = data[:, 0]
y = data[:, 1]

# now save tab delimited version
with open('D:\BD_data.txt', 'w') as f:
    for i in range(len(x)):
        f.write('{:4.1f}\t{:.4f}\n'.format(x[i], y[i]))   # tab delimited
    f.close()

# using with to read
with open('D:\BD_data.txt', 'r') as f:
    line = f.readline()
    header = []
    u = []
    v = []
    while line:
        if line.startswith('#'):
            header.append(line)
        else:
            data = line.split('\t')
            u.append(float(data[0]))
            v.append(float(data[1]))
        line = f.readline()
