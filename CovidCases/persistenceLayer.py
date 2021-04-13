# Created by Gabriel Faustino de Araujo

import pandas as pd
from matplotlib import pyplot as plt


class Parent:
    """
    A class matching some of the column names in the .csv file.

    ...

    Attributes
    ----------
    id : str
    date : str
    cases : str
    deaths : str
    """

    def __init__(self, id, date, cases, deaths):
        self.id = id
        self.date = date
        self.cases = cases
        self.deaths = deaths

    # Necessary so printing the object returns the actual values instead of the memory address location
    def __str__(self):
        return str(self.id) + " " + str(self.date) + " " + str(self.cases) + " " + str(self.deaths)


class Child(Parent):
    """
        A class inheriting from the Parent class adding the last two column names to match the .csv file.

        ...

        Attributes
        ----------
        id : str
        date : str
        cases : str
        deaths : str
        name_fr : str
        name_en : str
        """

    def __init__(self, id, date, cases, deaths, name_fr, name_en):
        super().__init__(id, date, cases, deaths)
        self.name_fr = name_fr
        self.name_en = name_en

    # Necessary so printing the object returns the actual values instead of the memory address location
    def __str__(self):
        return super().__str__() + " " + str(self.name_fr) + " " + str(self.name_en)


# Creates an empty list
my_list = []


def load_list():
    """
    Populates the variable my_list with the first 100 rows in the InternationalCovid19Cases.csv file

    :return:
    """

    try:
        columns = ["id", "date", "cases", "deaths", "name_fr", "name_en"]
        reader = pd.read_csv('InternationalCovid19Cases.csv', skiprows=1, names=columns)
        df = pd.DataFrame(reader)

        # Append each row into an index of simpleList by looping all the .csv rows
        for row in df.itertuples(index=False):
            my_list.append(Child(row.id, row.date, row.cases, row.deaths, row.name_fr, row.name_en))

        # Trim the list and leave only 10.000 entries (from index 0 to 9999)
        del my_list[10000:]

    # Throws an exception if the file does not exist
    except FileNotFoundError:
        print("The .csv file could not be located.")


def new_csv_file():
    """
    Creates a new .csv file with the current data stored in the my_list variable
    :return:
    """

    my_list.insert(0, Child("id", "date", "cases", "deaths", "name_fr", "name_en"))
    df = pd.DataFrame(my_list)
    df.to_csv('UpdatedInternationalCovid19Cases.csv', index=False,header=False)


def display_list(selection):
    """
    Display either a specific index or the whole my_list variable
    :param selection: int
    :return:
    """

    # Checks if the user input is within range
    if selection > 100 or selection < 0:
        print('Row is out of reach, please choose between 1 and 100')
        return

    if selection <= 100 or selection >= 0:
        print('ID   Date     C D Name_FR Name_EN')

        # Prints the whole list
        if selection == 0:
            for row in my_list:
                print(str(row))

        # Prints the selected row
        else:
            print(my_list[selection-1])


def add_new_entry(id, date, cases, deaths, name_en, name_fr):
    """
    Appends a new index at the end of the my_list variable
    :param id: str
    :param date: str
    :param cases: str
    :param deaths: str
    :param name_en: str
    :param name_fr: str
    :return:
    """

    my_list.append(Child(id, date, cases, deaths, name_fr, name_en))


def edit_entry(entry, id, date, cases, deaths, name_fr, name_en):
    """
    Edit the values of a specific index in the my_list variable
    :param entry: int
    :param id: str
    :param date: str
    :param cases: str
    :param deaths: str
    :param name_fr: str
    :param name_en: str
    :return:
    """

    my_list[entry-1] = Child(id, date, cases, deaths, name_fr, name_en)


def delete_entry(entry):
    """
    Deletes a specific index in the my_list variable
    :param entry: int
    :return:
    """

    del my_list[entry-1]


def create_chart(entry):
    """
        Creates a bar chart with the sum of cases per country
        :param entry: int
        :return:
        """
    temp_list = my_list.copy()
    del temp_list[entry:]

    data = pd.DataFrame([t.__dict__ for t in temp_list])
    data.columns = ['id', 'date', 'cases', 'deaths', 'name_fr', 'name_en']
    datasum = data.cases.groupby(data.name_en).sum()
    plt.title("Bar Chat - Cases by Country")
    datasum.plot(kind='bar')
    plt.show()
