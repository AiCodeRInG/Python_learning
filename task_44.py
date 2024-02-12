import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head(20)
for col in data['whoAmI'].unique():
    data.loc[data['whoAmI'] == col, col] = "1"
    data.loc[data['whoAmI'] != col, col] = "0"
data.head(20)
