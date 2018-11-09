import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet

data = pd.DataFrame()

start = 2014
end = 2018

for n in range(start, end + 1):
    file_name = '1320_' + str(n) + '.csv'
    data2 = pd.read_csv(file_name, skiprows=2, encoding="cp932", header=None,
                        names=['ds', 'Open', 'High', 'Low', 'Close', 'Volume', 'y'])
    data = data.append(data2)

model = Prophet()
model.fit(data)

future_data = model.make_future_dataframe(periods=200, freq='d')
future_data = future_data[future_data['ds'].dt.weekday < 5]
forecast_data = model.predict(future_data)

fig = model.plot(forecast_data)
model.plot_components(forecast_data)
plt.show()
