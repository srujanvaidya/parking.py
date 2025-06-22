#code for 100 vehicle parking
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="unknown",

                                )
mycursor=mydb.cursor()
#mycursor.execute("create database parking")
#mycursor.execute("use parking")
#mycursor.execute("create table lot(slot int primary key, carno varchar(20)")


class Parking:
    def __init__(self):

        self.lot={i:"free" for i in range (1,101)}                       # makes every value in the dictionary free

    def park(self,carno):

        print("these are the available slots",self.lot)

        for j in range(1,101):

            if len(carno) == 10:                                       #cannot use car no less or more than 10 as per nameplate
                pass                                                         #car arrival

                if self.lot[j] == "free":
                    self.lot[j] = carno
                else:
                    continue
            else:
                print("not a valid no,redo it")

            print("\nCar parked at slot no:", j, self.lot)
            break

        if all(k=="occupied" for k in self.lot.values()):               # [.values] checks only value in the dictionary
                print("\nparking is full")
                print("\n no available slots")

    def depart(self):

        carex =str(input("Enter car no"))                              # departure of the car

        for k in range(1,101):

            if len(carex) == 10:
                if self.lot[k] == carex:
                    self.lot[k] = "free"
                else:

                 continue
        print("Empty slots",self.lot)

def main():

    p = Parking()
    while True:

        no=int(input("\n1:park\n2:depart\n3.quit app\nenter a val:"))
        match no:
            case 1:
                carno=str(input("enter the car no"))
                p.park(carno)

            case 2:
                p.depart()

            case 3:
                print("quit applicaiton")
                break



if __name__ == "__main__":
    main()








