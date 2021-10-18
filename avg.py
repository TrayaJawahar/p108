import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff 
df=pd.read_csv("project.csv")

fig=ff.create_distplot([df["AvgRating"].tolist()] ,["RESULT"] , show_hist=False)
fig.show()