import ipywidgets as widgets
from ipywidgets import Layout

def selectWidget(options,
 defaultIndex=0,
  description="Select input data: ",
   disabled = False,
    style= {'description_width': 'initial'}
	):

	return widgets.Select(
    options=options,
    value=options[0],
    description='Select input data:',
    disabled=False,
    style= {'description_width': 'initial'},
	layout=Layout(width='100%'),
	)
	