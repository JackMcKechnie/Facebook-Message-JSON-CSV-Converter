import json
import csv
import sys
import os


def output_file(source, destination, filename):
    # Import the file
    filename = source + "\\" + filename
    with open(filename, 'r') as file:
        data = json.load(file)

    # Initialise arrays to hold: who sent the message, when it was sent and the contents
    sender = []
    time = []
    content = []

    # Loop over every message in the JSON file
    for elt in data["messages"]:
        sender.append(str(elt["sender_name"]))
        time.append(str(elt["timestamp_ms"]))
        # Default content to [PHOTO/GIF/VIDEO]
        content.append(elt.get("content", "[PHOTO/GIF/VIDEO]"))

    out_arr = []
    for mess_num in range(len(sender)):
        out_arr.append([sender[mess_num], time[mess_num], content[mess_num]])

    with open(os.path.join(destination + "\\out.csv"), "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for elt in out_arr:
            writer.writerow(elt)


def main(source, destination, num_files):
    for i in range(num_files):
        infile = "message_" + str(i+1) + ".json"
        output_file(source, destination, infile)


main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
print()
print("Successfully converted " + sys.argv[3] + " files from JSON to CSV")

