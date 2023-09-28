import tkinter as tk

def add_task():
    task = entry_add_items.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry_add_items.delete(0, tk.END)

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        new_task = entry_edit.get()
        if new_task:
            task_listbox.delete(index)
            task_listbox.insert(index, new_task)
            edit_window.destroy()

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task_listbox.delete(index)

def open_edit_window():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = task_listbox.get(index)
        global edit_window
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")

        edit_label = tk.Label(edit_window, text="Edit Task:")
        edit_label.pack()

        global entry_edit
        entry_edit = tk.Entry(edit_window)
        entry_edit.pack()

        entry_edit.insert(tk.END, task)

        edit_button = tk.Button(edit_window, text="Save", command=edit_task)
        edit_button.pack()

root = tk.Tk()
root.geometry("800x400")

canvas = tk.Canvas(root, height=400, width=800)
canvas.pack()

frame = tk.Frame(root, bg='green')
frame.place(relheight=0.2, relwidth=1)

label = tk.Label(frame, text='ToDo List', fg='black', bg='green')
label.pack(side='left')

# ADD ITEMS
frame_add_items = tk.Frame(root)
frame_add_items.place(rely=0.2, relheight=0.1, relwidth=1)
label_add_items = tk.Label(frame_add_items, text='Add Items')
label_add_items.pack(side='left', anchor='n')
entry_add_items = tk.Entry(frame_add_items)
entry_add_items.pack(side='left', padx=5, pady=5)

submit_button = tk.Button(frame_add_items, text='Add Task', command=add_task)
submit_button.pack(side='left', padx=5)

# tasks
tasks_frame = tk.Frame(root)
tasks_frame.place(rely=0.3, relheight=0.7, relwidth=1)

tasks_label = tk.Label(tasks_frame, text='Tasks', fg='black')
tasks_label.pack(side='left', anchor='n')

# task listbox
task_listbox = tk.Listbox(tasks_frame, selectbackground='gray')
task_listbox.pack(expand=True, fill='both')

# Edit and Delete Buttons
edit_button = tk.Button(tasks_frame, text="Edit", command=open_edit_window)
edit_button.pack(side='left', padx=5)

delete_button = tk.Button(tasks_frame, text="Delete", command=delete_task)
delete_button.pack(side='left', padx=5)

root.mainloop()