from Database.connector import cursor
from csv import DictWriter


def GenerateCsvFromTable(table:str, filename: str = "file.txt"):
    results = cursor.execute(f"SELECT * FROM {table}").fetchall()
    with open(filename, "w", encoding="utf8", newline='') as f:
        headers = [header[0] for header in cursor.description]
        csvFile = DictWriter(f, fieldnames=headers)
        csvFile.writeheader()
        for result in results:
            print(result)
            values = [ value if not(value == None) else "" for value in result ]
            print(dict(zip(headers,values)))
            csvFile.writerow(dict(zip(headers,values)))
        f.close()

def GenerateCsvFromQuery(query:str, filename: str = "file.txt"):
    results = cursor.execute(query).fetchall()
    with open(filename, "w", encoding="utf8", newline='') as f:
        headers = [header[0] for header in cursor.description]
        csvFile = DictWriter(f, fieldnames=headers)
        csvFile.writeheader()
        for result in results:
            values = [ value if not(value == None) else "" for value in result ]
            csvFile.writerow(dict(zip(headers,values)))
        f.close()