# ___________________________________________________-
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os 
from functools import partial



# This is for Window initialization
# This is our perent class 
# ___________________________________________________-
class Window:
    def __init__(self):
        self.root = Tk()

        #  Here we have encapsultaion 
        # here we access modifier so this attribute can not be used by any class 

        self.__geometry= self.root.geometry("1600x1600")
        self.__title = self.root.title("Hotel management system")
    
        self.imageDirecticon1 =  PhotoImage(file="./icon1.png")
        self.imageDirecticon2 =  PhotoImage(file="./icon2.png")
        self.imageDirecticon3 =  PhotoImage(file="./icon3.png")
        self.imageDirecticon4=  PhotoImage(file="./icon4.png")
    
# ___________________________________________________-
  
  

# This is our derived class 
class Gui(Window):
    def __init__(self):
        super().__init__()

        

        


        self.indicationalvariable= None
        self.mydb = mysql.connector.connect(
            host="localhost",
            user = "root",
            password= "baqarzafarfarooqui2021",
            database = "hotelm"
        )
        self.firstDisplay()
        self.temporrayStoringArray = []
        
       # This is for our password Authenticator        
        



      

# ___________________________________________________-
    def firstDisplay(self):
        self.mainmainFrame = Frame(self.root , width= 2000 , height=2000 ,bg="#E1EBEE")
        self.mainmainFrame.pack()
        self.mainmainFrame.pack_propagate(False)
        Label(self.mainmainFrame , text= "Password Required" , font=100  , bg="#E1EBEE" , fg="black").pack(pady= (200 , 1))
        self.password = Entry(self.mainmainFrame , show = "*", width= 30 , font=("serif" , 20 ) )
        self.password.pack(pady=(20 , 0))
        self.newbutton = Button(self.mainmainFrame , text="Log in " , bg="#008080" , command=self.passwordes , font= 20 , width=5 , bd=0)
        self.newbutton.pack(pady= 20)
        # This for event handle whenever we press enter key password function will run 
        self.password.bind("<Return>" , self.passwordes)









