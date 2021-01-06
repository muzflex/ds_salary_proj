# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:52:24 2021

@author: dell
"""

#This line will open a new chrome window and start the scraping.
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/dell/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 15, False, path, 15)
df