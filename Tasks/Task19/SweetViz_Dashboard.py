# import the necessary libraries
import pandas as pd
import sweetviz as sv

df = pd.read_csv('C:\\Users\\pc\\Documents\\GitHub\\AI_Diploma_Tasks\\Tasks\\Task20\\netflix1.csv')

# analyzing the dataset
netflix_dashboard = sv.analyze(df)

# display the report
netflix_dashboard.show_html('netflix.html')
