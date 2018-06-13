import numpy as np
import matplotlib.pyplot as plt
file = open('myout1.txt')

file = open("myout1.txt")  # 返回一个文件对象
list_acc = []
list_loss = []
for line in file:
    if line.find('Accuracy:') != -1:
        index_acc = line.find('Accuracy:')
        index_loss = line.find('Loss:')
        acc = line[index_acc+10:index_loss-2]
        loss = line[index_loss+6:len(line)-1]
        list_acc.append(acc)
        list_loss.append(loss)
        #print(acc)
        #print(loss)
print(list_acc)
print(list_loss)

plt.plot(list_acc[0:])
plt.plot(list_loss[0:])
#plt.savefig('result')
plt.show()
file.close()