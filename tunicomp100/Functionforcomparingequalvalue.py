"""
COMP.CS.100 A Function for Comparing Whether List Members Have an Equal Value¶
Creator: Ishan Malu
Student id number: 154138420
"""

def are_all_members_same(list):
    """
    this function takes a list as param and sees if all the values are the same
    """
    if len(list)==0:
        return True
    else:
        x= max(list)
        y= min(list)

        if x==y:
            return True
        else:
            return False



def main():
    pass

if __name__ == "__main__":
    main()