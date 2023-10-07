# import the necessary libraries
import pandas as pd
import numpy as np
from autoviz.AutoViz_Class import AutoViz_Class

filename = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csvhttps://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv'
data = pd.read_csv(filename)

av = AutoViz_Class()
av.AutoViz(data)
