import matplotlib.pyplot as plt
import pandas as pd

sales = pd.DataFrame({
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "cups_sold": [120, 135, 110, 145, 160, 210, 190]
})


plt.bar(sales["day"], sales["cups_sold"])

plt.xlabel("Day")
plt.ylabel("Cups Sold")
plt.title("Weekly Coffee Sales")

plt.xticks(rotation=45)

plt.show()

