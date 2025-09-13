"""
COMP.CS.100A Function for Reviewing a List's Order of Magnitude
Creator: Ishan Malu
Student id number: 154138420
"""

def is_the_list_in_order(list):
    """
     this function works in a way
    """
    if len(list)>0:
        revList= list.copy()
        list.sort()
        if revList == list:
            return True
        else:
            return False
    else:
        return True


def main():
    pass

if __name__ == "__main__":
    main()