import random
import tkinter as tk
import secrets
#import string
from tkinter import messagebox


#Adding usernames and passwords to list 

def add():
    #User input
    username = usernameInput.get()
    password = passwordInput.get()
    if username and password:
        with open("passwordList.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Complete", "Password Saved")
    else:
        messagebox.showerror("Error", "Missing Information")

#Deleting usernames and passwords from list

def delete():
    #Username input
    username = usernameInput.get()

    #List to store passwords
    storePasswords = []

    #
    try:
        with open("passwordList.txt", 'r') as f:
            for x in f:
                i = x.split(' ')
                if i[0] != username:
                    storePasswords.append(f"{i[0]} {i[1]}")

        # writing the modified data back to the file
        with open("passwordList.txt", 'w') as f:
            for line in storePasswords:
                f.write(line)

        #Password Successfully Deleted
        messagebox.showinfo(
            "Success", f"User {username} deleted successfully!")
        #Error deleteing password
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")
        
   
#Password list
     
def password_list():
    #List for all the passwords
    passwordList = {}

    #Check password list; if there are no passwords stored it will print an error
    try:
        with open("passwordList.txt", 'r') as f:
            for x in f:
                i = x.split(' ')
                passwordList[i[0]] = i[1]
    except:
        print("No Saved Passwords")

#Print Message
    if passwordList:
        message = "List of Passwords: \n"
        for name, password in passwordList.items():
            message += f"Password for {name} is {password}\n"
        messagebox.showinfo("Passwords", message)
    else:
        messagebox.showinfo("Passwords", "Password List Empty")    
         
def RNG():
    random_number = random.randint(243985734985, 9237894293847232)  
       
    #Print the password
    if random_number: 
        messagebox.showinfo("Randomly Generated Password", random_number)
        
        
#Loop/Dimensions  
        
if __name__ == "__main__":
    window = tk.Tk()
    window.iconbitmap("C:/Users/njade/OneDrive/Documents/PW Manager V2/PW-Manager/logo.ico")      
    window.geometry("350x250")
    window.title("The Best Password Manager!")

    #Username line
    labelUsername = tk.Label(window, text="Website Name:")
    labelUsername.grid(row=0, column=0, padx=15, pady=15)
    usernameInput = tk.Entry(window)
    usernameInput.grid(row=0, column=1, padx=15, pady=15)

    #Password line
    #change labelpassword
    labelPassword = tk.Label(window, text="Password:")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    passwordInput = tk.Entry(window)
    passwordInput.grid(row=1, column=1, padx=10, pady=5)

    #Password List
    buttonPassword_list = tk.Button(window, text="Password List", command=password_list)
    buttonPassword_list.grid(row=2, column=0, padx=10, pady=5)
    
    #Add
    buttonAdd = tk.Button(window, text="Add", command=add)
    buttonAdd.grid(row=2, column=1, padx=10, pady=5)

    #Delete
    buttonDelete = tk.Button(window, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=10, pady=5)

    #RNG
    buttonRNG = tk.Button(text="Create Random Password", command=RNG)
    buttonRNG.grid(row=3, column=0, padx=10, pady=20)
    
    
    window.mainloop()