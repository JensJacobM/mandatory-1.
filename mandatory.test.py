import json
import csv
from pathlib import Path

my_path = Path.cwd().joinpath("incident.json")
try:
    with open(my_path, "r") as f:
        data = json.load(f)
        alerts = data["alerts"]
except:
    print(f"file : {my_path} not found")
    exit()

csv_files = {
    "domains" : "alert_domain.csv",
    "fileHashes" : "alert_fileHashes.csv",
    "ips" : "alert_ips.csv",
    "processes" : "alert_processes.csv"
}
for fields in csv_files:
    filename = csv_files[fields]

def filecsv(name, header, input1):
    with open(name, "w", newline= "") as filea:
        writer = csv.writer(filea, quoting=csv.QUOTE_ALL)
        writer.writerow(["alertId", "machineId", "firstActivity", header])
        for alert in alerts:
            alert_id = alert["alertId"]
            machine_id = alert["machineId"]
            first_activity = alert["firstActivity"]
            
            for domain in alert["entities"][input1]:
                writer.writerow([alert_id, machine_id, first_activity, domain])


# filecsv("file_1.csv", "domains", "domains")
# filecsv("file_2.csv", "filehashes", "fileHashes")
# filecsv("file_3.csv", "ips", "ips")
# filecsv("file_4.csv", "processes", "processes")

for field, filename in csv_files.items():
    filecsv(filename, field, field)