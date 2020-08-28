import alpaca_trade_api as tradeapi
import pandas as pd
from login import Login

# create username and password variables
login = Login()
username = login.get_username()
password = login.get_password()

