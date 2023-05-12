import plotly.graph_objs as go

categories = ['Category A', 'Category B', 'Category C']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[4, 3, 2],
    theta=categories,
    fill='toself',
    name='Product A'
))
fig.add_trace(go.Scatterpolar(
    r=[2, 5, 4],
    theta=categories,
    fill='toself',
    name='Product B'
))
fig.add_trace(go.Scatterpolar(
    r=[1, 2, 6],
    theta=categories,
    fill='toself',
    name='Product C'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 6]
        )),
    showlegend=True
)

fig.show()
