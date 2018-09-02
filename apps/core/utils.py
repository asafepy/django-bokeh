from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models.sources import AjaxDataSource
from bokeh.resources import CDN

def make_plot():
    plot = figure(plot_height=300, sizing_mode='scale_width')

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]

    plot.line(x, y, line_width=4)

    script, div = components(plot, CDN)
    return script, div

def make_ajax_plot():
    source = AjaxDataSource(data_url='http://localhost:9000/data/',
                            polling_interval=2000, mode="append")

    source.data = dict(x=[], y=[])

    plot = figure(plot_height=300, sizing_mode='scale_width')
    plot.line('x', 'y', source=source, line_width=4)

    script, div = components(plot, CDN)
    return script, div
