import os
from datetime import date

import pandas as pd
from sqlalchemy import create_engine

today = date.today()

def load(date=today):
  try:
    engine = create_engine("mysql+pymysql://indicium_user:indicium_pass@localhost/northwind_data")
    tableListNames = os.listdir("data/postgres")
    for table in tableListNames:
      value = pd.read_csv("data/postgres/{1}/{0}/{1}.csv".format(date, table), index_col=0)
      value.to_sql(table, engine, if_exists='replace', index=False)
      print("Data successfully imported!")
  except Exception as e:
    print("Data load error: " + str(e))
  
  try:
    engine = create_engine("mysql+pymysql://indicium_user:indicium_pass@localhost/northwind_data")
    nameTable = "order_details"
    value = pd.read_csv("data/csv/{0}/{1}.csv".format(date, nameTable), index_col=0)
    value.to_sql(nameTable, engine, if_exists='replace', index=False)
    print("Data successfully imported!")
  except Exception as e:
    print("Data load error: " + str(e))
    
load()