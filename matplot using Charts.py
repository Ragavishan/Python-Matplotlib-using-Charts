#!/usr/bin/env python
# coding: utf-8

# # DATA VISUALIZATION 

# ## Matplotlib

# ### 1. Histogram Chart

# In[18]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.array([1, 5, 2, 8, 3, 2, 7, 4, 3, 8])

# Creating histogram
plt.hist(data, bins=5, edgecolor='black')

# Adding title and labels
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Displaying the plot
plt.show()


# ### 2. Bar Chart

# In[19]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 5, 2, 8, 3])
y = np.array([2, 7, 4, 3, 8])

# Creating bar chart
plt.bar(x, y, color='blue', edgecolor='black')

# Adding title and labels
plt.title('Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()


# ### 3. Scatter Plot

# In[20]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Creating scatter plot
plt.scatter(x, y, color='red', marker='o')

# Adding title and labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()


# ### 4.Pie Chart

# In[21]:


import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Creating pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Adding title
plt.title('Pie Chart')

# Displaying the plot
plt.show()


# ### 5. Bubble Chart

# In[22]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.random.rand(10)
y = np.random.rand(10)
sizes = np.random.rand(10) * 1000  # Bubble sizes
colors = np.random.rand(10)  # Bubble colors

# Creating bubble chart
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')

# Adding title and labels
plt.title('Bubble Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.colorbar()  # Show color scale
plt.show()


# ### 6. Area Chart

# In[23]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 6)
y = np.array([1, 4, 6, 8, 4])

# Creating area chart
plt.fill_between(x, y, color="skyblue", alpha=0.4)
plt.plot(x, y, color="Slateblue", alpha=0.6)

# Adding title and labels
plt.title('Area Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()


# ### 7. Box Plot

# In[24]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [np.random.normal(0, 1, 100), np.random.normal(5, 1.5, 100)]

# Creating box plot
plt.boxplot(data)

# Adding title and labels
plt.title('Box Plot')
plt.xlabel('Groups')
plt.ylabel('Values')

# Displaying the plot
plt.show()


# ### 8. Head Map

# In[26]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 10)

# Creating heat map
plt.imshow(data, cmap='viridis', interpolation='nearest')

# Adding color bar
plt.colorbar(label='Values')

# Adding title and labels
plt.title('Heat Map')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()


# In[ ]:




