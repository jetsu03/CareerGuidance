import csv
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def print_college_info(info):
    details = (f"College Number: {info[0]}\n"
               f"College Name: {info[2]}\n"
               f"Stream: {info[1]}\n"
               f"Place: {info[3]}\n"
               f"Entrance Exam: {info[4]}\n"
               f"Cutoff / Rank Required: {info[5]}\n"
               f"College Fees: {info[6]}\n"
               f"College Specialisation: {info[7]}\n"
               f"College Link: {info[8]}\n")
    return details
def process_stream_place():
    stream_map = {
        'Arts': 'arts',
        'Medical': 'medical',
        'Engineering': 'engineering',
        'Commerce': 'commerce'
    }
    
    place_map = {
        'Delhi': 'delhi',
        'Chennai': 'chennai',
        'Kolkata': 'kolkata',
        'Mumbai': 'mumbai',
        'Bangalore': 'bangalore',
        'Hyderabad': 'hyderabad'
    }
    
    stream = stream_var.get()
    place = place_var.get()
    
    stream_name = stream_map.get(stream)
    place_name = place_map.get(place)
    
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)  
    
    found = False
    for i in data:
        if i[1].lower() == stream_name and i[3].lower() == place_name:
            result_text.insert(tk.END, print_college_info(i) + '\n')
            found = True
    
    if not found:
        result_text.insert(tk.END, "No colleges found matching the selected criteria.\n")
    
    result_text.config(state=tk.DISABLED)  
def open_college_link():
    number = number_entry.get()
    url = dict_from_csv.get(number)
    if url:
        webbrowser.open(url, new=2)
    else:
        messagebox.showerror("Error", "No URL found for this number.")
with open("comp3.csv", "r") as f:
    h = list(csv.reader(f))

data = h
dict_from_csv = {i[0]: i[8] for i in h}
root = tk.Tk()
root.title("Career Guidance Portal")
tk.Label(root, text="Welcome to Career Guidance Portal!").pack(pady=10)

tk.Label(root, text="Select Stream:").pack()
stream_var = tk.StringVar()
stream_options = ttk.Combobox(root, textvariable=stream_var, values=["Arts", "Medical", "Engineering", "Commerce"])
stream_options.pack()

tk.Label(root, text="Select Place:").pack()
place_var = tk.StringVar()
place_options = ttk.Combobox(root, textvariable=place_var, values=["Delhi", "Chennai", "Kolkata", "Mumbai", "Bangalore", "Hyderabad"])
place_options.pack()

search_button = tk.Button(root, text="Search", command=process_stream_place)
search_button.pack(pady=10)
frame = tk.Frame(root)
frame.pack(pady=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text = tk.Text(frame, height=15, width=80, wrap=tk.WORD, yscrollcommand=scrollbar.set)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=result_text.yview)

tk.Label(root, text="Enter College Number to get URL:").pack()
number_entry = tk.Entry(root)
number_entry.pack()

link_button = tk.Button(root, text="Open Link", command=open_college_link)
link_button.pack(pady=10)

root.mainloop()
