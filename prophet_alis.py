import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

data = pd.DataFrame()

file_name = 'alis.csv'
# use `ds` and `y` for fb prophet => https://facebook.github.io/prophet/docs/quick_start.html#python-api
csv_data = pd.read_csv(file_name, skiprows=1, encoding="cp932", header=None,
                       names=['ds', 'Open', 'High', 'Low', 'y', 'Volume', 'Market Cap'])
data = data.append(csv_data)

model = Prophet()
model.fit(data)

future_data = model.make_future_dataframe(periods=100, freq='d')
#future_data = future_data[future_data['ds'].dt.weekday < 5]
forecast_data = model.predict(future_data)

fig = model.plot(forecast_data)
model.plot_components(forecast_data)
plt.show()
