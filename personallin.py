import customtkinter as k
import tkinter as tk
import mysql.connector as x
import enchant as e
from PIL import Image, ImageTk
 
obj=x.connect(host="localhost",user="root",passwd="2407",database="dist")
cur=obj.cursor()
 
#-----------------------------------Searching word in sql
def srword():
    displayBox.delete("0.0", "200.0")
    
    cur.execute("Select word from form")
    y=cur.fetchall()
    w=we.get()
    k=str((w,) in y)
    
    cur.execute("Select * from form")
    y=cur.fetchall()
 
    if(k=="True"):
        for i in y:
            if(w == i[0]):
                displayBox.insert("0.0","Antnonyms ="+str(i[4])+"\n")
                displayBox.insert("0.0","Synonyms ="+str(i[3])+"\n")
                displayBox.insert("0.0","Fav ="+str(i[2])+"\n")
                displayBox.insert("0.0","Meaning="+str(i[1])+"\n")
                displayBox.insert("0.0","Word ="+str(i[0])+"\n")
        
    else:
        displayBox.insert("0.0","No Such Word Exist")
 
    we.delete(0, tk.END)
 
#-----------------------------------Entering Data
 
def fill():
    global n
 
    displayBox.delete("0.0", "200.0")
    
    cur.execute("Select Word from form")
    y=cur.fetchall()
    w=we.get()
    m=wm.get()
    k=str((w,) in y)
 
    a=wc(w)
    
    if(k=="True"):
        displayBox.insert("0.0","Word Already Exists")
        
    else:
         
        if (a==False):
            displayBox.insert("0.0","Incorrect Spelling")
        else:
            displayBox.insert("0.0","Word Entered Sucessfully")
            x="insert into form values(%s,%s,%s,%s,%s)"
            obj.commit()
            cur.execute(x,(w,m,"Not Favorite","Not specified","Not specified"))
 
    we.delete(0, tk.END)
    wm.delete(0, tk.END)
 
#-----------------------------------------------------------check word
 
def wc(word):
 
    ## str(dict.suggest(word)## Can be used to suggest the correct word
                                           
    dict = e.Dict("en_US")  # You can specify the language you want to use, e.g., "en_US" for English
 
    if dict.check(word) == False:  
        return False
    else:
        return True
 
#--------------------------------------------------------
def ChangeAppD():
    k.set_appearance_mode("Dark")
    dialog.destroy()
 
def ChangeAppL():
    k.set_appearance_mode("Light")
    dialog.destroy()
    
#-------------------------------------------------------------------Settings
 
def sett():
    global dialog
    
    dialog = k.CTkToplevel()
    dialog.geometry("508x227")
 
    dialog.attributes('-topmost','true')
 
    ct=k.CTkLabel(dialog,text="Select Theme",font=("Roboto Slab Bold",25))
    ct.grid(row=0,column=0,sticky="NW",padx=50,pady=10,)
 
    bt=k.CTkRadioButton(dialog, text="Dark Theme",font=("Roboto Slab Bold",20),command=ChangeAppD)
    bt.grid(row=1,column=0,sticky="NW",pady=15,padx=50)
 
    bt2=k.CTkRadioButton(dialog, text="Light Theme",font=("Roboto Slab Bold",20),command=ChangeAppL)
    bt2.grid(row=2,column=0,sticky="NW",pady=15,padx=50)
 
    dialog.grid_columnconfigure((0,1),weight=1)
    dialog.grid_rowconfigure((0,1,2),weight=1)
   
#-----------------------------------------------------------------GUI
 
k.set_appearance_mode("Dark")
k.set_default_color_theme("blue")
root =k.CTk()
root.geometry("2800x2800")
root.configure(fg_color="#404258",)
root.title("Dictionary")
 
 
frame1=k.CTkFrame(root,height=500,fg_color="#50577A")
frame1.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0,weight=1)
 
 
#---------------------------------------------------------
 
img = Image.open(r"C:\Users\easha\Downloads\settings.png")
width, height = 50,50
resimg = img.resize((width, height), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resimg)
ic = k.CTkButton(root, image=photo,fg_color="transparent",text='',command=sett)
ic.grid(row=0,column=0,sticky="NE",padx=(100,0))
 
#-------------------------------------------------------------------Destroying frames
def des():
    frame2.destroy()
    frame3.destroy()
    home()
 
def des2():
    frame4.destroy()
    home()
 