# ___________________________________________________-
    def logout(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.firstDisplay()
        
# ___________________________________________________-
      
    def passwordes(self , event ):
        P = self.mydb.cursor()
        P.execute("select password from password ")
        password = P.fetchall()
        self.mydb.commit()
        
        if self.password.get() == password[0][0]:
            self.create_widgets()
            self.dashboard()
            self.password.destroy()
            self.newbutton.destroy()
            self.mainmainFrame.destroy()
        else:
            messagebox.showwarning("wrong password" ,"You are Entering Wrong Password" )

       
    
    
# ________________________________________________________________________________________________________-
    def create_widgets(self):
        
        self.navebar()
        self.header()
        self.Contents()





        

#________________________________________________________________________________________________________________

    def Check(self):
         
        # This data is comming from database 
        T = self.mydb.cursor()
        T.execute("select ROOMNUMBER from roombooking")
        dataa = T.fetchall()
        

        # Here we adding restriction so the same room cannot be given ;
        # self.ShowingdataBeforeStoring()
        for x in dataa :
            if x[0] != int(self.Roomnumber.get()):
                self.ShowingdataBeforeStoring()
            else:
                messagebox.showwarning("Not available" , "This room is not available")
        

       
# __________________________________________________________________________________________________________   
    def ShowingdataBeforeStoring(self):
        self.address1 =   self.address.get()
        self.Entryforname1 =  self.Entryforname.get()
        self.nic1 = self.nic.get()
        self.numberofday1 = self.numberofday.get()
        self.phonenumber1 = self.phonenumber.get()
        self.Typeofroom1 = self.Typeofroom.get()
        self.Roomnumber1 =  self.Roomnumber.get()
        
      
        self.temporrayStoringArray.append(self.Entryforname1) #0
        self.temporrayStoringArray.append(self.nic1)#1
        self.temporrayStoringArray.append(self.address1)#2
        self.temporrayStoringArray.append(self.Typeofroom1)#3
        self.temporrayStoringArray.append(self.phonenumber1)#4
        self.temporrayStoringArray.append(self.numberofday1)#5
        self.temporrayStoringArray.append(self.Roomnumber1)#6
        
        T = self.mydb.cursor()
        T.execute(f"select {self.Typeofroom1.upper() } from typesofrooms")
        
        dataofroomtype =   T.fetchall()[0][0]
        Total = dataofroomtype * int(self.numberofday1)
        
        self.temporrayStoringArray.append(Total)#7
        self.Cashpayment()
    

# __________________________________________________________________________________________

   # This method is to store the values of
   
    def sumittomysql(self):
        

        

        
        name = self.temporrayStoringArray[0]
        nic = self.temporrayStoringArray[1]
        address = self.temporrayStoringArray[2]
        typesofroom =  self.temporrayStoringArray[3]
        phonenumber = self.temporrayStoringArray[4]
        roomnumber = self.temporrayStoringArray[6]
        numberofdays = self.temporrayStoringArray[5]
        Amount = self.temporrayStoringArray[7]
        messagebox.showinfo("Information","Record of this guest has seccessfully added")   
        mycursor =self.mydb.cursor()
        mycursor.execute("update roomandhall set Rooms = Rooms - 1 ")
        self.mydb.commit()
        mycursor.execute("""
          INSERT INTO roombooking (name, NIC, address, phonenumber, typeofroom, numberofdays, ROOMNUMBER, amount)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
           """, (name, nic, address, phonenumber, typesofroom, numberofdays, roomnumber, Amount))
        self.mydb.commit()
     
          

        
         


   
# __________________________________________________________________________________________________-
    def navebar(self):

        def indication(a):
            print(a)
            


        def DashA(a,b , c , d , e , f ,g):
            print("Dash")
           
            for frame in self.frame4.winfo_children():
                frame.destroy()
            
            
            self.dashboard()
            b.configure(bg="white")
            c.configure(bg="white")
            d.configure(bg="white")
            a.configure(bg="#007FFF")
            e.configure(bg="white")
            f.configure(bg= "white")
            g.configure(bg="white")
            # button.configure(bg= "blue")
          
            

    #________________________________________________________________________        

        def BookB(b , a , c , d ,e , f , g ):
            print("Booking")
            for frame in self.frame4.winfo_children():
                frame.destroy()
            self.BookingForm()
            # button.configure(bg= "blue")
            a.configure(bg ="white")
            c.configure(bg= "white")
            d.configure(bg= "white")
            b.configure( bg="#008080")
            e.configure(bg="white")
            f.configure(bg="white")
            g.configure(bg="white")
            

           
# _______________________________________________________________________________________

           
            
        def BookRoomC(c , a , b ,d ,e , f , g ):
            print("bookrooms")

            for frame in self.frame4.winfo_children():
                frame.destroy()
            # button.configure(bg= "blue")
            self.bookedR()
            a.configure(bg="white")
            b.configure(bg="white")
            d.configure(bg="white")
            e.configure(bg="white")
            f.configure(bg="white")
            g,configure(bg="white")
            c.configure( bg="#008080")

          
           
#____________________________________________________________________________________________________
    
      
            
        def Departments(d , a , b , c  , e , f,g):
            print("Department")
          
            self.department() 
            a.configure(bg= "white")
            b.configure(bg= "white")
            c.configure(bg= "white")
            d.configure(bg="#008080")
            e.configure(bg= "white")
            f.configure(bg="white")
            g.configure(bg="white")
        
        def BookHallD():
            print("Booked Halls")
        def MenuE():
            print("Menu")
        def AvailableF():
            print("Availability Calendar")
        def Hotelconfiguration(e , a , b , c ,d ,f,g):
            print("Hotel Configuration")
            a.configure(bg="white")
            b.configure(bg="white")
            c.configure(bg="white")
            d.configure(bg="white")
            g.configure(bg="white")
            
            e.configure( bg="#008080")      
            f.configure(bg="white")
    

        
        def setting(f , a , b ,c  ,d , e ,g):
            print("setting")
            a.configure(bg="white")
            b.configure(bg="white")
            c.configure(bg="white")
            d.configure(bg="white")
            e.configure(bg="white")
            g.configure(bg="white")
            f.configure(bg="#008080")
            self.settingcomponent()

        def complaints(g , a ,b ,c ,d ,e , f ):
            
            a.configure(bg="white")
            b.configure(bg="white")
            c.configure(bg="white")
            d.configure(bg="white")
            e.configure(bg="white")
            f.configure(bg="white")
            g.configure(bg="#008080")
            self.Complaints()



      
# ____________________________________________________________________________________________________________

       
            
    # frame is for  navebar
        self.frame1 = Frame(self.root, width=300, height=800, bg="#E1EBEE" , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        self.frame1.pack_propagate(False)
        self.frame1.pack(side=LEFT, fill=Y)
        self.frame1.grid_propagate(False)

        

        #_____________________________________________________________________________
        frameTitle = Frame(self.frame1 , width= 300 , height=100 , bg="#008080" , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2  )
        frameTitle.pack()
        frameTitle.pack_propagate(False)
        frameTitle.grid_propagate(False)
      
        self.number = 0 
        def backgroundcolorchanger():
            
            if self.number ==0 :
                print("hello world")
                self.number += 1
                self.frame8.config(bg="black")
                self.FrameRoomnumberses.config(bg="black")
                self.two.config(bg="black")
                self.three.config(bg="black")
                self.four.config(bg="black")
                self.five.config(bg="black")
                self.six.config(bg="black")
                self.seven.config(bg="black")
                self.eight.config(bg="black")
                self.nine.config(bg="black")
                self.ten.config(bg="black")
                self.elevene.config(bg="black")
                self.twelve.config(bg="black")
                self.thirdteen.config(bg="black")
                self.fourteen.config(bg="black")
                self.fifteen.config(bg="black")
                self.sixteen.config(bg="black")
                self.seventeen.config(bg="black")
                self.eighteen.config(bg="black")
                self.nineteen.config(bg="black")
                self.twinteen.config(bg="black")
                self.one.config(bg="black")
                self.FrameRoomnumbers.config(bg="black")
                self.mainFrame.config(bg="black")

              
                
            elif self.number == 1 :
                print("hello india")
                self.one.config(bg="#E1EBEE")
               
                self.FrameRoomnumbers.config(bg="#E1EBEE")
                self.frame8.config(bg="#E1EBEE")
                
                self.FrameRoomnumberses.config(bg="#E1EBEE")



                self.two.config(bg="#E1EBEE")
                self.three.config(bg="#E1EBEE")
                self.four.config(bg="#E1EBEE")
                self.five.config(bg="#E1EBEE")
                self.six.config(bg="#E1EBEE")
                self.seven.config(bg="#E1EBEE")
                self.eight.config(bg="#E1EBEE")
                self.nine.config(bg="#E1EBEE")
                self.ten.config(bg="#E1EBEE")
                self.elevene.config(bg="#E1EBEE")
                self.twelve.config(bg="#E1EBEE")
                self.thirdteen.config(bg="#E1EBEE")
                self.fourteen.config(bg="#E1EBEE")
                self.fifteen.config(bg="#E1EBEE")
                self.sixteen.config(bg="#E1EBEE")
                self.seventeen.config(bg="#E1EBEE")
                self.eighteen.config(bg="#E1EBEE")
                self.nineteen.config(bg="#E1EBEE")
                self.twinteen.config(bg="#E1EBEE")
                self.mainFrame.config(bg="#E1EBEE")




















                self.number = 0 
            
        value  = Checkbutton(frameTitle , text="lightordarkmode" , command= lambda : backgroundcolorchanger() , bg="#008080" , bd=None)
        value.grid(column=0 , row=0)
        
         # Label(frameTitle , text= "Hotel Management Syster " , font=("bold" , 2 )  , fg= "white").pack()

        # ___________________________________________________________________________________
        self.frameN1 =  Frame(self.frame1 , width = 300 , height= 1000)
        self.frameN1.pack()
        self.frameN1.pack_propagate(False)
        self.frameN1.grid_propagate(False)
        a = Label(self.frameN1 )
        a.grid(row= 1 , column= 0 , padx= 3)
        b = Label(self.frameN1)
        b.grid(row= 2 , column= 0 , padx= 3)
        c = Label(self.frameN1 )
        c.grid(row= 3 , column= 0 , padx= 3)
        d = Label(self.frameN1)
        d.grid(row= 4 , column= 0 , padx= 3)
        e = Label(self.frameN1)
        e.grid(row=5 , column= 0 , padx= 3)
        f = Label(self.frameN1)
        f.grid(row=6 , column= 0 , padx= 3)
        g = Label(self.frameN1)
        g.grid(row=8, column= 0 , padx= 3)
        
        # _____________________________________________________________________________
        dash = Button(self.frameN1 , text="Dash board" , command= lambda :  DashA(a  , b , c, d , e ,f , g ) , fg="#008080" , bd=0 , padx= 10 , pady=20 , font=("bold" , 20))
        dash.grid(row= 1, column= 1)
        dash2 = Button(self.frameN1  , text="Booking " , command= lambda : BookB(b ,a , c , d , e , f,g), fg="#008080", bd=0 , padx= 10, pady=20 , font=("bold" , 20))
        dash2.grid(row=2 , column= 1)
        dash3 = Button(self.frameN1  , text="Guests " , command= lambda : BookRoomC(c , a ,b ,d , e ,f ,g), fg="#008080", bd=0 , padx= 10 , pady=20 , font=("bold" , 20))
        dash3.grid(row=3 , column= 1)
        dash4  = Button(self.frameN1  , text="Department" , command= lambda : Departments(d , a , b ,c , e ,f,g ), fg="#008080" , bd=0 , padx= 10, pady=20 , font=("bold" , 20))
        dash4.grid(row=4 , column=1)
        dash5 = Button(self.frameN1 , text="Hotel configuration" ,command= lambda : Hotelconfiguration(e , a , b ,c ,d  , f , g), fg="#008080" , bd=0 , padx= 10, pady=20 , font=("bold" , 20))
        dash5.grid(row=5 , column= 1)
       
        dash6 = Button(self.frameN1 , text="Setting" ,command= lambda : setting(f , a , b ,c ,d ,e, g  ), fg="#008080" , bd=0 , padx= 10, pady=20 , font=("bold" , 20))
        dash6.grid(row=6 , column= 1)
       
        dash6 = Button(self.frameN1 , text="Depository" ,command= lambda : setting(f , a , b ,c ,d ,e ,g ), fg="#008080" , bd=0 , padx= 10, pady=20 , font=("bold" , 20))
        dash6.grid(row=7 , column= 1)
        

        dash6 = Button(self.frameN1 , text="G complaints" ,command= lambda : complaints(f , a , b ,c ,d ,e ,g ) , fg="#008080", bd=0 , padx= 10, pady=10 , font=("bold" , 20))
        dash6.grid(row=8 , column= 1)
       
       
        
       
   
   #__________________________________________________________________________________

    def header(self):
 
        # frame  2 is the header  
        self.frame2 = Frame(self.root, width=1500, height=100, bg="#008080")
 
        self.frame2.pack(side=TOP, fill=X)
        self.frame2.pack_propagate(False)
        self.frameforheader  = Frame(self.frame2 , width= 150 , height=50  , bg="#008080")
        self.frameforheader.pack(side=RIGHT , padx=(0 , 60))
        Label(self.frameforheader , text="Baqar zafar farooqui" ,
             font= 100 , bg= "#008080" , fg="white").grid(column=1 , row=0)
        Button(self.frameforheader , text="Log Out " , 
               bg="red", fg="black" ,
               command=self.logout , font=("serif" , 10 ) , bd=0).grid(column=2 , row=0 , padx=(5 , 1)           )
     


   

# ______________________________________________________________________________________________________
    def Contents(self):


        self.frame3 = Frame(self.root, width=1300, height=800, bg= "#E1EBEE")
        self.frame3.pack(side=RIGHT, fill=BOTH, expand=True)
        self.frame3.pack_propagate(False)
        self.frame4 = Frame(self.frame3, width=800, height=700  , bg= "#E1EBEE")
        self.frame4.pack(fill=BOTH, expand=True)
  

  # ___________________________________________________________________________________________________ 
    def BookingForm(self):
       
        # self.frame8.destroy()
        # self.frame9.destr0oy()
       
       
        self.frame7 = Frame(self.frame4 , width=1500,
                            height=1000 , bg= "#E1EBEE")
        self.frame7.grid(column=0, row=0 )
        


        self.framef = Frame(self.frame7, width=800, 
                            height=900, bg="#E1EBEE")
        
        self.framef.grid(padx=300)

        self.framef.grid_propagate(False)  # Disable resizing to fit contents

        # Add Entry widget
        leble = Label(self.framef , text="Name"  ,font=20 , bg= "#E1EBEE",
                       fg="#008080" ).grid(row= 0 ,column=0  ,pady=15 )
        
        
        self.Entryforname = Entry(self.framef, bg="white" ,width=20  , font=30 , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        

        self.Entryforname.grid(row=0 ,column=1 ,pady=15)
        
        leble = Label(self.framef , text="NIC"  ,
                       font=20 , bg= "#E1EBEE"
                       , fg="#008080" ).grid(row=1 , column=0 ,pady=15 )
        
        self.nic = Entry(self.framef, bg="white" , width=30 , font= 30  , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        
        self.nic.grid(row=1 , column=1 ,  padx=40  ,pady=15 )
        leble = Label(self.framef , text="Address"  , 
                          font=20 , bg= "#E1EBEE", fg="#008080" ).grid(row=2 , column=0 ,pady=15 )
        
        self.address = Entry(self.framef, bg="white" ,
                              width=30  , font=30  , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        self.address.grid(row=2 , column=1 ,pady=15 )
        
        leble = Label(self.framef , text="Phone Number" , 
                      font=20, bg= "#E1EBEE", fg="#008080").grid(row=3 , column=0 ,pady=10 
                                                              )
        
        self.phonenumber = Entry(self.framef, bg="white" , 
                                 width=30  , font=30  , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        
        self.phonenumber.grid(row=3 , column=1 , padx=40  ,pady=15 )


        leble = Label(self.framef , text="Type Of Room" , font=20 ,
                      bg= "#E1EBEE", fg="#008080").grid(row=4 , column=0 ,pady=10  )
        

        self.Typeofroom = Entry(self.framef, bg="white",width=10 , font=30 , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2  )
        

        self.Typeofroom.grid(row=4 , column=1  ,pady=15)


        leble = Label(self.framef , text="Number of days" , 
                      font=20 , bg= "#E1EBEE" , fg="#008080" ).grid(row=5 , column=0  ,pady=10)
        

        self.numberofday = Entry(self.framef, bg="white",width= 10  , font=30, highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2  )
        
        self.numberofday.grid(row= 5, column=1 , padx=40 ,pady=15 )
        leble = Label(self.framef , text="Room number" , 
                      
                      font=20 , bg= "#E1EBEE", fg="#008080" ).grid(row=6 , column=0  ,pady=10 
                                                              )
        
        self.Roomnumber = Entry(self.framef, bg="white",
                                 width= 10 , font=30, highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 
                                  )
        
        self.Roomnumber.grid(row=6 , column=1  ,pady=15)

        
        Button(self.framef , text="Submit" , command=self.Check , 
                bg="#008080", fg="white" , font=20).grid(row=7 , column=1)

        self.A =  Frame(self.frame4, width=1500, height=1000 , bg= "orange")
        self.A.destroy()
            

#_______________________________________________________________________________________________________________
    

    def delete(self , get):
            mess=   messagebox.askquestion("message " , "are you sure you want to delete ")
            aditiontoDatabase = self.mydb.cursor()
            
            if mess =="yes":
                
                self.mydb.cursor().execute("delete from roombooking where name = %s" , (get,))
                
                aditiontoDatabase.execute("update roomandhall set Rooms = Rooms + 1")
                self.bookedR()

 

# 1 ________________________________________________________________________________________________________________
    def dashboard(self):
    
       
        self.frame8 = Frame(self.frame4, width=2000, height=400 , bg= "#E1EBEE" , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=4)
     #_______
        self.mainFrame = Frame(self.frame8 , width= 500 , height= 200 , bg= "#E1EBEE")
     #_______
        self.mainFrame.pack(padx=(100 , 0), pady= 100)
     #_______
        self. mainFrame.pack_propagate
     #_______
        self.frame8.pack(fill="x")
     #_______
        self.framed1 = Frame(self.mainFrame , width=200 , height= 100 , bg= "#E1EBEE" )
     #_______
        self.framed1.grid(row=0 , column= 0 , padx= (50 , 20) , pady= 30  )
     #_______
        self.framed1.grid_propagate()
        
     #_______
        
        RM =   self.mydb.cursor()
     #_______
        RM.execute("select Rooms from RoomandHall ")
     #_______

        Rooms = RM.fetchall()
     #_______
    

        self.label1 = Label(self.framed1 , image=self.imageDirecticon1 )
     #_______
        self.label1.grid(row= 0 , column= 1 ) 
     #_______
        self.frameab = Frame(self.framed1 , width= 80 , height= 85  )
     #_______
        self.frameab.grid(row=0 , column= 2 , padx=20)
     #_______
        self.frameab.grid_propagate(False)  
     #_______
        self.label2 = Label(self.frameab , text= "Rooms" , font=50 , fg="#00BFFF" , bg= "#E1EBEE" )
     #_______
        self.label2.pack()
     #_______ 
        self.label2 = Label(self.frameab , text= Rooms , font=10 , fg="#00BFFF" , bg= "#E1EBEE")
     #_______
        self.label2.pack(pady=10)
        
        

     #_______
        self.framed2 = Frame(self.mainFrame , width=200 , height= 100  , bg= "#E1EBEE")
     #_______
        self.framed2.grid(row=0 , column= 2  , padx= 20   , pady= 30 )
     #_______
        self.framed2.grid_propagate(False)
     #_______
        

        self.label2 = Label(self.framed2 , image=self.imageDirecticon2 )
     #_______
        self.label2.grid(row=0 , column= 1)
     #_______
        self.frameac = Frame(self.framed2 , width= 80 , height= 85 , bg= "#E1EBEE" )
     #_______
        self.frameac.grid(row= 0 , column=2 , padx=20 )
     #_______
        self.frameac.grid_propagate(False)
     #_______
        
        H = self.mydb.cursor()
     #_______
        H.execute("select Halls from RoomandHall")
     #_______
        halls =  H.fetchall()
     #_______
        Label(self.frameac , text="Halls" , font= 50 , fg="red" , bg= "#E1EBEE" ).pack()
     #_______
        self.label3 = Label(self.frameac , text= halls , font=10 , fg="red" , bg= "#E1EBEE")
     #_______
        self.label3.pack(pady=10)
     #_______

        self.framed3 = Frame(self.mainFrame , width=200 , height= 100 , bg= "#E1EBEE")
     #_______
        self.framed3.grid(row=0 , column= 3  , padx= 20   , pady= 30     )
     #_______
        self.framed3.grid_propagate(False)
     #_______


        label3 = Label(self.framed3 , image=self.imageDirecticon3 )
     #_______
        label3.grid(column = 0 , row= 0)
     #_______
         
        h = self.mydb.cursor()
     #_______
        h.execute("select floors from RoomandHall where floors = 20 ")
     #_______
        floors = h.fetchall()
     #_______
        self.framead= Frame(self.framed3 ,  width=80 , height=85  , bg= "#E1EBEE")
     #_______
        self.framead.grid(row= 0 , column= 2  , padx=30)
     #_______
        self.framead.grid_propagate(False)


     #_______
        Label(self.framead , text= "Floors" , font=50 , fg="green", bg= "#E1EBEE").pack()
     #_______
        self.label4 = Label(self.framead , text= floors , font= 10 , fg="green", bg= "#E1EBEE")
     #_______
        self.label4.pack(pady=10)

        self.framed4 = Frame(self.mainFrame , width=200 , height= 100 , bg= "#E1EBEE" )
     #_______
        self.framed4.grid(row=0 , column= 4  , padx= 20   , pady= 30  )
     #_______
        self.framed4.grid_propagate(False)
     #_______


        self.label4 = Label(self.framed4 , image = self.imageDirecticon4 )
     #_______
        self.label4.grid(row=0 , column= 1 )
    
     #_______

        
        
     #_______
        self.Frameae = Frame(self.framed4 , width=80 , height= 85 , bg= "#E1EBEE")
     #_______
    
        self.Frameae.grid(row=0 , column=2 , padx= 10)

        self.Frameae.grid_propagate(False)
        
        self.guestdataA =   self.mydb.cursor()
     #_______
        self.guestdataA.execute("select count(name) from roombooking")
     #_______
        self.guestdataC = self.guestdataA.fetchall()
     #_______

        
        self.label4 =  Label(self.Frameae , text= "Guest" , font=50 , fg="orange", bg= "#E1EBEE")
        self.label4.pack()
     #_______
        label4 = Label(self.Frameae, text= self.guestdataC[0], font= 50 , fg="orange" , bg= "#E1EBEE")
     #_______
        label4.pack(pady=10)
     #_______
        self.frame8.grid_propagate(False)
     
         


     #_______
        self.FrameRoomnumberses =    Frame(self.frame4,  height= 500  , width=500, bg="#E1EBEE" , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=4 )
        self.FrameRoomnumberses.pack(fill="x")
        self.FrameRoomnumberses.pack_propagate(False)
        self.FrameRoomnumberses.grid_propagate(False)
        self.FrameRoomnumbers = Frame(  self.FrameRoomnumberses , width=400 , height=400, bg="#E1EBEE" )
        self.FrameRoomnumbers.pack()
       
        self.one = Label( self.FrameRoomnumbers ,text="1)  1      To   100    (1) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.one.grid(row=0 , column=0 , padx= 50 )
        self.two=  Label( self.FrameRoomnumbers ,text="2)  101    To   200    (2) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.two.grid(row=1 , column=0 , padx= 50)
        self.three =  Label( self.FrameRoomnumbers,text="3)  201    To   300    (3) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.three.grid(row= 2, column=0 , padx= 50)
        self.four = Label( self.FrameRoomnumbers,text="4)  301    To   400    (4) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.four.grid(row=3, column=0 , padx= 50)
        self.five= Label( self.FrameRoomnumbers,text="5)  401    To   500    (5) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.five.grid(row=4 , column=0 , padx= 50)
        self.six=  Label( self.FrameRoomnumbers,text="6)  501    To   600    (6) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.six.grid(row=5 , column=0 , padx= 50)
        self.seven= Label( self.FrameRoomnumbers ,text="7)  601    To   700    (7) floor" , font="bold" , bg="#E1EBEE", fg="#008080")
        self.seven.grid(row=6 , column=0 , padx= 50)
        self.eight = Label( self.FrameRoomnumbers ,text="8)  701    To   800    (8) floor",  font="bold" , bg="#E1EBEE", fg="#008080")
        self.eight.grid(row=7 , column=0 , padx= 50)
        self.nine= Label( self.FrameRoomnumbers,text="9)  801    To   900    (9) floor",  font="bold" , bg="#E1EBEE", fg="#008080")
        self.nine.grid(row=8 , column=0 , padx= 50)
        self.ten=Label( self.FrameRoomnumbers  ,text="10) 901    To  1000    (10) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.ten.grid(row = 9 , column=0 , padx= 50)
        self.elevene=Label( self.FrameRoomnumbers,text="11) 1000   To  1100    (11) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.elevene.grid(row=9 , column=3, padx= 50)
        self.twelve=Label(self.FrameRoomnumbers ,text="12) 1101   To  1200    (12) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.twelve.grid(row=0, column=3 , padx= 50)
        self.thirdteen= Label(self.FrameRoomnumbers ,text="13) 1201   To  1300    (13) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.thirdteen.grid(row=1 , column=3 , padx= 50)
        self.fourteen=Label(self.FrameRoomnumbers ,text="14) 1301   To  1400    (14) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.fourteen.grid(row=2 , column=3 , padx= 50)
        self.fifteen = Label(self.FrameRoomnumbers ,text="15) 1401   To  1500    (15) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.fifteen.grid(row=3 , column=3 , padx= 50)
        self.sixteen=Label(self.FrameRoomnumbers ,text="16) 1501   To  1600    (16) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.sixteen.grid(row=4 , column=3 , padx= 50)
        self.eighteen=Label(self.FrameRoomnumbers ,text="17) 1601   To  1700    (17) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.eighteen.grid(row=5 , column=3 , padx= 50)
        self.nineteen=Label(self.FrameRoomnumbers ,text="18) 1701   To  1800    (18) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.nineteen.grid(row=6 , column=3 , padx= 50)
        self.seventeen= Label(self.FrameRoomnumbers,text="19) 1801   To  1900    (19) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.seventeen.grid(row=7 , column=3 , padx= 50)
        self.twinteen= Label(self.FrameRoomnumbers ,text="20) 1901   To  2000    (20) floor", font="bold" , bg="#E1EBEE", fg="#008080")
        self.twinteen.grid(row=8 , column=3 , padx= 50)
       
       
   

    def Complaints(self):
       
       for frame in  self.frame4.winfo_children() :
           frame.destroy()
       c = Frame(self.frame4 , width=1300 , height=1000 , bg="#E1EBEE",)
       c.pack()

       Label(c ,text="Guest Information" , bg="#008080" , font="bold" , fg="white").pack(pady=10 , fill="x" )
       d = Frame(c ,width=1000 , height=100 , bg="#E1EBEE")
       d.pack()
       d.grid_propagate(False)
       d.pack_propagate(False)

       Label(d , text="Guest name " , font="bold" , bg="#E1EBEE", fg="#008080").grid(column=0 , row=0 , pady=10)
       EName=  Entry(d , font="bold")
       EName.grid(column= 1, row=0 ,)
       Label(d , text="Guest Phone number ", font="bold", bg="#E1EBEE", fg="#008080").grid(column=2 , row=0 , pady=10)
       Ephonenumber =Entry(d , font="bold")
       Ephonenumber.grid(column=3 , row=0)
       Label(d , text="Guest Address" , font="bold", bg="#E1EBEE", fg="#008080").grid(column=0 , row=1 , pady=10)
       Eaddress = Entry(d , width=40 , font="bold" )
       Eaddress.grid(row=1 , column=1 )
       Label(d , text= "Guest room number", font="bold", bg="#E1EBEE" , fg="#008080").grid(column=2 , row=1 , pady=10)
       Eroomnumber = Entry(d , font="bold")
       Eroomnumber.grid(row=1 , column=3 , pady=10)
       Label(c ,text="Complaint Information" , bg="#008080" , font="bold" , fg="white").pack(pady=10 , fill="x" )
      
       E = Frame(c, bg="#E1EBEE" , pady=20 , width=1000)
       E.pack()
       Label(E , text="Complaint Date" , font="bold", bg="#E1EBEE" , fg="#008080").grid(column=0 , row=0 , pady=10 , padx=10)
       Ea = Entry(E, font="bold")
       Ea.grid(column=1, row=0, pady=10 , padx=10)
       Label(E , text="Complaint Taken BY", font="bold", bg="#E1EBEE" , fg="#008080").grid(row=0 , column=2 , padx=10)
       Eb=Entry(E, font="bold")
       Eb.grid(column=3, row=0, pady=10, padx=10)
       Label(E , text="Complaint Details", font="bold", bg="#E1EBEE" , fg="#008080").grid(column=0 , row=1 , padx=10)
       Ec = Entry(E, font="bold")
       Ec.grid(column=1, row=1, pady=10, padx=10)
       Label(E , text="First Response", font="bold", bg="#E1EBEE" , fg="#008080").grid(column=2 , row=1)
       Ed = Entry(E, font="bold")
       Ed.grid(column=3, row=1, pady=10 , padx=10)
       Label(E , text="Suspected cause", font="bold", bg="#E1EBEE" , fg="#008080").grid(column=0 , row=2, padx=10)
       Ee = Entry(E, font="bold")
       Ee.grid(column=1, row=2, pady=10, padx=10)
       
       def summitethecomplaint():
     


         print(Eroomnumber.get() , EName.get()
               , Ephonenumber.get() , Eaddress.get()
               , Ea.get() , Eb.get(),
               Ec.get() , Ed.get() , Ee.get()
               
               )
           
       Button(c , text="Submit the complaint" , command=summitethecomplaint, font="bold" , bg="#008080" , fg="white").pack()
   





#____________________________________________________________________________________________________________________
  
      

    def settingcomponent(self):
        
        
        for frame in self.frame4.winfo_children():
            frame.destroy()
        

        ab = Frame(self.frame4, width=1000 , height= 800 , bg="#E1EBEE")
        ab.pack()

        ac = Frame(ab , width= 1500,height= 800 , bg="#E1EBEE"  , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        ac.pack(pady= 200 , padx=10)
        ac.pack_propagate(False)
        
        l1 = Label(ac , text="Old password" , font=("bold"), bg="#E1EBEE"  ,fg="#008080")
        l1.grid(column=0 , row=0  , pady= 10 , padx=10)
        entry1 = Entry(ac ,show= "*",  font=("bold"), bg="#E1EBEE" , highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        entry1.grid(column=1 , row= 0 , pady= 10 , padx=10)
      #   value = entry1.get()
        l2 = Label(ac , text="New password " , font=("bold"), bg="#E1EBEE"  ,fg="#008080")
        l2.grid(column=0 , row=1 , pady= 10 , padx=10)
        entry2 = Entry(ac , font=("bold"), bg="#E1EBEE", highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        entry2.grid(row=1 , column=1 , pady= 10 , padx=10)
      #   value2 = entry2.get()
        l3 = Label(ac , text="Confirm password" , font=("bold"), bg="#E1EBEE"  ,fg="#008080")
        l3.grid(row=2 , column= 0 , pady= 10 , padx=10)
        entry3 = Entry(ac ,show= "*" ,font=("bold"), bg="#E1EBEE", highlightbackground="#008080", highlightcolor="#008080", highlightthickness=2 )
        entry3.grid(row=2 , column= 1  , pady= 10 , padx=10)
      #   value3 = entry3.get()
        


        def myfunction():
            
            p = self.mydb.cursor()
            p.execute("select password from password")
            password = p.fetchall()
         
              
            if entry2.get() == entry3.get() : 
              if entry1.get() == password[0][0]:
                
                   p.execute("update password set password  = %s"  , (entry3.get(),))
                   messagebox.showinfo("Password" , "password has changed now ")
                   
            else :
                messagebox.showinfo("password" , "confirm password does not match")
            
        Button(ac , text="Change" , bg="green", command=myfunction , font="bold").grid(row=3 , pady= 10)





          




#2_________________________________________________________________________________________________________     
    def bookedR(self):
        # self.frame7.destroy()
        # self.frame7.destroy()

        self.frame9 = Frame(self.frame4, width=1500, height=1000 , bg="#E1EBEE" )
        self.frame9.grid(column=0, row=0)
       
        self.frame11 = Frame(self.frame9 , width= 1500, height= 50  , bg="#E1EBEE" )
        self.frame11.grid(column= 0, row=1)
        self.frame11.grid_propagate(False)

       
          
  
          
         
          
          
        
        name1 = Label(self.frame11 , text= "Name", font= 15 , fg="#008080"  , bg="#E1EBEE" )
        name1.grid(row=0 , column = 0  , padx=(50 , 0))
        
        name2 = Label(self.frame11 , text= "Address", font= 15 , fg="#008080"   , bg="#E1EBEE" )
        name2.grid(row=0 , column = 1 , padx=(45 , 0))
        
        name3 = Label(self.frame11 , text= "Phone no", font= 15 , fg="#008080"  , bg="#E1EBEE")
        name3.grid(row=0 , column = 2 , padx=(30 , 0) )
        
        name4 = Label(self.frame11 , text= "T of room ", font= 15 , fg="#008080"  , bg="#E1EBEE")
        name4.grid(row=0 , column = 3  )
        
        name5 = Label(self.frame11 , text= "CNIC", font= 15 , fg="#008080" , bg="#E1EBEE")
        name5.grid(row=0 , column = 4  )
        
        name6 = Label(self.frame11 , text= "N of rooms ", font= 15 , fg="#008080", bg="#E1EBEE")
        name6.grid(row=0 , column = 5 , padx = (10 , 10))
        name6 = Label(self.frame11 , text= "Amount", font= 15 , fg="#008080" , bg="#E1EBEE")
        name6.grid(row=0 , column = 6 )
        name6 = Label(self.frame11 , text= "Room no ", font= 15 , fg="#008080" , bg="#E1EBEE")
        name6.grid(row=0 , column = 7 )
        # name7 = Label(self.frame11 , text= button[6], font= 15 , fg="#1F75FE" , bg="white")
        # name7.grid(row=0 , column = 6    , padx = (25 ,0))
        

        
        self.frame9.grid_propagate(False)










        framecanvas = Canvas(self.frame9 , width= 1500 , height= 450 , bg="#E1EBEE")
        framecanvas.grid(column= 0 , row=2)



        self.frame12 = Frame(framecanvas , width= 1500, height= 400 , bg="#E1EBEE")
        self.frame12.grid(column= 0, row=2)
        self.frame12.grid_propagate(False)
   
        # here We are retriving data 
        mycursor =  self.mydb.cursor()
        mycursor.execute("select * from roombooking")
        self.data = mycursor.fetchall()
        



        # This is for  data representation

        for x in range(len(self.data)):
            
            for y in range(len(self.data[x])):
               lable =   Label(self.frame12 , text= self.data[x][y] , font= 20 , bg="#E1EBEE", fg="black" )
               lable.grid(row = x , column= y   , padx= 4 )
              
               button=Button(self.frame12,  bg="red" , text= "Delete"  , font=5 , command= partial(self.delete , self.data[x][0]) )
               button.grid(row= x , column = len(self.data[x] ) , pady=3 , padx=40)
             
        self.mydb.commit()
         

    
# ____________________________________________________________________________________________________________________
    # def CashPayment1(self):
       
    #     self.Cashpayment()

       
       
            
    def Cashpayment(self):
       
        
        # self.Paymentsystem()
        self.A =  Frame(self.frame4, width=1500, height=1000 , bg= "orange")
        self.A.grid(column=0, row=0 )
        self.A.grid_propagate(False)

        B = Frame(self.A , width= 1300 , height= 300 , bg="#E1EBEE" )
        B.grid(column= 0 , row = 0)
        B.grid_propagate(False)

        C = Frame(B , width=  1000 , height= 300 , bg= "#E1EBEE")
        C.grid_propagate(False)
        C.grid(row= 0 , column= 4 , padx=(150  , 0))
        LA =  Label(C , text= "Name" , font= 30 , fg= "#008080"  , bg="#E1EBEE")
        LA.grid(row=0 , column= 0  , padx= 10  , pady= 15)
        LB = Label(C , text= self.temporrayStoringArray[0] , bg="#E1EBEE")
        LB.grid(row=0 , column= 1 , padx= 10  , pady= 15)
        LC =  Label(C  , text= "NIC" , font= 30  ,fg= "#008080" , bg="#E1EBEE")
        LC.grid(row= 1 , column= 0 , padx= 10  , pady= 10)
        LD = Label(C , text=  self.temporrayStoringArray[1]  , bg="#E1EBEE")
        LD.grid(row = 1 , column= 1, padx= 10  , pady= 10)
        LE =  Label(C  , text= "Address" , font= 30 ,fg= "#008080" , bg="#E1EBEE")
        LE.grid(row = 2 , column= 0 , padx= 10  , pady= 10)
        LF = Label(C , text= self.temporrayStoringArray[2]  , bg="#E1EBEE")
        LF.grid(row=2, column=1, padx= 10  , pady= 10)
       
        LE =  Label(C  , text= "Phone number" , font= 30 ,fg= "#008080" , bg="#E1EBEE")
        LE.grid(row = 0 , column= 2 , padx= 10  , pady= 10)
        LF = Label(C , text= self.temporrayStoringArray[4], bg="#E1EBEE")
        LF.grid(row=0, column=3 , padx= 10  , pady= 10)
       
        LE =  Label(C  , text= "Room number " , font= 40 ,fg= "#008080" , bg="#E1EBEE")
        LE.grid(row = 1 , column= 2 , padx= 10  , pady= 10)
        LF = Label(C , text= self.temporrayStoringArray[6] , bg="#E1EBEE")
        LF.grid(row=1, column=3 , padx= 10  , pady= 10)
        LE =  Label(C  , text= "Date  " , font= 40 ,fg= "#008080" , bg="#E1EBEE")
        LE.grid(row = 2, column= 2 , padx= 10  , pady= 10)
        LF = Label(C , text= "todays day automactically will assign" , bg="#E1EBEE")
        LF.grid(row =2, column=3 , padx= 10  , pady= 10)
        LE =  Label(C  , text= "Type of Room  " , font= 40 ,fg= "#008080" , bg="#E1EBEE")
        LE.grid(row = 3, column= 0 , padx= 10  , pady= 10)
        LF = Label(C , text= self.temporrayStoringArray[3] ,  bg="#E1EBEE")
        LF.grid(row = 3, column=1 , padx= 10  , pady= 10)
        LE =  Label(C  , text= "Check out date  " , font= 40 ,fg= "#008080" , bg="#E1EBEE")
        LE.grid(row = 3, column= 2 , padx= 10  , pady= 10)
        LF = Label(C , text= "8.12 . 2024" , font= 10 , bg="#E1EBEE")
        LF.grid(row =3, column=3 , padx= 10  , pady= 10)
       
       
        
         
        
        LF = Label(C , text= "Receptionist name " , font= 10 ,fg= "#008080" , bg="#E1EBEE" )
        LF.grid(row =4, column=0 , padx= 10  , pady= 10)
        LF = Label(C , text= "baqarzafarfarooqui" , bg="#E1EBEE")  
        LF.grid(row =4, column=1 , padx= 10  , pady= 10)
        LF = Label(C , text= "Number of days " , font= 10 ,fg= "#008080" , bg="#E1EBEE")
        LF.grid(row =4, column=2 , padx= 10  , pady= 10)
        LF = Label(C , text= self.temporrayStoringArray[5] , )  
        LF.grid(row =4, column=3 , padx= 10  , pady= 10)


        D = Frame(self.A , width=1300 , height=500 , bg="#E1EBEE")
        D.grid(row=2 , column=0)
        D.grid_propagate(False)
        self.E = Frame(D , width=1500  , height= 500 , bg="#E1EBEE")
        self. E.grid(row=0 , column= 4  , padx=(250, 0) , pady= 50)
        self.E.grid_propagate(False)



        T =  self.mydb.cursor()
        self.typesofrooms = self.temporrayStoringArray[3]
        T.execute(f"select  {self.typesofrooms} from  typesofrooms")
        
        self.Total = T.fetchall()[0][0] * int(self.temporrayStoringArray[5])
        Le = Label(self.E , bg="#E1EBEE" , text=" Total " ,fg= "#008080" , font= ("serif" , 10))
        Le.grid(row=0 , column= 0 , padx=(25 , 0) , pady= 5)
        lf = Label( self.E , bg= "#E1EBEE" , text= self.Total,fg= "#007FFF", font= ("serif" , 10) )
        lf.grid(row= 0 , column= 1 , padx=(25 , 0) , pady= 5)


        
        lf = Label( self.E , bg= "#E1EBEE" , text="Receive amount",fg= "#008080" , font= ("serif" , 10) )
        lf.grid(row= 0 , column= 2 , padx=(25 , 0) , pady= 5)
        self.lf = Entry( self.E ,  fg="black"  , width= 10, font= 10  )
        self.lf.grid(row= 0 , column= 3  , padx=(25 , 0) , pady= 5)
         
        self.returnamoutarray = [0]
        
        self.lf.bind("<Return>" ,self.returnamount)
        lg= Label( self.E , bg= "#E1EBEE" , text="To Return ",fg= "#008080" )
        lg.grid(row= 2 , column= 2 , padx=(25) , pady= 5)
        
        
       
#__________________________________________________________________________________________________________        
       
    def returnamount(self , event):
        self.cashbutton1 = Button(self.E , command= self.sumittomysql,text="Reserve The  Room " ,
               bg="yellow" , width=20 , font=("serif" , 20 )).grid( row=3 , column=2 , pady=30)
        csh = self.mydb.cursor()
        g = csh.execute("insert into hotelcash (Cash ) values (%s)" , ([self.Total]))
         
        
        self.usablenumber = 1
        if int(self.lf.get()) == self.Total:
           self.returnamoutarray.clear()
           self.returnamoutarray.append(0)
           print("The function is running")
           self.X()
        elif int(self.lf.get()) != self.Total:

             self.returnamoutarray.clear()
             self.returnamoutarray.append( int(self.lf.get()) - self.Total)
             print("The function is running2")
             self.X()
                
    def X(self):
        lh = Label( self.E , bg= "white" , text= self.returnamoutarray[0], fg="black"  )
        lh.grid(row= 2 , column= 3)

    
    

    def department(self):

        for frame in self.frame4.winfo_children():
            frame.destroy()
        frameD =  Frame(self.frame4 , width= 1500 , height= 1500 , bg="white")
        frameD.grid(row=0 , column= 0  )
        frameD.grid_propagate(False)

        frameE = Frame(frameD , width= 500 , height=300 , bg="#7C93C3")
        frameE.grid(row=0 , column= 0 , padx= 100 , pady= 20)
        frameE.grid_propagate(False)
        buttonA = Button(frameE ,fg="white" ,  text="It department" , width=32 , height=10 , font=("bold" , 20) , bg="#55679C" )
        buttonA.grid(row=0 , column=0)
       
        frameF = Frame(frameD , width= 500 , height=300 , bg="#1E2A5E")
        frameF.grid(row=0 , column= 1 , pady= 20)
        frameF.grid_propagate(False)
        buttonB = Button(frameF ,fg="white", text="Cleaning Staff"  , width=32 , height=10 , font=("bold" , 20) , bg="#1E2A5E")
        buttonB.grid(row=0 , column=0)
    
        frameG = Frame(frameD , width= 500 , height=300 , bg="#7077A1")
        frameG.grid(row=2 , column= 0 , padx= 100)
        frameG.grid_propagate(False)
        buttonC = Button(frameG ,fg="white" , text="Hotel management " , width=32 , height=10 , font=("bold" , 20)  , bg="#7077A1")
        buttonC.grid(row=0 , column= 0)
       
        frameH = Frame(frameD , width= 500 , height=300 , bg="#D6E0F0")
        frameH.grid(row=2 , column= 1)
        frameH.grid_propagate(False)
        buttonD = Button(frameH ,fg="white", text="House Keeping"  , width=32 , height=10 , font=("bold" , 20)  , bg="#797A7E")
        buttonD.grid(row =0 , column=0)
        


       




Gui().root.mainloop()
        






        



        
    
        
       











   
    




        




