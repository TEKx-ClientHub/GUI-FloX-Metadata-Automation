#This progragm creates a GUI which enables to user to input metadata information collected from FLoX tower
#The user needs to have any python development environment to run the program
#--------------------------------------------------------------------------------------------------------------


#importing necessary libraries

import tkinter as tk
import pandas as pd

#Define function of the program
def submit_metadata_fields():
    path = ''        #path for the spreadsheet (varies for ther user) 
    df1 = pd.read_csv(path)                              #create DataFrame for fields 
    
    #Define series  
    SeriesA =df1['Date(yyyy/mm/dd)']
    SeriesB =df1['Inspector']
    SeriesC =df1['Tower_conditions']
    SeriesD =df1['Calibrations']
    SeriesE =df1['Other_comments']
    
    #corresponding new values to old series
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    C = pd.Series(entry3.get())
    D = pd.Series(entry4.get())
    E = pd.Series(entry5.get())
    
    
    #pin the above new values to old series
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesC.append(C)
    SeriesD = SeriesD.append(D)
    SeriesE = SeriesE.append(E)
    
    #pass these series to a DataFrame 
    df2 = pd.DataFrame({"Date(yyyy/mm/dd)":SeriesA, "Inspector":SeriesB, "Tower_conditions":SeriesC, "Calibrations":SeriesD, "Other_comments":SeriesE})
    df2.to_csv(path, index=False)
    
    #remove items from the GUI whenever after submit 
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    


master = tk.Tk()                        #create a tkinker widget and instance
master.geometry("400x200")              #set widget size
master.configure(bg='green')            #set window color
master.title("FLoX GUI")                #Add Title

#assign labels to tkinker widget  and defining location where the label  
Label(master, text="Date(yyyy/mm/dd)").grid(row=0)
Label(master, text="Inspector").grid(row=1)
Label(master, text="Tower_conditions").grid(row=2)
Label(master, text="Calibrations").grid(row=3)
Label(master, text="Other_comments").grid(row=4)

#Define to user entries to tkinter widget  
entry1 = Entry(master)
entry2 = Entry(master)
entry3 = Entry(master)
entry4 = Entry(master)
entry5 = Entry(master)

#position the above entries on the form  
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)


#create buttons that will have actions on form
Button(master, text='Quit', command=master.quit).grid(row=5,column=0, pady=4)
Button(master, text='Submit', command=submit_metadata_fields).grid(row=5,column=1, pady=4)

#Excute GUI
mainloop()

#END
