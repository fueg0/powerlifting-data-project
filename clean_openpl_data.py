import os
from os import path
import csv

local_dir = os.getcwd() + "\\usapl"

required_labels = ["Name", "Sex", "Event", "Equipment", "BirthYear",
                   "BodyweightKg", "Best3SquatKg", "Best3BenchKg",
                   "Best3DeadliftKg", "TotalKg", "Place"]

with open('reordered.csv', 'a', encoding='utf-8', newline="") as outfile:
    # output dict needs a list for new column ordering
    writer = csv.DictWriter(outfile, fieldnames=required_labels,
                            extrasaction='ignore')
    # reorder the header first
    writer.writeheader()
    outfile.close()

with open('cleaned_data.csv', 'a', encoding='utf-8', newline="") as outfile:
    # output dict needs a list for new column ordering
    writer = csv.DictWriter(outfile, fieldnames=required_labels,
                            extrasaction='ignore')
    # reorder the header first
    writer.writeheader()
    outfile.close()


def filter_files():
    """
    Loops through data directories. If directories contain unnecessary data or
    are empty, a flag deletes the directories. Otherwise, if a needed
    directory contains extraneous files, the files are deleted.
    :return: None, a void function that returns
    """
    for subdir, dirs, files in os.walk(local_dir):
        this_folder = os.path.join(subdir)

        for file in files:
            cwd = os.path.join(subdir, file)

            if file == "entries.csv":
                with open(cwd, "r", encoding='utf-8') as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=",")

                    # loops through ONLY the first item, the column names, of
                    # each csv file and then determines if it should be
                    # removed before the loop breaks
                    for line in csv_reader:
                        good_meet = filter_csv(line)

                        if good_meet:
                            reorder_columns(cwd)
                        else:
                            pass
                        break

            else:
                pass


def filter_csv(csv_line):
    """
    Checks that a csv file for a meet represents a full-power meet and
    contains all needed headers
    :param csv_line: first line of a csv file
    :return: boolean
    """
    if set(required_labels).issubset(set(csv_line)):
        return True
    else:
        return False


def reorder_columns(file1):
    """
    Reorders columns using DictReaders/Writers to sort data quickly and easily
    :param file1: input file
    :return: void, edits other files
    """
    try:
        with open('reordered.csv', 'a', encoding='utf-8', newline='') \
                as outfile:
            writer = csv.DictWriter(outfile, fieldnames=required_labels,
                                    extrasaction='ignore')
            with open(file1, 'r') as infile:
                for row in csv.DictReader(infile):
                    # writes the reordered rows to the new file
                    writer.writerow(row)
    except UnicodeDecodeError as e:
        pass


def clean_csv():
    """
    Sorts through unneeded data in a file and adds relevant data to a new
    file.
    :return: void, modifies existing file
    """
    with open('cleaned_data.csv', 'a', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=required_labels,
                                extrasaction='ignore')
        with open('reordered.csv', 'r') as infile:
            for line in csv.DictReader(infile):
                if line['Event'] != "SBD":
                    pass
                elif line['Equipment'] != "Raw":
                    pass
                elif line['BodyweightKg'] == "":
                    pass
                elif line['Best3SquatKg'] == "":
                    pass
                elif line['Best3BenchKg'] == "":
                    pass
                elif line['Best3DeadliftKg'] == "":
                    pass
                elif line['TotalKg'] == "":
                    pass
                elif line['Place'] == "DQ" or line['Place'] == "DD" \
                        or line['Place'] == "":
                    pass
                else:
                    writer.writerow(line)


if __name__ == '__main__':
    filter_files()
    print("File filtering complete.")
    clean_csv()
    print("File cleaning complete.")