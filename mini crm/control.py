from idlelib import query
from pathlib import Path
import json,csv

DATA_DIR=(Path(__file__).resolve().parent/"data")
DB_PATH=DATA_DIR/"leads.json"

#CRUD

#CREATE
#READ
#UPDATE
#DELETE

#READ

def read_leads():
    if not DB_PATH.exists():
        return[]

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:

      return []



def create_lead(lead_dict):

    leads=read_leads()  #lista de dicionarios de leads
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=4), encoding="utf-8")

# Export leads as csv
def export_csv():

    """Exporta as leads para CSV e RETORNA o caminho do arquivo criado"""

    path_csv=DATA_DIR/"leads.csv"

    leads= read_leads() # LISTA - ARRAY!!

    try:
        with path_csv.open("w",newline="",encoding="utf-8") as file_csv:
            writer=csv.DictWriter(file_csv, fieldnames=leads[0].keys())
            writer.writeheader()

            for row in leads:
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None

# READ LEADS FROM QUERY/SEARCH
def read_leads_search(query):
    leads=read_leads()
    results=[]

    for i, lead in enumerate(leads):
        txt_lead=f"{lead["Name"]} {lead['email']} {lead['company']}".lower()
        #print(txt_lead)

        if query.lower() in txt_lead:
            results.append((i,lead))

    return results

print(read_leads_search("fiap"))