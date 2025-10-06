import json
import csv
from pathlib import Path

my_path = Path.cwd().joinpath("incident.json") # definerer hvor den finder json filen, så det virker på alles maskiner

# starter med en try except for at se om filen findes
try:
    with open(my_path, "r") as f:
        data = json.load(f)
        alerts = data["alerts"]
except:
    print(f"file : {my_path} not found or something else went wrong")
    exit()


def filecsv(file_name, data_field): # laver en funktion så vi ikke behøver at skrive koden fire gange
    with open(file_name, "w", newline= "") as filea:
        writer = csv.writer(filea, quoting=csv.QUOTE_ALL) # quoting fundet på geekforgeeks for at lave "" mellem alle datapunkter
        writer.writerow(["alertId", "machineId", "firstActivity", data_field])
        for alert in alerts:
            alert_id = alert["alertId"]
            machine_id = alert["machineId"]
            first_activity = alert["firstActivity"]
            
            # laver en try except for at sikre programmet ikke giver fejl hvis en af "entities" mangler
            try:
                for field in alert["entities"][data_field]: # for loop til at skrive alle rows udover header
                    writer.writerow([alert_id, machine_id, first_activity, field])
            except:
                print(f'"{data_field}" not found in : {alert_id}\n{alert_id} not writen to {file_name}')
                pass
            

# kalder fire funktioner for at få de 4 csv filer
filecsv("alert_domain.csv", "domains")
filecsv("alert_fileHashes.csv", "fileHashes")
filecsv("alert_ips.csv", "ips")
filecsv("alert_processes.csv", "processes")

# ________________________________________________________________________________________________

# lave det hele i et loop, i stedet for at kalde funktionen 4 gange

# csv_files = {
#     "domains" : "alert_domain.csv",
#     "fileHashes" : "alert_fileHashes.csv",
#     "ips" : "alert_ips.csv",
#     "processes" : "alert_processes.csv"
# }

# for fields in csv_files:
#     filename = csv_files[fields]

# for field, filename in csv_files.items():
#     filecsv(filename, field, field)
#     print(f"created af csv file [{filename}] at : {Path.cwd()}")