def des3():
    frame5.destroy()
    home()
    
def des4():
    frame6.destroy()
    home()
    
def des5():
    frame7.destroy()
    home()
 
def Dld():
    dialog.destroy()
 
def Dldd():
    cur.execute("Delete from form")
    dialog.destroy()
#------------------------------------------------------Clear Dictionary
 
def cd():
 
    global dialog
    
    dialog = k.CTkToplevel()
    dialog.geometry("508x227")
 
    dialog.attributes('-topmost', 'true')
 
    ct=k.CTkLabel(dialog,text="Are you Sure you Want to Clear Dictionary",font=("Roboto Slab Bold",20))
    ct.grid(row=1,column=0,sticky="NEW",padx=50,pady=50,columnspan=2)
 
    bt=k.CTkButton(dialog, text="Yes",font=("Roboto Slab Bold",15),command=Dldd,)
    bt.grid(row=2,column=0,sticky="N",pady=15)
 
    bt2=k.CTkButton(dialog, text="No",font=("Roboto Slab Bold",15),command=Dld)
    bt2.grid(row=2,column=1,sticky="N",pady=15)
 
    dialog.grid_columnconfigure((0,1),weight=1)
    dialog.grid_rowconfigure((0,1),weight=1)
    
#--------------------------------------------Search Word
def searchword():
    global frame7,displayBox,we
    frame7=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame7.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0,weight=1)
 
    #---------------------------------------------------------------Inner content
    frame7.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    frame7.grid_columnconfigure(0,weight=2)
 
 
    img3 = Image.open(r"C:\Users\easha\Downloads\data (1).png")
    width3, height3 = 500,500
    resimg3 = img3.resize((width3, height3), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(resimg3)
    ic = k.CTkLabel(frame7, image=photo3,fg_color="transparent",text='',)
    ic.grid(row=0,column=1,sticky="NSE",pady=100,padx=100,rowspan=5)
 
    word= k.CTkLabel(frame7, text="Please Enter the word to search:",font=("Roboto Slab Bold",32))
    word.grid(row=0, column=0, sticky="NW",padx=50,pady=(50,0))
 
    we=k.CTkEntry(frame7,width=290,fg_color="#404258",height=35,)
    we.grid(row=1,column=0,padx=50,pady=40,sticky="SW",columnspan=2,)
 
    btn=k.CTkButton(frame7,text="Search",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=srword,hover_color="#50577A")
    btn.grid(row=1, column=0, sticky="SE",pady=40,padx=(5,970),columnspan=3,)
 
    displayBox = k.CTkTextbox(frame7,font=("Roboto Slab Bold",30,),height=300,width=700)
    displayBox.grid(row=3, column=0,padx=50, pady=20, sticky="NSW",columnspan=2,rowspan=2)
 
    ex =k.CTkButton(frame7,text="Home",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=des5,hover_color="#50577A")
    ex.grid(row=5, column=1, sticky="SE",pady=(20,0),padx=25,columnspan=3,)
 
        
   
#-----------------------------------------Deleting word
 
def deleteword():
    
    w_d=wd.get()
    displayBox.delete("0.0", "200.0")
    
    cur.execute("Select Word from form")
    y=cur.fetchall()
    k=str((w_d,) in y)
    
    if(k=="False"):
        displayBox.insert("0.0","Word Does not exist")
    else:
        displayBox.insert("0.0","Word Deleted Sucessfully")
        x="delete from form where Word= %s"
        obj.commit()
        cur.execute(x,(w_d,))
 
    wd.delete(0, tk.END)
 
#--------------------------Modifing Word
 
def ns():
    displayBox.delete("0.0", "200.0")
    button_1.deselect()
    
    dialog = k.CTkInputDialog(text="Enter Synonyms:", title="Synonyms")
    
    nws=dialog.get_input()
    w_m=wm.get()
 
    if wc(nws)==False:
        wm.configure(state="normal")
        displayBox.insert("0.0","Incorrect Spelling")
        
    else:        
        c=("Update form set Synonyms=%s where word=%s")
        cur.execute(c,(nws,w_m))
        obj.commit()    
        wm.configure(state="normal")
        displayBox.insert("0.0","Synonyms Added Sucessfully")
 
#---------------------
        
def na():
    displayBox.delete("0.0", "200.0")
    button_1.deselect()
    
    dialog = k.CTkInputDialog(text="Enter Antnonyms:", title="Antnonyms")
    
    nws=dialog.get_input()
    w_m=wm.get()
 
    if wc(nws)==False:
        wm.configure(state="normal")
        displayBox.insert("0.0","Incorrect Spelling")
        
    else:        
        c=("Update form set Antnonyms=%s where word=%s")
        cur.execute(c,(nws,w_m))
        obj.commit()    
        wm.configure(state="normal")
        displayBox.insert("0.0","Antnonyms Added Sucessfully")
 
 
def nm():
    displayBox.delete("0.0", "200.0")
    button_2.deselect()
    
    dialog = k.CTkInputDialog(text="Enter New Spelling:", title="New Meaning")
    
    nws=dialog.get_input()
    w_m=wm.get()
    c=("Update form set meaning=%s where word=%s")
    cur.execute(c,(nws,w_m))
    obj.commit()
    
    wm.configure(state="normal")
    displayBox.insert("0.0","Meaning Changed Sucessfully")
 
def fav():
    displayBox.delete("0.0", "200.0")
    button_3.deselect()
    
    c=("Update form set fav=%s where word=%s")
    w_m=wm.get()
    cur.execute(c,("Favorite",w_m,))
    obj.commit()
    
    wm.configure(state="normal")
    
    displayBox.insert("0.0","Marked as Favorite Sucessfully")
 
def rfav():
    displayBox.delete("0.0", "200.0")
    button_3.deselect()
    
    c=("Update form set fav=%s where word=%s")
    w_m=wm.get()
    cur.execute(c,("Not Favorite",w_m,))
    obj.commit()
    
    wm.configure(state="normal")
    
    displayBox.insert("0.0","Removed from Favorite \nSucessfully")
 
#---------------------------------------------------------Credits
 
def crd():
 
    global frame6
 
    frame6=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame6.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0,weight=1)
 
    #---------------------------------------------------------------Inner content
    frame6.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    frame6.grid_columnconfigure(0,weight=2)
 
    N1 = k.CTkLabel(frame6, text="CREDITS",font=("Roboto Slab Bold",95),)
    N1.grid(row=1, column=0, sticky="NSEW",pady=30,padx=150,columnspan=2)
 
    N3 = k.CTkLabel(frame6, text="EASHAN HASIJA ",font=("Roboto Slab Bold",35),)
    N3.grid(row=2, column=0, sticky="NSEW",pady=20,padx=100,columnspan=2)
    
    N4= k.CTkLabel(frame6, text="ARPIT SHARMA",font=("Roboto Slab Bold",35),)
    N4.grid(row=3, column=0, sticky="NSEW",pady=20,padx=100,columnspan=2)
    
    N5= k.CTkLabel(frame6, text="DIVYANSHI RATH",font=("Roboto Slab Bold",35),)
    N5.grid(row=4, column=0, sticky="NSEW",pady=20,padx=100,columnspan=2)
 
    ex =k.CTkButton(frame6,text="Home",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=des4,hover_color="#50577A")
    ex.grid(row=5, column=1, sticky="SE",pady=(20,0),padx=25,columnspan=3,)
 
 
