import tkinter as tk
import tkinter.messagebox
import random

number = random.randint(1,100)
g=[] 

def reset_number():
    global number, g
    number = random.randint(1,100)
    g=[] 

def set_number ():
    global number, g
    user_geuss = int(entry.get())
    try:
        user_guess = int(user_geuss)
    except ValueError:
        tkinter.messagebox.showinfo('GUESSING GAME', 'Please enter an integer between 1 and 100.')
        return
 
    if user_geuss <1 or user_geuss>100:
        tkinter.messagebox.showinfo('GUESSING GAME','OUT OF BOUNDS, try again')
        return
    
    if user_geuss == number:
        tkinter.messagebox.showinfo('GUESSING GAME','CONGRAGOLATIONS! You guessed the number!')
        if tkinter.messagebox.askyesno('GUESSING GAME','DO TOU WANT TO PLAY AGAIN? '):
            reset_number()
            entry.delete(0, tk.END)
        return    

    if g[-2]:
        if abs(number- user_geuss) < abs(number - g[-2]):
            tkinter.messagebox.showinfo('GUESSING GAME','WARMER')
        else:
            tkinter.messagebox.showinfo('GUESSING GAME','COLDER')

    if abs(number -user_geuss)>=10:
        tkinter.messagebox.showinfo('GUESSING GAME','COLD')
    else:
        tkinter.messagebox.showinfo('GUESSING GAME','WARM')  
          
    g.append(user_geuss)

root = tk.Tk()
root.title('GEUSSING GAME')

label= tk.Label(root, text="guess a random number in range 1 to 100 correctly:"+\
                "\nIf your guess is more than 10 away from my number, I'll tell you you're COLD"+\
                "\nIf your guess is within 10 of my number, I'll tell you you're WARM"+\
                "\nIf your guess is farther than your most recent guess, I'll say you're getting COLDER"+\
                "\nIf your guess is closer than your most recent guess, I'll say you're getting WARMER"+\
                "\nLET'S PLAY!")
label.pack()
entry= tk.Entry(root)
entry.pack()

button = tk.Button(root, text='SUBMIT', command=set_number)
button.pack()

root.mainloop() 