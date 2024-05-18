import tkinter as tk
from tkinter import Button, Label, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import cv2
import PIL
from tkinter import ttk
import sys

def rotasi_90_derajat_jarum_jam(image):
    if image is None:
        return
    
    baris, kolom, _ = image.shape
    matriks_rotasi = np.zeros((kolom, baris, image.shape[2]), dtype=image.dtype)
    for i in range(baris):
        for j in range(kolom):
            matriks_rotasi[j, baris-1-i] = image[i, j]
    return matriks_rotasi

def rotasi_90_derajat_berlawanan_jarum_jam(image):
    if image is None:
        return
    
    baris, kolom, _ = image.shape
    matriks_rotasi = np.zeros((kolom, baris, image.shape[2]), dtype=image.dtype)
    for i in range(baris):
        for j in range(kolom):
            matriks_rotasi[kolom-1-j, i] = image[i, j]
    return matriks_rotasi

def pencerminan_horizontal(image):
    if image is None:
        return

    baris, kolom, _ = image.shape
    matriks_pencerminan = np.zeros((baris, kolom, image.shape[2]), dtype=image.dtype)
    for i in range(baris):
        for j in range(kolom):
            matriks_pencerminan[i, kolom-1-j] = image[i, j]
    return matriks_pencerminan

def pencerminan_vertikal(image):
    if image is None:
        return

    baris, kolom, _ = image.shape
    matriks_pencerminan = np.zeros((baris, kolom, image.shape[2]), dtype=image.dtype)
    for i in range(baris):
        for j in range(kolom):
            matriks_pencerminan[baris-1-i, j] = image[i, j]
    return matriks_pencerminan

def process_image():
    global original_image
    
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if not file_path:
        return
    
    reset_program()
    
    original_image = cv2.imread(file_path)
    if original_image is None:
        return
    
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    original_image_pil = Image.fromarray(original_image)
    original_image_pil.thumbnail((344, 344))  # Resize image for display
    original_image_tk = ImageTk.PhotoImage(original_image_pil)
    image_label.config(image=original_image_tk)
    image_label.image = original_image_tk


def simpan_gambar_hasil():
    global processed_image

    if processed_image is None:
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png")])
    if not file_path:
        return
    
    cv2.imwrite(file_path, cv2.cvtColor(processed_image, cv2.COLOR_RGB2BGR))
    
def simpan_nilai_intensitas_to_excel(image):
    global file_path
    
    if image is None:
        return
    
    data = []
    baris, kolom, _ = image.shape
    for i in range(baris):
        for j in range(kolom):
            R, G, B = image[i, j]
            data.append([f"f({i}, {j})", R, G, B])
    
    df = pd.DataFrame(data, columns=["Piksel", "R", "G", "B"])

    # Munculkan dialog penyimpanan file Excel
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela root
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    if file_path:
        max_sheet_size = 1048576  # Maksimum ukuran lembar kerja Excel
        num_rows = df.shape[0]
        num_sheets = (num_rows - 1) // max_sheet_size + 1

        with pd.ExcelWriter(file_path) as writer:
            for i in range(num_sheets):
                start_idx = i * max_sheet_size
                end_idx = min((i + 1) * max_sheet_size, num_rows)
                df_subset = df.iloc[start_idx:end_idx]
                sheet_name = f"Sheet_{i+1}"
                df_subset.to_excel(writer, sheet_name=sheet_name, index=False)

        # messagebox.showinfo("Info", f"Data nilai piksel telah disimpan ke dalam file Excel '{file_path}' dengan {num_sheets} lembar kerja.")

def file_open():
    global file_path

    if file_path:
        try:
            filename = r"{}".format(file_path)
            df = pd.read_excel(filename)

            # Set up new treeview
            my_tree["column"] = list(df.columns)
            my_tree["show"] = "headings"
            
            # Loop thru column list for headers
            for column in my_tree["column"]:
                my_tree.heading(column, text=column)
                my_tree.column(column, width=184)

            # Put data in treeview
            df_rows = df.to_numpy().tolist()
            for row in df_rows:
                my_tree.insert("", "end", values=row)
            
            # Pack the treeview finally
            my_tree.pack()

        except ValueError:
            print("File Couldn't Be Opened...try again!")
        except FileNotFoundError:
            print("File Couldn't Be Found...try again!")
    
def process_image_excel():
    global original_image

    simpan_nilai_intensitas_to_excel(original_image)
    file_open()

