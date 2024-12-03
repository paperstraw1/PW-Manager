import random
import tkinter as tk
import secrets
import string
import uuid
import pyperclip
from tkinter import messagebox


#Copy to clipboard
def clipboard():
    password = passwordInput.get()  # Get the password from the input field
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Clipboard", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")
        

#Gathering user input to add usernames and passwords to list 

def add():
    #User input
    web = usernameInput.get()
    password = passwordInput.get()
    
    #Saving user input and printing a complete or error message
    if web and password:
        with open("passwordList.txt", 'a') as f:
            f.write(f"{web} {password}\n")
        messagebox.showinfo("Complete", "Password Saved")
    else:
        messagebox.showerror("Error", "Missing Information")


#Deleting usernames and passwords from list

def delete():
    #Username input
    web = usernameInput.get()

    #List to store passwords
    storePasswords = []

    #Deleting password
    try:
        with open("passwordList.txt", 'r') as f:
            for x in f:
                i = x.split(' ')
                if i[0] != web:
                    storePasswords.append(f"{i[0]} {i[1]}")
        with open("passwordList.txt", 'w') as f:
            for line in storePasswords:
                f.write(line)

        #Password Successfully Deleted
        messagebox.showinfo(
            "Success", f"Password{web} deleted successfully!")
        #Error deleteing password
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting password {web}: {e}")
        
   
#Password list
     
def password_list():
    #List for all the passwords
    passwordList = {}

    #Check password list; if there are no passwords stored, it will print an error
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
        for web, password in passwordList.items():
            message += f"Password for {web} is {password}\n"
        messagebox.showinfo("Passwords", message)
    else:
        messagebox.showinfo("Passwords", "Password List Empty")    
    
         
#Generate random password
    
def RNG():
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + "!@#$%^&*") for _ in range(15))
    
    #Display password
    passwordInput.delete(0, tk.END)
    passwordInput.insert(0, password)
    messagebox.showinfo("Generated Password", f"Your new password: {password}")
        
        
#Loop/Dimensions  
        
if __name__ == "__main__":
    window = tk.Tk()
    window.iconbitmap("C:/Users/njade/OneDrive/Documents/PW Manager V2/PW-Manager/logo.ico")      
    window.geometry("350x250")
    window.title("The Best Password Manager!")

    #Username line
    labelUsername = tk.Label(window, text="Website Name:")
    labelUsername.grid(column=0, row=0, padx=15, pady=15)
    usernameInput = tk.Entry(window)
    usernameInput.grid(column=1, row=0, padx=15, pady=15)

    #Password line
    #change labelpassword
    labelPassword = tk.Label(window, text="Password:")
    labelPassword.grid(column=0, row=1, padx=10, pady=5)
    passwordInput = tk.Entry(window)
    passwordInput.grid(column=1, row=1, padx=10, pady=5)

    #Password List
    buttonPassword_list = tk.Button(window, text="Password List", command=password_list)
    buttonPassword_list.grid(column=0, row=2, padx=10, pady=5)
    
    #Add
    buttonAdd = tk.Button(window, text="Add", command=add)
    buttonAdd.grid( column=1, row=2, padx=10, pady=5)

    #Delete
    buttonDelete = tk.Button(window, text="Delete", command=delete)
    buttonDelete.grid(column=1, row=3, padx=10, pady=5)

    #RNG
    buttonRNG = tk.Button(text="Create Random Password", command=RNG)
    buttonRNG.grid(column=0, row=3, padx=10, pady=20)
    
    #Copy to Clipboard
    buttonCopy = tk.Button(window, text="Copy to Clipboard", command=clipboard)
    buttonCopy.grid(column=0, row=4, columnspan=2, pady=10)
    
    
    window.mainloop()