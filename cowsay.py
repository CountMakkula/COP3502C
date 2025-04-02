#Cow say program
#Import libraries
import sys
from heifer_generator import get_cows
from dragon import Dragon


#List cows function
def list_cows(cows):
    CowList = ""
    print("Cows available:", end=" ")
    for i in cows:
        CowList += f"{i.name} "
    return CowList[:-1]

#Find cow function
def find_cow(name, cows):
    for i in cows:
        if i.name == name:
            return i.image, i
    return None

#Main function
def main():
    # -l command
    if sys.argv[1] == "-l":
        print(list_cows(get_cows()))
    # -n command
    elif sys.argv[1] == "-n":
        SelectedCow = find_cow(sys.argv[2], get_cows())
        if SelectedCow[0] is None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            Message = ""
            for i in sys.argv[3:]:
                Message += f"{i} "
            print(Message[:-1])
            print(SelectedCow[0])
            if isinstance(SelectedCow[1], Dragon):
                if SelectedCow[1].can_breath_fire():
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
    # Message
    else:
        Message = ""
        for i in sys.argv[1:]:
            Message += f"{i} "
        print(Message[:-1])
        print(get_cows()[0].image)

if __name__ == "__main__":
        main()
