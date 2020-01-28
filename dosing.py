import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv('t2_registry 20190619.csv').query('VISCODE != "bl" and SVPERF == "Y"')
data['Total'] = 1
df = pd.DataFrame(data)
ds = pd.DataFrame(data).groupby('VISCODE').count()

fig = px.pie(df, values='Total',names ='VISCODE',
             title='VISCODE from Registry', labels={'ID':'Total'}
            )
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
