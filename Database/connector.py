import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()
database=os.getenv("")

server = os.getenv("SERVER")
database = os.getenv("DATABASE")

# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
try:
    string_connection = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'
    cnxn = pyodbc.connect(string_connection)
    cursor = cnxn.cursor()
except Exception as ex:
    print("An exception has happened", ex.args)
    pass

