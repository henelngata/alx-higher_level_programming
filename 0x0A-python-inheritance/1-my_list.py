#!/usr/bin/python3
""" Module is documented"""


class MyList(list):
    """This class MyList"""

    def print_sorted(self):
        """orts and prints a list
        Yeilds:
            list: a asorted list
        """
        my_list = list(self)
        my_list.sort()
        print("{}".format(my_list))

    def __str__(self):
        """Return:
                A class string rep
        """
        return "Class MyList"
