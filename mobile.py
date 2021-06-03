import pandas as pd
import plotly.figure_factory as pff
import os

os.system('cls')

f = open('data.csv')

df = pd.read_csv('data.csv')

graph = pff.create_distplot([df["Avg Rating"].to_list()],["Sales"])
graph.show()

