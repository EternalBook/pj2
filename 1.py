import pandas as pd

abbrevs = pd.read_csv("./data/state-abbrevs.csv")
areas = pd.read_csv("./data/state-areas.csv")
population = pd.read_csv("./data/state-population.csv")
df_csv = pd.merge(abbrevs, population,left_on='abbreviation',right_on='state/region')
print(df_csv)
