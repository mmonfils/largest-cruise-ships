# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:56:23 2021

@author: mmonf
"""

import pandas as pd
import requests

"""
Writing a script to retrieve and locally save the data from the Wikipedia
website. The script below is for 'In Service' cruise ships.
"""

url = "https://en.wikipedia.org/wiki/List_of_largest_cruise_ships"

r = requests.get(url)
df_list = pd.read_html(r.text)
df = df_list[0]
df.to_csv('largest_cruise_ships.csv', index=False)


"""
Writing a script to retrieve and locally save the data from the Wikipedia
website. The script below is for 'On Order' cruise ships.
"""

url = "https://en.wikipedia.org/wiki/List_of_largest_cruise_ships"

r = requests.get(url)
df_list = pd.read_html(r.text)
df = df_list[1]
df.to_csv('largest_on_order_ships.csv', index=False)
