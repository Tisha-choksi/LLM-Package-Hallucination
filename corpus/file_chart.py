import plotly.express as px
import pandas as pd
import numpy as np
import altair as alt
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import factorize

# Generate random data
np.random.seed(42)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=100),
    'Value1': np.random.randn(100),
    'Value2': np.random.randn(100) * 10,
    'Value3': np.random.rand(100) * 100
})

# Histogram
fig = px.histogram(data, x='Value1', nbins=30, title="Histogram of Value1")
fig.show()

# Scatter plot
scatter = alt.Chart(data).mark_point().encode(
    x='Value1',
    y='Value2',
    color='Category'
).properties(title="Scatter Plot of Value1 vs Value2")
scatter.show()

# Box plot (using bokeh's boxplot)
p = figure(title="Boxplot of Value1 by Category", x_axis_label='Category', y_axis_label='Value1')
p.boxplot(data, categories='Category', values='Value1', width=800, height=400)
show(p)