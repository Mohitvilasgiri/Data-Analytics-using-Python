import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

dataset = pd.read_csv('weatherHistory.csv')

print(dataset)

#generate a reort

profile = ProfileReport(dataset)
profile.to_file(output_file="weatherHistory.html")