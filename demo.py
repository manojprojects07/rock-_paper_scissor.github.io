import numpy as np
import matplotlib.pyplot as plt 
languages = ['Python', 'C', 'Java', 'HTML']
students = [100, 30, 60, 25]
plt.pie(students, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()
