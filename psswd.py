from tkinter import*
import string
import random
import pyperclip

def generator():
    small_alpha=string.ascii_lowercase
    capital_alpha=string.ascii_uppercase
    numbers=string.digits
    special_character=string.punctuation
    all=small_alpha+capital_alpha+numbers+special_character
    psswd_len=int(len_box.get())
    if choice.get()==1:
        psswdField.insert(0,random.sample(small_alpha,psswd_len))
    elif choice.get()==2:
        psswdField.insert(0,random.sample(small_alpha+capital_alpha,psswd_len))
    elif choice.get()==3:
        psswdField.insert(0,random.sample(small_alpha+capital_alpha+numbers+special_character,psswd_len))
    # password=random.sample(all,psswd_len)
    # psswdField.insert(0,password)
def copy():
   random_pswd= psswdField.get()
   pyperclip.copy(random_pswd)
 

root=Tk()
root.config(bg='#856ff8')
choice=IntVar()

passwdLabel=Label(root,text="Password Generator",font=('great vibes',25,'bold'),bg='#856ff8',fg='white')
passwdLabel.grid(pady=10)
weakradio=Radiobutton(root,text='Weak',value=1,variable=choice,font=('helventica',13,'bold'),bg='#856ff8',fg='white')
weakradio.grid()

medradio=Radiobutton(root,text='Medium',value=2,variable=choice,font=('helventica',13,'bold'),bg='#856ff8',fg='white')
medradio.grid()

strongradio=Radiobutton(root,text='Strong',value=3,variable=choice,font=('helventica',13,'bold'),bg='#856ff8',fg='white')
strongradio.grid()

lenLabel=Label(root,text="Password length",font=('great vibes',25,'bold'),bg='#856ff8',fg='white')
lenLabel.grid(pady=5)
len_box=Spinbox(root,from_=5,to_=18,width=5,font=('great vibes',25,'bold'),bg='white',fg='black')
len_box.grid(pady=5)
generatebutton=Button(root,text='Generate',font=('great vibes',25,'bold'),bg='gray20',fg='white',command=generator)
generatebutton.grid(pady=5)
psswdField=Entry(root,width=15,bd=2,font=('helventica',20,'bold'),bg='white',fg='black')
psswdField.grid()
copybutton=Button(root,text='copy',font=('great vibes',25,'bold'),bg='gray20',fg='white',command=copy)
copybutton.grid(pady=5)
root.mainloop()
