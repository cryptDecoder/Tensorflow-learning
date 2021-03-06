import plotly.express as px


def animatedGraph():
    df = px.data.gapminder()

    fig = px.bar(df, x="continent", y="pop", color="continent",
                 animation_frame="year", animation_group="country", range_y=[0, 4000000000])
    fig.show()
