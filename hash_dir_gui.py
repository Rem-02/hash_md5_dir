"""Module that contains the GUI for the hash dir
"""

from tkinter import Button, Label, Tk, filedialog, StringVar, Entry, X
from hash_dir import get_hash_of_dir

class HashDirGUI:
    """Class for the GUI
    """
    def __init__(self):
        """Constructor
        """
        # The GUI
        self.i_window = Tk()
        self.i_window.title("Hash Dir GUI")

        # Group to select the folder
        self.i_label_dir_var = StringVar()
        self.i_label_dir_var.set("Choisir un dossier")
        label_dir = Label(self.i_window, textvariable=self.i_label_dir_var)
        label_dir.pack(padx=5, pady=2)
        button_browse = Button(self.i_window, text="Parcourir...", command=self.browse_button)
        button_browse.pack(padx=5, pady=2)

        # Group to provide an extensions filter
        label_filter = Label(self.i_window, text="Filtre d'extensions de fichier (séparés par des ,)")
        label_filter.pack(padx=5, pady=2)
        self.i_filter_var = StringVar()
        entry_filter = Entry(self.i_window, textvariable=self.i_filter_var)
        entry_filter.pack(fill=X, padx=5, pady=2)

        # Group to compute the MD5 Hash
        button_hash = Button(self.i_window, text="Obtenir le hash MD5", command=self.hash)
        button_hash.pack(padx=5, pady=2)
        self.i_hash_var = StringVar()
        label_hash = Label(self.i_window, text="Hash MD5 : (Copié automatiquement)")
        label_hash.pack(padx=5, pady=2)
        entry_hash = Entry(self.i_window, textvariable=self.i_hash_var, state="readonly", justify="center")
        entry_hash.pack(fill=X, padx=5, pady=2)

        # Vars
        self.i_folder_path = ""

    def browse_button(self):
        """Use to browse a folder
        """
        self.i_folder_path = filedialog.askdirectory()
        # Set the label the the folder
        self.i_label_dir_var.set(f"Dossier : {self.i_folder_path}")

    def hash(self):
        """Use to hash the selected folder
        """
        # Verify a folder is selected
        if not self.i_folder_path:
            return
        # Get the filter
        raw_filter = self.i_filter_var.get()
        ext_filter = list()
        for item in raw_filter.split(","):
            if item.strip():
                ext_filter.append(item.strip())
        txt_hash = str(get_hash_of_dir(self.i_folder_path, ext_filter))
        # Display the result
        self.i_hash_var.set(txt_hash)
        # Copy it to the clipboard
        self.i_window.clipboard_clear()
        self.i_window.clipboard_append(txt_hash)

    def show(self):
        """Show the GUI
        """
        self.i_window.mainloop()

if __name__ == "__main__":
    def main():
        """ Main """
        gui = HashDirGUI()
        gui.show()
    main()
