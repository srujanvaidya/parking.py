#code for 100 vehicle parking

class Parking:
    def __init__(self):
        self.lot={i:"free" for i in range (1,101)}

    def park(self):
        for j in range(1,101):
            if self.lot[j]=="free" :
               self.lot[j]="occupied"
            else:
                continue
            print("car parked at slot no:",j,self.lot)
            break


def main():
    p = Parking()
    while True:
        no=int(input("1:park\n2:exit app\nenter a val for the task to perform:"))
        match no:
                case 1:
                   p.park()

                case 2:
                    print("quit application")
                    break

if __name__ == "__main__":
    main()








