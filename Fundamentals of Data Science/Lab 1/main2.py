import pandas as pd

URL = "http://exoplanets.org/csv-files/exoplanets.csv"

df = pd.read_csv(URL, low_memory=False)

# drop rows containing missing values
df = df[['NAME', 'MSINI', 'A']].dropna()

# i don't like orignal columns names
df = df.rename(columns={'NAME': 'Name',
                        'MSINI':'Mass',
                        'A': 'Distance'}).set_index('Name').astype(float)

# some masses are not missing but equal to zero, let's get rid of them too
df = df.drop(df[df['Mass'] == 0].index)

# # make it look appealing
df_styled = df.sample(7).style.background_gradient(axis=0,
                                                   gmap=df['Mass'],
                                                   cmap='cividis')
dfi.export(df_styled, 'filename.png', dpi=300)