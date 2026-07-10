import matplotlib.pyplot as plt

from input_file import iphone_price

with open("input_file.py","r") as file:
    para= file.read().splitlines()

print(para[0])
# for data in para:
#     print(data)
# for data2 in para2:
#     print(data2)
# plt.plot(data,data2)
# plt.show()

