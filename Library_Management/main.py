import tkinter as tk
from tkinter import messagebox, simpledialog

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        if book_name:
            self.books.append(book_name)

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            return True
        return False

    def get_books(self):
        return self.books

    def total_books(self):
        return len(self.books)

class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x500")

        self.title_label = tk.Label(root, text="Library Management", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.books_listbox = tk.Listbox(root, width=40, height=15)
        self.books_listbox.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Selected Book", command=self.remove_book)
        self.remove_button.pack(pady=5)

        self.display_button = tk.Button(root, text="Display Books", command=self.display_books)
        self.display_button.pack(pady=5)

        self.total_button = tk.Button(root, text="Show Total Books", command=self.show_total)
        self.total_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=20)

    def add_book(self):
        book_name = self.entry.get()
        if book_name.strip() == "":
            messagebox.showwarning("Input Error", "Book name cannot be empty.")
            return
        self.library.add_book(book_name)
        self.entry.delete(0, tk.END)
        self.display_books()

    def remove_book(self):
        selected = self.books_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No book selected to remove.")
            return
        book_name = self.books_listbox.get(selected[0])
        removed = self.library.remove_book(book_name)
        if removed:
            self.display_books()
        else:
            messagebox.showerror("Remove Error", "Book not found.")

    def display_books(self):
        self.books_listbox.delete(0, tk.END)
        for book in self.library.get_books():
            self.books_listbox.insert(tk.END, book)

    def show_total(self):
        total = self.library.total_books()
        messagebox.showinfo("Total Books", f"Total number of books: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
