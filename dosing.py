import pandas as pd

import plotly.graph_objects as go

data = pd.read_csv('t2_registry 20190619.csv').query('VISCODE != "bl" and SVPERF == "Y"')
data['Total'] = 1
df = pd.DataFrame(data)

fig = go.Figure(go.Pie(
    name='',
    values=df['Total'],
    labels=df['VISCODE'],
    text=df['VISCODE'],

    hovertemplate="VISCODE: %{label} <br>Percentage: %{percent}  "
))
fig.update_layout(
    title='VISCODE from Registry',

    font=dict(

        size=18,
        color="#7f7f7f"

    )
)
fig.show()
