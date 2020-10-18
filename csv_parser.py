import csv

with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("parsed_names.csv", "w") as parsed_file:
        csv_writer = csv.writer(parsed_file, delimiter=" ")

        for line in csv_reader:
            if line[1] == "Stuart":
                csv_writer.writerow(line)
