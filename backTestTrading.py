import backtrader
import datetime
from strategies import TestStrategy

# Cerebro is the main control center for backtrader
# Connect together data feed + strategy / Runs strategy against data feed
# https://backtrader.com/docu/quickstart/quickstart/
# Create an instance of cerebro
cerebro = backtrader.Cerebro()

#Set initial value of Portfolio 
cerebro.broker.setcash(1000.00)

# Create a Data Feed
data = backtrader.feeds.YahooFinanceCSVData(
    dataname='oracle_data.csv',

    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1),

    # Do not pass values after this date
    todate=datetime.datetime(2000, 12, 31),
    reverse=False)


# Connect data feed to cerebro
cerebro.adddata(data)

# Add strategy
cerebro.addstrategy(TestStrategy)

# Adds a broker by default e.g. cerebro.broker.getvalue()
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())