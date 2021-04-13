# Created by Gabriel Faustino de Araujo

import persistenceLayer


def reload():
    """
    Calls the method in the persistence file responsible for populating the in memory list

    :return:
    """

    persistenceLayer.load_list()
    print("\nLoaded to the memory the first 100 rows from InternationalCovid19Cases.csv")


def create_csv_file():
    """
    Calls the method in the persistence file responsible for creating a new .csv file with the in memory data

    :return:
    """

    persistenceLayer.new_csv_file()
    print("\nA new file called UpdatedInternationalCovid19Cases.csv has been created with the current in memory data")


def display_data(row):
    """
    Calls the method in the persistence file responsible for outputting the row selected

    :param row:
    :return:
    """

    persistenceLayer.display_list(row)


def select_create(id, date, cases, deaths, name_en, name_fr):
    """
    Calls the method in the persistence file responsible for creating a new row

    :param id:
    :param date:
    :param cases:
    :param deaths:
    :param name_en:
    :param name_fr:
    :return:
    """

    persistenceLayer.add_new_entry(id, date, cases, deaths, name_en, name_fr)
    print("\nRow {0} successfully added.".format(len(persistenceLayer.my_list)))


def select_edit(row, id, date, cases, deaths, name_fr, name_en):
    """
    Calls the method in the persistence file responsible for editing a existing row

    :param row:
    :param id:
    :param date:
    :param cases:
    :param deaths:
    :param name_fr:
    :param name_en:
    :return:
    """

    persistenceLayer.edit_entry(row, id, date, cases, deaths, name_fr, name_en)
    print("\nRow {0} successfully edited.".format(row))


def select_delete(row):
    """
    Calls the method in the persistence file responsible for deleting a existing row
    :param row:
    :return:
    """

    persistenceLayer.delete_entry(row)
    print("\nRow {0} successfully deleted.".format(row))


def display_chart(choice):
    persistenceLayer.create_chart(choice)