#----------------------------------------------------------Making frame for modify
 
def modifyword():
 
    global button_1,button_2,button_3,button_4
    w_m=wm.get()
    
    cur.execute("Select Word from form")
    y=cur.fetchall()
    a=str((w_m,) in y)
    
    if(a=="False"):
        displayBox.delete("0.0", "200.0")
        displayBox.insert("0.0", "Word Does not Exist")
    else:
        displayBox.delete("0.0", "200.0")
        wm.configure(state="disabled")
        opt=k.CTkLabel(frame5, text="Please Choose from the Following Options:",font=("Roboto Slab Bold",32))
        opt.grid(row=0, column=1, sticky="NSW",padx=50,pady=(50,0))
 
 
        button_1 = k.CTkRadioButton(frame5, text="Add Synonym",  value=1,font=("Roboto Slab Bold",32),command=ns)
        button_2 = k.CTkRadioButton(frame5, text="Add Antnonyms",  value=1,font=("Roboto Slab Bold",32),command=na)
        button_3 = k.CTkRadioButton(frame5, text="Modify Meaning",  value=2,font=("Roboto Slab Bold",32),command=nm,)
       
        c="Select fav from form where word=%s"
        cur.execute(c,(w_m,))
        fv=cur.fetchall()
        if ("Favorite",) in fv:
            
            button_4 = k.CTkRadioButton(frame5, text="Remove from Favorite", value=3,font=("Roboto Slab Bold",32),command=rfav)
 
        else:
 
            button_4 = k.CTkRadioButton(frame5, text="Mark as Favorite", value=3,font=("Roboto Slab Bold",32),command=fav)
 
