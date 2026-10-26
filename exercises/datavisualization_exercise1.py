import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# sales = [120, 150, 170, 160, 190]

# plt.plot(months, sales, 
#         color = 'green',
#         linestyle = '--',
#         marker = 's',
#         markersize = 8,
#         label = 'Sales'
#          )

# plt.title('Monthly Sales')
# plt.legend()
# plt.show()


# subjects = ['Math', 'Physics', 'Chemistry', 'Biology']
# scores = [85, 78, 92, 88]

# plt.plot(subjects, scores,
#         color = 'red',
#         marker = '*',
#         linewidth = 3,
#         markerfacecolor = 'yellow',
#         label = 'Scores'
                
#         )
# plt.title("Examn Scores")
# plt.legend()
# plt.show()


# years = [2021, 2022, 2023, 2024]
# revenue = [500, 700, 850, 1000]



# plt.plot(years, revenue,
#         color = 'blue',
#         marker = 'D',
#         linestyle = ':',
#         label = 'Revenue'
                
#         )
# plt.title("company Revenue Over Years")
# plt.legend()
# plt.show()

fruits = ['Apple', 'Banana', 'Cherry', 'Date']
counts = [50, 30, 20, 10]
colors = ['red', 'yellow', 'pink', 'brown']

bars = ax.bar(fruits,  counts, color = colors)
ax.set_title("Fruit Supply")
ax.set_ylabel("Quantity")

ax.legend("Fruits")
plt.show()