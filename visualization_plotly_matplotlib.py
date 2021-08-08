import plotly.express as px
import matplotlib.pyplot as plt

#Plotly
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()

# Matplotlib
X = [0, 2, 4]

fig, ax = plt.subplots()
ax.plot(X, X, label='linear')
ax.plot(X, [x ** 2 for x in X], label='quadratic')
ax.plot(X, [x ** 3 for x in X], label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()

plt.show()
