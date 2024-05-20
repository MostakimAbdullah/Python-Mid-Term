class Star_Cinema():
    hall_list=[]
    def __init__(self) -> None:
        pass
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.__seats={}
        self.__show_list=[]

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.__show_list.append(show)
        seat=[[0 for i in range(self.cols)]for j in range(self.rows)]
        self.__seats[id]=seat 
    
    

    def book_seats(self, id, list):
        value=0
        if id in self.__seats.keys():
            value=self.__seats[id]
            for row, col in list:
                if value[row][col]==1:
                    print("Sorry,The seat is already booked \n")
                else:
                    value[row][col]=1
                    print("\n")
                    print("Congratulations for booking seat successfully \n")
                    print("============================")
                    for rows in range(self.rows):
                        for col in range(self.cols):
                
                            print(value[rows][col],end=" ")
                
                        print("\n")
        

    def view_show_list(self):
        for i in self.__show_list:
            print(i)
    
    def get_showlist(self):
        self.view_show_list()
    
    def view_available_seats(self,id):
        value=self.__seats[id]
        for rows in range(self.rows):
            for col in range(self.cols):
                
                print(value[rows][col],end=" ")
                
            print("\n")    
    def get_id(self,id):
        if id in self.__seats.keys():
            return True
        else:
            return False

    def get_available_seats(self,id):
        self.view_available_seats(id)        

        

        
hall=Hall(4,5,"Hall 5")
Starcine=Star_Cinema()
Starcine.entry_hall(hall)
hall.entry_show("101","Knight Riders","11.00 A.M")
hall.entry_show("333","Omar","2.00 P.M")
# list=[(1,1)]
# hall.book_seats("101",list)
# hall.view_show_list()
# hall.view_available_seats("101")
# list=[(0,0)]
# hall.book_seats("333",list)
# hall.view_available_seats("333")
# hall.book_seats("333",list)


while True:
    print("===============================\n")
    print(" Welcome to the Star Cineplex \n")
    print("===============================\n")
    print("Options\n")
    print("1: View all show today\n")
    print("2: View Available Seats\n")
    print("3: Book Ticket\n")
    print("4: Exit\n")

    option=int(input("Enter option: "))
    if option==1:
        print("Shows are Running now :\n")
        hall.get_showlist()
    elif option==2:
        print("Avalable seats are:")
        show_id=input("Enter the show_id : ")
        print("\n")
        if hall.get_id(show_id)==True:
            hall.get_available_seats(show_id)
        else:
            print("Wrong Id")


    elif option==3:
        print("Book Ticket")
        show_id=input("Enter the show_id: ")
        row=int(input("Enter the row no: "))
        col=int(input("Enter the column no: "))
        print("\n")
        if hall.get_id(show_id)==True:
            if row<0 or row>hall.rows and col<0 or col>hall.cols:
                print("Please provide valid number of seat")
            else:
                list=[(row,col)]
                hall.book_seats(show_id,list)

        else:
            print("Wrong Id")
        
    elif option==4:
        print("\n")
        print("Exit")
        break
