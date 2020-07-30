import pandas as pd
import plotly.graph_objs as go


def return_figures():
    """Creates 1 plotly visualization

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # first chart plots arable land from 1990 to 2015 in top 10 economies
  # as a line chart

    graph_one = []
    df = pd.read_csv('data/regionfile.csv')
    graph_one.append(
	go.Bar(
      x = df['State'],
      y = df['Count'],
      )
    )

    layout_one = dict(title = 'Number of Companies Breakdown by States (ODM Dataset)',
                yaxis = dict(title = 'Number of Companies'))

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))



    return figures
