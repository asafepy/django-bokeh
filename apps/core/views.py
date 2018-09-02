from django.shortcuts import render, HttpResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import components
from .utils import make_plot, make_ajax_plot
from django.views.decorators.csrf import csrf_exempt
import json 
from django.http import JsonResponse
import numpy as np

x = 0
step = 0

def show_dashboard(request):

    plots = []
    # plots.append(make_plot())
    plots.append(make_ajax_plot())
    

    return render(request, 'dashboard/index.html', {'plots':plots})


@csrf_exempt
def data(request):
    global step

    if step == 12:
        step = 0


    # print(step)
    
    # main = map(curdoc(), 'cmems', int(step)) 


    global x
    x += 1
    y = np.sin(x)

    data = {
        "x": x, 
        "y": y
    }

    step += 1
    return JsonResponse(data)
