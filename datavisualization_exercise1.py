import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [120, 150, 170, 160, 190]

plt.plot(months, sales, 
        color = 'green',
        linestyle = '--',
        marker = 's',
        markersize = 8,
        label = 'Sales'
         )

plt.title('Monthly Sales')
plt.legend()
plt.show()