def process_image_result(process_function):
    global processed_image, original_image
    
    if processed_image is not None:
        image_to_process = processed_image
    elif original_image is not None:
        # image_to_process = np.array(original_image)
        image_to_process = original_image
    else:
        return

    processed_image = process_function(image_to_process)
    processed_image_pil = Image.fromarray(processed_image.astype(np.uint8))
    processed_image_pil.thumbnail((344, 344))  # Resize image for display
    image_result_tk = ImageTk.PhotoImage(processed_image_pil)
    image_result_label.config(image=image_result_tk)
    image_result_label.image = image_result_tk

def reset_program():
    global original_image, processed_image, file_path

    # Reset the global variables
    original_image = None
    processed_image = None
    file_path = None

    # Reset the image labels
    my_tree.delete(*my_tree.get_children())

    image_label.config(image=newBlank1)
    image_label.image = newBlank1
    image_result_label.config(image=newBlank2)
    image_result_label.image = newBlank2

def exit_program():
    # global file_path

    # if os.path.exists(file_path):
    #     os.remove(file_path)

    app.destroy()
    sys.exit()
     
app = tk.Tk()
app.geometry('1280x720')
app.title("Itensity & Transform")
app.configure(background='#242424')

# Global variables
original_image = None
processed_image = None
file_path = None

notebook = ttk.Notebook(app)
labeljudul1 = Label(app, text="Intensity & Transform")
labeljudul1.place(x=49, y=36, width=348, height=44)
labeljudul2 = Label(app, text="Method")
labeljudul2.place(x=464, y=36, width=772, height=44)
labelgambar1 = Label(app)
labelgambar1.place(x=49, y=86, width=348, height=24)
labelgambar2 = Label(app, text="Gambar Awal")
labelgambar2.place(x=49, y=116, width=348, height=30)

# Frame for original image
newBlank1 = PIL.Image.new('RGB', (344, 344), (255, 255, 255))
newBlank1 = PIL.ImageTk.PhotoImage(newBlank1)
image_label = tk.Label(image=newBlank1)
image_label.place(x=49, y=152)

buttoninsert = Button(app, text="Load Image", command=process_image)
buttoninsert.place(x=49, y=510, width=348, height=44)
buttonprocess = Button(app, text="Process Image", command=process_image_excel)
buttonprocess.place(x=49, y=564, width=348, height=44)
buttonreset = Button(app, text="Reset", command=reset_program)
buttonreset.place(x=464, y=564, width=380, height=44)
buttonexit = Button(app, text="Exit", command=exit_program)
buttonexit.place(x=856, y=564, width=380, height=44)

# tab 1
tab1 = ttk.Frame(notebook)
my_tree = ttk.Treeview(tab1)

# tab 2
tab2 = ttk.Frame(notebook)
labelgambar4 = Label(tab2, text="Metode Rotasi")
labelgambar4.place(x=4, y=44, width=380, height=40)
button11 = Button(tab2, text="Rotate 90° Clockwise", command=lambda: process_image_result(rotasi_90_derajat_jarum_jam))
button11.place(x=4, y=90, width=380, height=40)
button12 = Button(tab2, text="Rotate 90° Counter Clockwise", command=lambda: process_image_result(rotasi_90_derajat_berlawanan_jarum_jam))
button12.place(x=4, y=136, width=380, height=40)
labelgambar4 = Label(tab2, text="Metode Refleksi")
labelgambar4.place(x=4, y=200, width=380, height=40)
button1 = Button(tab2, text="Mirror Horizontal", command=lambda: process_image_result(pencerminan_horizontal))
button1.place(x=4, y=256, width=380, height=40)
button1 = Button(tab2, text="Mirror Vertical", command=lambda: process_image_result(pencerminan_vertikal))
button1.place(x=4, y=302, width=380, height=40)
labelgambar3 = Label(tab2, text="Gambar Hasil")
labelgambar3.place(x=420, y=6, width=348, height=30)

#Frame for processed image
newBlank2 = PIL.Image.new('RGB', (344, 344), (255, 255, 255))
newBlank2 = PIL.ImageTk.PhotoImage(newBlank2)
image_result_label = tk.Label(tab2, image=newBlank2)
image_result_label.place(x=420, y=44)

buttoninsert = Button(tab2, text="Save Gambar", command=simpan_gambar_hasil)
buttoninsert.place(x=420, y=394, width=170, height=44)
buttonsavepixel = Button(tab2, text="Save Pixel", command=lambda: simpan_nilai_intensitas_to_excel(processed_image))
buttonsavepixel.place(x=598, y=394, width=170, height=44)

notebook.add(tab1, text='                                                       Intensity                                                       ')
notebook.add(tab2, text='                                                       Transform                                                       ')

# Set a specific size for the tabs
notebook.place(x=464, y=86, width=772, height=468)

app.mainloop()