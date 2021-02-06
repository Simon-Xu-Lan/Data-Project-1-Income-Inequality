
import pandas as pd
from utility import PlotTools

income_data = pd.read_csv("./raw_data/income_Distribution_OECD_013021.csv")

PlotTools.check_columns(income_data, 5)