import os
import pandas as pd
import datetime as T
from dateutil.relativedelta import relativedelta
startDate = T.datetime(2019,9,1)
endDate = T.datetime(2020,9,30)
iterDate = startDate
df = pd.DataFrame()
while iterDate <= endDate:
    month_id = iterDate.strftime('%Y_%m')
    data = pd.read_csv('/Users/petercotton/github/microfilter/data/'+month_id+'.zip', compression='zip', header=0, sep=',', quotechar='"')
    df = df.append(data)
    print(month_id,':',len(df.index))
    iterDate += relativedelta(months=+1)
    print('Result dataset size:', len(df.index))

print('Result dataset size:', len(df.index))