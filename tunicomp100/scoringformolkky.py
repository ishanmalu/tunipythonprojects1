"""
COMP.CS.100 Scoring for Mölkky
Creator: Ishan Malu
Student id number: 154138420
"""

class Player:
    def __init__(self, name):
        self.__name= name
        self.__pts=0
        self.__avg=0
        self.__turn=0
        self.__success=0
        self.__sum=0

    def avg(self,points):
        average= self.__sum/self.__turn
        if points> average and self.__turn>1:
            print(f"Cheers {self.__name}!")


    def get_name(self):
        return self.__name

    def rate(self):
        if self.__success==0:
            return 0
        else:
            val = (self.__success/self.__turn)
            return val*100

    def add_points(self,points):
        self.__pts += points
        self.__turn +=1
        self.__sum += points

        if points>0:
            self.__success +=1

        if 40 <= self.__pts <= 49:
            x= 50- self.__pts
            print(f"{self.__name} needs only {x} points. It's better to avoid knocking down the pins with higher points.")
        elif self.__pts > 50:
            self.__pts = 25
            print(f"{self.__name} gets penalty points!")

    def has_won(self):
        if self.__pts == 50:
            return True
        else:
            return False

    def get_points(self):
        return self.__pts

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        in_turn.avg(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.rate():.1f}")  # TODO: d)
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.rate():.1f}") # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()