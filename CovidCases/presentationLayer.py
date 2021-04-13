# Created by Gabriel Faustino de Araujo

import businessLayer


def menu():
    """
    The menu responsible for doing all the interaction with the user

    :return:
    """

    print("\nOptions:\n"
          + "\n\t1 - Reload the data from the dataset, replacing the in-memory data."
          + "\n\t2 - Persist the data from memory to the disk as a comma-separated file, writing to a new file."
          + "\n\t3 - Select and display either one record, or display all records from the in-memory data."
          + "\n\t4 - Create a new record and store it in the simple data structure in memory"
          + "\n\t5 - Select and edit a record held in the simple data structure in memory"
          + "\n\t6 - Select and delete a record from the simple data structure in memory"
          + "\n\t7 - Create a bar chart of the simple data structure"
          + "\n\t0 - To exit the program\n")

    user_input = int(input("Choose an option: "))

    while user_input != 0:
        if user_input == 1:
            businessLayer.reload()
            menu()

        if user_input == 2:
            businessLayer.create_csv_file()
            menu()

        if user_input == 3:
            row_input = int(input("Choose which row you want to see (choose 0 to see all rows): "))
            print(" ")
            businessLayer.display_data(row_input)
            menu()

        if user_input == 4:
            id_input = str(input("Type the ID of the Country: "))
            date_input = str(input("Type the date of the entry (yyyy-mm-dd): "))
            cases_input = str(input("Type the number of cases: "))
            deaths_input = str(input("Type the number of deaths: "))
            name_fr_input = str(input("Type the Country name in French: "))
            name_en_input = str(input("Type the Country name in English: "))
            businessLayer.select_create(id_input, date_input, cases_input, deaths_input, name_fr_input, name_en_input)
            menu()

        if user_input == 5:
            row_input = int(input("Type the row number that you wish to edit: "))
            id_input = str(input("Type the ID of the Country: "))
            date_input = str(input("Type the date of the entry (yyyy-mm-dd): "))
            cases_input = str(input("Type the number of cases: "))
            deaths_input = str(input("Type the number of deaths: "))
            name_fr_input = str(input("Type the Country name in French: "))
            name_en_input = str(input("Type the Country name in English: "))
            businessLayer.select_edit(row_input, id_input, date_input, cases_input, deaths_input, name_fr_input, name_en_input)
            menu()

        if user_input == 6:
            row_input = int(input("Type the row number that you wish to delete: "))
            businessLayer.select_delete(row_input)
            menu()

        if user_input == 7:
            records_input = int(input("Enter number of records between 0 - 4000 to generate a bar chart: "))
            businessLayer.display_chart(records_input)
            menu()

        else:
            print("Thanks for using this program, have a nice day!")
            exit()


if __name__ == '__main__':
    menu()
