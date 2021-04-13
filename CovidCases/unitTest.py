# Created by Gabriel Faustino de Araujo

import unittest
import persistenceLayer


class Test(unittest.TestCase):
    def test_edit(self):

        # Loads the .csv in the list variable
        persistenceLayer.load_list()

        # Save the original value of index 75
        before = persistenceLayer.my_list[75]

        # The method asks for the row and not for the index, so I need to give 1 higher to match
        persistenceLayer.edit_entry(76, "BR", "2020-10-14", "27235", "749", "Brazil", "Bresil")

        # Save the new value of index 75
        after = persistenceLayer.my_list[75]

        # Compare and assert that they are not equal anymore
        self.assertNotEqual(str(before), str(after))


if __name__ == '__main__':
    unittest.main()
