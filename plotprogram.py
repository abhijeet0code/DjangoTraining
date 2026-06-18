import matplotlib.pyplot as plt

#Plotting the price of I phone over the year.
iphone_price=[50000,67000,82000,130000,135000]
samsung_price=[30000,44000,52000,90000,150000]
year=[2016,2018,2020,2022,2024]

plt.plot(year,iphone_price,color='green',label='IPhone Price',linestyle='--',linewidth=3)
plt.plot(year,samsung_price,color='blue',label='Samsung Price',linestyle='--')
plt.title("Price of the phones over the year")
plt.xlabel("Year")
plt.ylabel("Price")

plt.show()