#----------------------------------------------------------------------------
            
        button_1.grid(row=1,column=1,padx=50,pady=50,columnspan=3,sticky="NW")
        button_2.grid(row=2,column=1,padx=50,pady=50,columnspan=3,sticky="NW")
        button_3.grid(row=3,column=1,padx=50,pady=50,columnspan=3,sticky="NW")
        button_4.grid(row=4,column=1,padx=50,pady=50,columnspan=3,sticky="NW")
 
#-----------------------------------------------------------Making frame for data entry
 
def e_w():
 
    global we,wm,displayBox,frame3,frame2
    
    frame1.destroy()
    
    frame2=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame2.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
    
    frame3=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame3.grid(row=1, column=0, padx=50, pady=(0,25),sticky="NSEW",)
 
    #--------------------------------------------------------Inner content
 
    frame2.grid_rowconfigure((0,1,2,3,4),weight=1)
    frame2.grid_columnconfigure(0,weight=2)
 
    frame3.grid_rowconfigure(0,weight=1)
    frame3.grid_columnconfigure(0,weight=1)
    
    word= k.CTkLabel(frame2, text="Please Enter the word:",font=("Roboto Slab Bold",32))
    word.grid(row=0, column=0, sticky="NW",padx=50,pady=(50,0))
 
    we=k.CTkEntry(frame2,width=290,fg_color="#404258",height=35,)
    we.grid(row=1,column=0,padx=50,pady=40,sticky="SW",columnspan=2,)
 
    meaning= k.CTkLabel(frame2, text="Please Enter the word's Meaning:",font=("Roboto Slab Bold",32))
    meaning.grid(row=2, column=0, sticky="NW",padx=50,pady=(30,0))
 
    wm=k.CTkEntry(frame2,width=290,fg_color="#404258",height=35)
    wm.grid(row=3,column=0,padx=50,sticky="SW",columnspan=2,pady=40)
 
    displayBox = k.CTkTextbox(frame3,width=500,height=100,font=("Roboto Slab Bold",30,))
    displayBox.grid(row=0, column=0,padx=20, pady=20, sticky="nsew",columnspan=2,)
 
    ex =k.CTkButton(frame2,text="Home",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=des,hover_color="#50577A")
    ex.grid(row=3, column=1, sticky="SE",pady=(20,0),padx=25,columnspan=3,)
 
    sb=k.CTkButton(frame2,text="Submit",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=fill,hover_color="#50577A")
    sb.grid(row=4, column=0, sticky="NSEW",padx=25,columnspan=4,)
 
#---------------------------------------------------------------Making frame for deleting
 
def dlw():
    global frame4,wd,displayBox
    
    frame1.destroy()
    
    frame4=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame4.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
    
    #----------------------------------------------------------Inner content
 
    frame4.grid_rowconfigure((0,1,2,3,4),weight=1)
    frame4.grid_columnconfigure(0,weight=2)
    
    wordd= k.CTkLabel(frame4, text="Please Enter the Word to Delete:",font=("Roboto Slab Bold",32))
    wordd.grid(row=0, column=0, sticky="NSW",padx=50,pady=(50,0))
 
    wd=k.CTkEntry(frame4,width=290,fg_color="#404258",height=35)
    wd.grid(row=1,column=0,padx=50,pady=40,sticky="NW",columnspan=2,)
 
    ex =k.CTkButton(frame4,text="Home",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=des2,hover_color="#50577A")
    ex.grid(row=4, column=1, sticky="NSE",pady=(20,0),padx=25,columnspan=3,)
 
    sb=k.CTkButton(frame4,text="Delete Word",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=deleteword,hover_color="#50577A")
    sb.grid(row=4, column=0, sticky="NSW",padx=25,columnspan=4,) 
 
    displayBox = k.CTkTextbox(frame4,width=500,height=200,font=("Roboto Slab Bold",30,))
    displayBox.grid(row=0, column=1,padx=20, pady=20, sticky="NWE",rowspan=2,columnspan=3)
 
#-------------------------------------------------------------------Making frame for modifing
 
