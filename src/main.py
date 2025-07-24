import csv

def load_chromebook_sn_db(file_path):
    chromebook_sn_db = {}
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            serial_number = row[1].strip().upper()
            ou_path = row[6].strip().upper()
            chromebook_sn_db[serial_number] = ou_path 

    return chromebook_sn_db

def load_chromebook_check_file(file_path):
    chromebook_check_db = {}
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
           location = row[0].strip().upper()
           serial_number = row[1].strip().upper()
           model = row[2].strip().upper()
           notes = row[3].strip().upper()

           chromebook_check_db[serial_number] = {
               "location": location,
               "serial_number": serial_number,
               "model": model,
               "notes": notes,
                "ou_path": "NOT FOUND"
           }
    return chromebook_check_db

def return_updated_chromebook_check_db(chromebook_check_db, chromebook_sn_db):
     for chromebook in chromebook_check_db.values():
        serial_number = chromebook["serial_number"]

        if chromebook.get("serial_number") in chromebook_sn_db:
            ou_path = chromebook_sn_db[serial_number]
            chromebook_check_db[serial_number]["ou_path"] = ou_path
        else:
            chromebook_check_db[serial_number]["ou_path"] = "Not Found"

def write_new_chromebook_check_file(file_path, chromebook_check_db):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for serial_number, data in chromebook_check_db.items():
            row = [
                data["location"],
                data["serial_number"],
                data["model"],
                data["notes"],
                data["ou_path"]
            ]
            writer.writerow(row)

def main(): 
    chromebook_db_file_path = 'input\phs_chromebooks_list.csv'
    input_file_path = 'input\input.csv'
    output_file_path = 'output\output.csv'

    chromebook_sn_db = load_chromebook_sn_db(chromebook_db_file_path)
    chromebook_check_db = load_chromebook_check_file(input_file_path)

    return_updated_chromebook_check_db(chromebook_check_db, chromebook_sn_db)
    write_new_chromebook_check_file(output_file_path, chromebook_check_db)




main()