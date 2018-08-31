from weather import Weather, Unit
from datetime import datetime, timedelta

date_today = datetime.now()
days = pd.date_range(date_today, date_today + timedelta(9), freq='D')

np.random.seed(seed=1111)

weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('bento gonçalves')
forecasts = location.forecast
weather = [forecast.text for forecast in forecasts]
minima = [forecast.low for forecast in forecasts]
maxima = [forecast.high for forecast in forecasts]
tempo = {'forecast': weather, 'minima': minima, 
         'maxima': maxima, 'day': days.day, 
         'month': days.month, 'year': days.year,
         'hours': days.hour, 'minutes': days.minute}
tempo
