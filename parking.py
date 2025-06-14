
#code for 100 vehicle parkingz

class Parking:
    def __init__(self):
        self.lot={i:"free" for i in range (1,101)}                       # makes every value in the dictionary free

    def park(self):
        print("these are the available slots",self.lot)

        for j in range(1,101):


            if self.lot[j] == "free":
                self.lot[j] = "occupied"
            else:
                continue

            print("\nCar parked at slot no:", j, self.lot)
            break
        if all(k=="occupied" for k in self.lot.values()):                # [.values] checks only value in the dictionary
                print("\nparking is full")

def main():

    p = Parking()
    while True:

        no=int(input("1:park\n2:exit app\nenter a val:"))
        match no:
            case 1:
               p.park()

            case 2:
                print("quit application")
                break

if __name__ == "__main__":
    main()








