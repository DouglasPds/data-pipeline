import os
from datetime import date

import pandas as pd
from sqlalchemy import create_engine, text

today = date.today()

def readCsv(date=today):
  try:
    order_details = pd.read_csv("source/order_details.csv")
    newPathDay = "data/csv/{0}".format(date)
    if not os.path.exists(newPathDay):
      os.makedirs(newPathDay)
    order_details.to_csv("data/csv/{0}/order_details.csv".format(date))
  except Exception as e:
    print("Csv extract error: " + str(e))
  
readCsv()

def readSql(date=today):
  try:
    engine = create_engine("postgresql+psycopg2://northwind_user:thewindisblowing@localhost/northwind")
    queryGetNameTables = """SELECT TABLE_NAME
      FROM INFORMATION_SCHEMA.TABLES
      WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'public'"""
    tableListNames = pd.read_sql(text(queryGetNameTables), engine.connect())
    
    for row in tableListNames.to_numpy():
      nameTable = row[0]
      valueOfTable = pd.read_sql(nameTable, engine.connect())
      newPathDay = "data/postgres/{1}/{0}".format(date, nameTable)
      if not os.path.exists(newPathDay):
        os.makedirs(newPathDay)
      valueOfTable.to_csv("data/postgres/{1}/{0}/{1}.csv".format(date, nameTable))
  except Exception as e:
    print("Data extract error: " + str(e))
  
readSql()