"""
Nicholas Fiorito
30 March 2021
DS2001 Final Project
"""
import csv
import math
import os
from os import path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import clean_openpl_data

mens_weight_classes = {
    '59': (0, 59.0),
    '66': (59.001, 66.0),
    '74': (66.001, 74.0),
    '83': (74.001, 83.0),
    '93': (0, 93.0),
    '105': (93.001, 105.0),
    '120': (105.001, 120.0),
    '120+': (120.001, 500),
    'all': (0, 500)
}

womens_weight_classes = {
    '43': (0, 43.0),
    '47': (43.001, 47.0),
    '52': (47.001, 52.0),
    '57': (52.001, 57.0),
    '63': (57, 63.0),
    '69': (63.001, 69.0),
    '76': (69.001, 76.0),
    '84': (76.001, 84.0),
    '84+': (84.001, 500),
    'all': (0, 500)
}

categories = ["Name", "Sex", "Event", "Equipment", "BirthYear",
              "BodyweightKg", "Best3SquatKg", "Best3BenchKg",
              "Best3DeadliftKg", "TotalKg", "Place"]


def get_weight_class():
    """
    Asks user for input to get which weight class to analyze
    :return: str, representing the entered weight class from the user.
    """
    print("\nwhich weight class would you like to look at?\nMen's:")
    print(list(mens_weight_classes.keys()))

    print("\nOr Women's:")
    print(list(womens_weight_classes.keys()))

    weight_class = str.lower(
        input("Please input one of the above weight classes\n"))

    return weight_class


def get_lifter_sex(weight_class):
    """
    Gets the sex of the lifter based on the weight class entered.
    :param weight_class: A weight class represented in the mens_weight_classes
    dictionary or womens_weight_classes dictionary.
    :return: str, tuple, representing a sex ("M" or "F") and the tuple
    representing the weight range of their class.
    """
    if weight_class == "all":
        sex = input("would you like to see all weight classes for M or F?\n")
    elif weight_class in mens_weight_classes:
        sex = "M"
    elif weight_class in womens_weight_classes:
        sex = "F"
    else:
        print("Please re-run and enter a valid weight class.")
        exit(1)

    if sex == "M":
        weight_range = mens_weight_classes[weight_class]
    elif sex == "F":
        weight_range = womens_weight_classes[weight_class]

    return sex, weight_range


def standard_deviation(data, ddof=0):
    """
    Calculates standard deviation, sigma.
    :param data: Set of numerical data to find the standard deviation of
    :param ddof: degrees of freedom. Can be set to 1, but should not be for
    the purposes of this program
    :return: int representing the standard deviation of the data set
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - ddof)

    return math.sqrt(variance)


def make_lifters_list():
    """
    Makes a list of lifters of the correct sex and weight classes to be
    graphed.
    :return: list of ordered dictionaries, representing lifters who fit the
    criteria.
    """
    individuals = []

    with open("cleaned_data.csv", "r", encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=",")

        for lifter in csv_reader:
            if lifter["Sex"] == lifter_sex:
                if weight_class_range[0] < float(lifter["BodyweightKg"]) < \
                        weight_class_range[1]:
                    individuals.append(lifter)

    return individuals


def sort_by_totals(people, categories):
    """
    Sorts lifters into categories based on standard deviations of their total.
    :param people: List of lifters who fit the criteria for this category
    :param categories: The different standard deviation ranges for totals in
    this weight class
    :return: 2D list of lifters in each standard deviation bracket.
    """
    lifters_by_stdev = []
    for i in range(0, len(categories)):
        lifters_by_stdev.append([])

    for person in people:
        total = float(person["TotalKg"])
        i = 0
        for category in categories:
            if total > category[1]:
                i += 1
            else:
                lifters_by_stdev[i].append(person)

    return lifters_by_stdev


def make_brackets():
    """
    Creates the average makeups of the total in each standard deviation
    bracket.
    :return: void, modifies existing list
    """
    for bracket in sorted_lifters:
        bracket_size = len(bracket)
        squat_accumulation = 0
        bench_accumulation = 0
        deadlift_accumulation = 0

        for lifter in bracket:
            squat_accumulation += (float(lifter["Best3SquatKg"]) / float(lifter["TotalKg"])) * 100
            bench_accumulation += (float(lifter["Best3BenchKg"]) / float(lifter["TotalKg"])) * 100
            deadlift_accumulation += (float(lifter["Best3DeadliftKg"]) / float(lifter["TotalKg"])) * 100

        avg_squat_percent = round(squat_accumulation / bracket_size, 1)
        avg_bench_percent = round(bench_accumulation / bracket_size, 1)
        avg_deadlift_percent = round(deadlift_accumulation / bracket_size, 1)

        squat_percentages.append(avg_squat_percent)
        bench_percentages.append(avg_bench_percent)
        deadlift_percentages.append(avg_deadlift_percent)




if __name__ == "__main__":
    print("Would you like to reload the csv? \n\nPress Y if you have not run "
          "the program ever before. (this will take some time for the "
          "program to do before you can input more.)")
    redo = input("Y/N?\n")

    if redo == "Y":
        if path.exists("reordered.csv"):
            os.remove("reordered.csv")

        if path.exists("cleaned_data.csv"):
            os.remove("cleaned_data.csv")

        os.system('python clean_openpl_Data.py')
    else:
        pass

    weight = get_weight_class()
    lifter_sex, weight_class_range = get_lifter_sex(weight)

    lifters = make_lifters_list()

    total_of_totals = 0
    totals_list = []
    for lifter in lifters:
        totals_list.append(float(lifter["TotalKg"]))
        total_of_totals += float(lifter["TotalKg"])

    mu = total_of_totals / len(lifters)
    sigma = standard_deviation(totals_list)
    x1 = min(totals_list)
    x2 = max(totals_list)

    ranges = []
    range_item = x1
    while range_item < x2:
        last_number = range_item
        range_item += sigma
        ranges.append((round(last_number), round(range_item, 0)))

    range_limits = []
    for item in ranges:
        range_limits.append(item[0])

    sorted_lifters = sort_by_totals(lifters, ranges)

    squat_percentages = []
    bench_percentages = []
    deadlift_percentages = []

    make_brackets()

    bracket_percentages = [squat_percentages, bench_percentages,
                           deadlift_percentages]

    # handles for legend
    handles = [mpatches.Patch(color='green', label='Squat'),
               mpatches.Patch(color='orange', label='Bench'),
               mpatches.Patch(color='red', label='Deadlift')]

    width = 0.25
    bracket_nums = list(range(0, len(ranges)))
    plt.bar(np.arange(len(ranges)), bracket_percentages[0], color='green', width=width)
    plt.bar(np.arange(len(ranges)) + width, bracket_percentages[1], color='orange', width=width)
    plt.bar(np.arange(len(ranges)) + (width * 2), bracket_percentages[2], color='red', width=width)
    plt.xlabel("Range of Total (up to, but not including next tickmark)")
    plt.xticks(bracket_nums, range_limits)
    plt.ylabel("Percent of Total")
    plt.yticks(np.arange(10, 101, 10), np.arange(10, 101, 10))
    plt.title("Percent of Total Made up by Lifts in Powerlifting")
    plt.legend(handles=handles,
               loc='upper right', borderaxespad=0.1)
    plt.show()
