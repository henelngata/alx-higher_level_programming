#!/usr/bin/python3

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