def mdw():
    global frame5,wm,displayBox
    
    frame1.destroy()
    
    frame5=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame5.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
    
    #----------------------------------------------------------Inner content
 
    frame5.grid_rowconfigure(0,weight=2)
    frame5.grid_rowconfigure((1,2,3,4),weight=1)
    frame5.grid_columnconfigure(0,weight=2)
    frame5.grid_columnconfigure(1,weight=1)
    
    wordm= k.CTkLabel(frame5, text="Please Enter the Word to Modify:",font=("Roboto Slab Bold",32))
    wordm.grid(row=0, column=0, sticky="NSW",padx=50,pady=(50,0))
 
    wm=k.CTkEntry(frame5,width=290,fg_color="#404258",height=35)
    wm.grid(row=1,column=0,padx=50,pady=50,sticky="NW",columnspan=2,)
 
    ex =k.CTkButton(frame5,text="Home",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=des3,hover_color="#50577A")
    ex.grid(row=4, column=1, sticky="NSE",pady=(20,0),padx=25,columnspan=3,)
 
    sb=k.CTkButton(frame5,text="Modify Word",font=("Roboto Slab Bold",30,"underline"),fg_color="transparent",command=modifyword,hover_color="#50577A")
    sb.grid(row=4, column=0, sticky="NSW",padx=25,columnspan=4,)
 
    displayBox = k.CTkTextbox(frame5,width=500,height=200,font=("Roboto Slab Bold",30,))
    displayBox.grid(row=2, column=0,padx=25, pady=20, sticky="NW",rowspan=2,)
 
#-------------------------------------------------------------------Frame for Homepage
 
def home():
 
    frame1=k.CTkFrame(root,height=500,fg_color="#50577A")
    frame1.grid(row=0, column=0, padx=50, pady=50,sticky="NSEW",)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0,weight=1)
 
    #---------------------------------------------------------------Inner content
    frame1.grid_rowconfigure((0,1,2,3,4),weight=1)
    frame1.grid_columnconfigure(0,weight=2)
    frame1.grid_columnconfigure(1,weight=1)
 
    img2 = Image.open(r"C:\Users\easha\Downloads\dictionary.png")
    width2, height2 = 600,600
    resimg2 = img2.resize((width2, height2), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(resimg2)
    ic2 = k.CTkButton(frame1, image=photo2,fg_color="transparent",text='',hover_color="#50577A",command=searchword)
    ic2.grid(row=0,column=1,sticky="NSE",padx=(100,75),rowspan=5,pady=10)
 
    name_label = k.CTkButton(frame1, text="Welcome",font=("Roboto Slab Bold",35),fg_color="transparent",hover_color="#50577A",command=crd)
    name_label.grid(row=0, column=1, sticky="NE",padx=20,pady=(15,0),columnspan=3,)
 
    title = k.CTkLabel(frame1, text="Dictionary",font=("Roboto Slab Bold",80),)
    title.grid(row=0, column=0, sticky="NW",pady=(20,10),padx=40,columnspan=3)
 
    opt = k.CTkLabel(frame1, text="Please Choose from the following:",font=("Roboto Slab Bold",30,),)
    opt.grid(row=1, column=0, sticky="NW",pady=(20,0),padx=35,columnspan=1)
 
    btn1 =k.CTkButton(frame1,text="1. Enter a Word",font=("Roboto Slab Bold",35,),fg_color="transparent",command=e_w,hover_color="#50577A")
    btn1.grid(row=2, column=0, sticky="NW",pady=(20,0),padx=35,columnspan=1,)
 
    btn2 =k.CTkButton(frame1,text="2. Modify a Word",font=("Roboto Slab Bold",35,),fg_color="transparent",command=mdw,hover_color="#50577A")
    btn2.grid(row=3, column=0, sticky="NW",pady=(20,0),padx=35,columnspan=1)
 
    btn3 =k.CTkButton(frame1,text="3. Delete a Word",font=("Roboto Slab Bold",35,),fg_color="transparent",command=dlw,hover_color="#50577A")
    btn3.grid(row=4, column=0, sticky="NW",pady=(20,0),padx=35,columnspan=1)
 
    btn4 =k.CTkButton(frame1,text="Clear Dictionary",font=("Roboto Slab Bold",30,),fg_color="transparent",command=cd,hover_color="#50577A")
    btn4.grid(row=4, column=1, sticky="SE",pady=20,padx=25,columnspan=3)
 
home()    
root.mainloop()

