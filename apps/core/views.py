from django.shortcuts import render, HttpResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import components
from .utils import make_plot, make_ajax_plot


x = 0

def show_dashboard(request):
    
    
    plots = []
    plots.append(make_ajax_plot())
    plots.append(make_plot())

    return render(request, 'index.html', {'plots':plots})


def data(request):
    global x
    x += 1
    y = 2**x
    return dict(x=x, y=y)
