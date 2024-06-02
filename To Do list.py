import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")
        self.tasks = []

        # Create widgets
        self.entry_task = tk.Entry(self.root, width=50,bg="yellow")
        self.btn_add = tk.Button(self.root, text="Add Task",font=16, command=self.add_task)
        self.listbox_tasks = tk.Listbox(self.root, width=40,font=40, height=10)
        self.btn_mark_done = tk.Button(self.root, text="Mark Done",font=160, command=self.mark_done,bg="pink")

        # Pack widgets
        self.entry_task.pack(pady=10)
        self.btn_add.pack()
        self.listbox_tasks.pack()
        self.btn_mark_done.pack()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def mark_done(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.listbox_tasks.delete(task_index)
        else:
            messagebox.showerror("Error", "Select a task to mark as done.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ToDoListApp()
app.run()


        


        

    

       
       
       
        

        
       

  
