from typing import List
from dataclasses import dataclass

import tkinter as tk
import webbrowser
from tkinter import messagebox, Listbox


@dataclass
class BaseItem:
    """Базовый класс для всех элементов инвентаря."""
    id: int


@dataclass
class Product(BaseItem):
    """Класс, представляющий продукт в инвентаре."""
    name: str  #: Имя продукта.
    price: float  #: Цена продукта.


@dataclass
class BookItem:
    """Базовый класс для всех элементов инвентаря."""
    book_id: int


@dataclass
class Book(BookItem):
    """Класс, представляющий продукт в инвентаре."""
    author: str
    book_name: str
    genre: str
    book_price: float


@dataclass
class ElectronicsItem:
    """Базовый класс для всех элементов инвентаря."""
    electronics_id: int


@dataclass
class Electronics(ElectronicsItem):
    """Класс, представляющий продукт в инвентаре."""
    brand: str
    electronics_name: str
    electronics_type: str
    electronics_price: float


class InventoryProducts():
    """Класс для управления инвентарем продуктов."""
    def __init__(self):
        """Инициализация инвентаря."""
        self.items: List[Product] = []
        self.books_items: List1[Book] = []
        self.electronics_item: List2[Electronics] = []

    def get_item(self, item_id: int):
        """Получить продукт по его ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def add_item(self, item: Product):
        """Добавить продукт в инвентарь."""
        self.items.append(item)

    def remove_item(self, item_id: int):
        """Удалить продукт из инвентаря."""
        self.items = [item for item in self.items if item.id != item_id]

    def update_item(self, item_id: int, item: Product):
        """Обновить информацию о продуктах."""
        for temp_item in self.items:
            if temp_item.id == item_id:
                temp_item.id = item.id
                temp_item.name = item.name
                temp_item.price = item.price
                return True
        return False

    def list_items(self):
        """Получить список всех продуктов в инвентаре."""
        return self.items

    def get_books_item(self, books_id: int):
        """Получить книгу по его ID."""
        for book in self.books_items:
            if book.id == books_id:
                return book
        return None

    def add_books_item(self, book: Book):
        """Добавить книгу в инвентарь."""
        self.books_items.append(book)

    def remove_books_item(self, books_id: int):
        """Удалить книгу из инвентаря."""
        self.books_items = [book for book in self.books_items if book.id != books_id]

    def update_books_item(self, books_id: int, book: Book):
        """Обновить информацию о книгах."""
        for temp_book_item in self.books_items:
            if temp_book_item.book_id == books_id:
                temp_book_item.book_id = book.book_id
                temp_book_item.author = book.author
                temp_book_item.book_name = book.book_name
                temp_book_item.genre = book.genre
                temp_book_item.book_price = book.book_price
                return True
        return False

    def list_book_items(self):
        """Получить список всех книгах в инвентаре."""
        return self.books_items

    def get_eletronics_item(self, eletroniccs_id: int):
        """Получить технику по его ID."""
        for electronic in self.electroniccs_items:
            if electronic.id == electroniccs_id:
                return electronic
        return None

    def add_electronics_item(self, electronic: Electronics):
        """Добавить технику в инвентарь."""
        self.electroniccs_items.append(Electronics)

    def remove_electronics_item(self, electroniccs_id: int):
        """Удалить технику из инвентаря."""
        self.electroniccs_items = [electronic for electronic in self.electroniccs_items if electronic.electronics_id != electroniccs_id]

    def update_electronics_item(self, electronics_id: int, electronic: Electronics):
        """Обновить информацию о технике."""
        for temp_electronic_item in self.electronics_items:
            if temp_electronic_item.electronics_id == electroniccs_id:
                temp_electronic_item.electronics_id = electronic.electronics_id
                temp_electronic_item.brand = electronic.brand
                temp_electronic_item.electronics_name = electronic.electronics_name
                temp_electronic_item.electronics_type = electronic.electronics_type
                temp_electronic_item.price = electronic.price
                return True
        return False

    def list_electronic_items(self):
        """Получить список всех продуктов в инвентаре."""
        return self.electronics_items


class InventoryApp():
    """Класс для создания приложения управления инвентарем."""
    def __init__(self, master):
        """Инициализация приложения."""
        self.master = master
        master.title("Приложение Управление инвентарём в онлайн-магазине")
        master.geometry("400x300")

        self.product_inventory = InventoryProducts()

        self.label = tk.Label(master, text="Управление инвентарём\nонлайн-магазин", font=("Arial", 18))
        self.label.pack()

        self.master.after(3000, self.show_main_menu)

    def show_main_menu(self):
        """Отображение главного меню."""
        self.label.destroy()

        self.inventory_button = tk.Button(self.master, text="Инвентарь", command=self.open_inventory_menu)
        self.inventory_button.pack()

        self.quit_button = tk.Button(self.master, text="Выйти", command=self.master.quit)
        self.quit_button.pack()

        self.commamd_button = tk.Button(self.master, text="Презентация", command=self.open_link)
        self.commamd_button.pack()

        self.products_button = tk.Button(self.master, text="Продукты", command=self.open_list_products)
        self.products_button.pack()
        self.products_button.destroy()

        self.books_button = tk.Button(self.master, text="Книги", command=self.open_list_books)
        self.books_button.pack()
        self.books_button.destroy()

        self.electronics_button = tk.Button(self.master, text="Техника", command=self.open_list_electronics)
        self.electronics_button.pack()
        self.electronics_button.destroy()

    def open_link(self):
        self.command = webbrowser.open_new("https://www.canva.com/design/DAFgoDCkJfM/t7kbuRIMTzLlbEqXwV80Xw/edit?utm_content=DAFgoDCkJfM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")

    def open_list_products(self):
        pass

    def open_list_books(self):
        pass

    def open_list_electronics(self):
        pass

    def open_inventory_menu(self):
        """Открытие меню инвентаря."""
        self.inventory_button.destroy()
        self.products_button.destroy()
        self.commamd_button.destroy()
        self.books_button.destroy()
        self.electronics_button.destroy()
        self.quit_button.destroy()

        self.inventory_label = tk.Label(self.master, text="Внести изменения", font=("Arial", 16))
        self.inventory_label.pack()

        self.products_list_button = tk.Button(self.master, text="Список продуктов", command=self.open_products_menu)
        self.products_list_button.pack()

        self.books_list_button = tk.Button(self.master, text="Список книг", command=self.open_books_menu)
        self.books_list_button.pack()

        self.electronics_list_button = tk.Button(self.master, text="Список техники", command=self.open_electronics_menu)
        self.electronics_list_button.pack()

        self.quit_button = tk.Button(self.master, text="Выйти", command=self.master.quit)
        self.quit_button.pack()

    def open_products_menu(self):
        """Открытие меню продуктов."""
        self.inventory_label.destroy()
        self.products_list_button.destroy()
        self.books_list_button.destroy()
        self.electronics_list_button.destroy()
        self.quit_button.destroy()

        self.products_label = tk.Label(self.master, text="Выберите изменения", font=("Arial", 16))
        self.products_label.pack()

        self.add_product_button = tk.Button(self.master, text="Добавить новый продукт", command=self.add_product)
        self.add_product_button.pack()

        self.remove_product_button = tk.Button(self.master, text="Удалить продукт", command=self.remove_product)
        self.remove_product_button.pack()

        self.product_listbox = Listbox(self.master, width=60)
        self.product_listbox.pack()

        for product_item in self.product_inventory.list_items():
            self.product_listbox.insert(
                0,
                f"ID: {product_item.id} | Имя продукта: {product_item.name} | Стоимость: {product_item.price}"
            )


    def add_product(self):
        """Добавление нового продукта."""
        self.products_label.destroy()
        self.add_product_button.destroy()
        self.remove_product_button.destroy()
        self.product_listbox.destroy()

        self.add_product_label = tk.Label(self.master, text="Добавить новый продукт")
        self.add_product_label.pack()

        self.id_product_label = tk.Label(self.master, text="ID:")
        self.id_product_label.pack()
        self.id_product_entry = tk.Entry(self.master)
        self.id_product_entry.pack()

        self.name_product_label = tk.Label(self.master, text="Имя продукта:")
        self.name_product_label.pack()
        self.name_product_entry = tk.Entry(self.master)
        self.name_product_entry.pack()

        self.price_product_label = tk.Label(self.master, text="Стоимость:")
        self.price_product_label.pack()
        self.price_product_entry = tk.Entry(self.master)
        self.price_product_entry.pack()

        self.add_button = tk.Button(self.master, text="Добавлено", command=self.add_product_to_inventory)
        self.add_button.pack()

    def add_product_destroy(self):
        """Удаление виджетов после добавления продукта."""
        self.add_product_label.destroy()
        self.id_product_label.destroy()
        self.id_product_entry.destroy()
        self.name_product_label.destroy()
        self.name_product_entry.destroy()
        self.price_product_label.destroy()
        self.price_product_entry.destroy()
        self.add_button.destroy()

    def remove_product(self):
        """Удаление продукта."""
        self.products_label.destroy()
        self.add_product_button.destroy()
        self.remove_product_button.destroy()
        self.product_listbox.destroy()
        self.quit_button.destroy()

        self.remove_product_label = tk.Label(self.master, text="Удалить продукт")
        self.remove_product_label.pack()

        self.id_product_label = tk.Label(self.master, text="ID:")
        self.id_product_label.pack()
        self.id_product_entry = tk.Entry(self.master)
        self.id_product_entry.pack()

        self.remove_button = tk.Button(self.master, text="Удалить", command=self.remove_product_from_inventory)
        self.remove_button.pack()

    def remove_product_destroy(self):
        """Удаление виджетов после удаления продукта."""
        self.remove_product_label.destroy()
        self.id_product_label.destroy()
        self.id_product_entry.destroy()
        self.remove_button.destroy()

    def list_products_items(self):
        """Отображение списка продуктов."""
        items = self.product_inventory.list_items()
        messagebox.showinfo("List of Items", items if items else "No items in inventory")

    def add_product_to_inventory(self):
        """Добавление продукта в инвентарь."""
        product_id = int(self.id_product_entry.get())
        product_name = self.name_product_entry.get()
        product_price = float(self.price_product_entry.get())
        item = Product(product_id, product_name, product_price)
        self.product_inventory.add_item(item)
        messagebox.showinfo("Item Added", f"Added {item}")
        self.master.after(500, self.open_products_menu)
        self.add_product_destroy()

    def remove_product_from_inventory(self):
        """Удаление продукта из инвентаря."""
        product_id = int(self.id_product_entry.get())
        product_item = self.product_inventory.get_item(product_id)
        if product_item:
            self.product_inventory.remove_item(product_id)
            messagebox.showinfo("Item Removed", f"Removed {product_id}")
        else:
            messagebox.showerror("Error", f"Item {product_id} not found")
        self.master.after(500, self.open_products_menu)
        self.remove_product_destroy()

    def open_books_menu(self):
        """Открытие меню книг."""
        self.inventory_label.destroy()
        self.products_list_button.destroy()
        self.commamd_button.destroy()
        self.books_list_button.destroy()
        self.electronics_list_button.destroy()
        self.quit_button.destroy()

        self.books_label = tk.Label(self.master, text="Выберите изменения", font=("Arial", 16))
        self.books_label.pack()

        self.add_book_button = tk.Button(self.master, text="Добавить новую книгу", command=self.add_book)
        self.add_book_button.pack()

        self.remove_book_button = tk.Button(self.master, text="Удалить книгу", command=self.remove_book)
        self.remove_book_button.pack()

        self.book_listbox = Listbox(self.master, width=60)
        self.book_listbox.pack()

        for book_item in self.product_inventory.list_book_items():
            self.book_listbox.insert(
                0,
                f"ID: {book_item.book_id} | Автор: {book_item.author} | Название книги: {book_item.book_name} | Жанр книги: {book_item.genre} | Стоимость: {book_item.book_price}"
            )


    def add_book(self):
        """Добавление новой книги."""
        self.books_label.destroy()
        self.add_book_button.destroy()
        self.remove_book_button.destroy()
        self.book_listbox.destroy()

        self.add_book_label = tk.Label(self.master, text="Добавить новую книгу")
        self.add_book_label.pack()

        self.id_book_label = tk.Label(self.master, text="ID:")
        self.id_book_label.pack()
        self.id_book_entry = tk.Entry(self.master)
        self.id_book_entry.pack()

        self.author_book_label = tk.Label(self.master, text="Автор:")
        self.author_book_label.pack()
        self.author_book_entry = tk.Entry(self.master)
        self.author_book_entry.pack()

        self.name_book_label = tk.Label(self.master, text="Название книги:")
        self.name_book_label.pack()
        self.name_book_entry = tk.Entry(self.master)
        self.name_book_entry.pack()

        self.genre_book_label = tk.Label(self.master, text="Жанр:")
        self.genre_book_label.pack()
        self.genre_book_entry = tk.Entry(self.master)
        self.genre_book_entry.pack()

        self.price_book_label = tk.Label(self.master, text="Стоимость:")
        self.price_book_label.pack()
        self.price_book_entry = tk.Entry(self.master)
        self.price_book_entry.pack()

        self.add_button = tk.Button(self.master, text="Добавлено", command=self.add_book_to_inventory)
        self.add_button.pack()

    def add_book_destroy(self):
        """Удаление виджетов после добавления книги."""
        self.add_book_label.destroy()
        self.id_book_label.destroy()
        self.id_book_entry.destroy()
        self.author_book_label.destroy()
        self.author_book_entry.destroy()
        self.name_book_label.destroy()
        self.name_book_entry.destroy()
        self.genre_book_label.destroy()
        self.genre_book_entry.destroy()
        self.price_book_label.destroy()
        self.price_book_entry.destroy()
        self.add_button.destroy()

    def remove_book(self):
        """Удаление книги."""
        self.books_label.destroy()
        self.add_book_button.destroy()
        self.remove_book_button.destroy()
        self.book_listbox.destroy()
        self.quit_button.destroy()

        self.remove_book_label = tk.Label(self.master, text="Удалить книгу")
        self.remove_book_label.pack()

        self.id_book_label = tk.Label(self.master, text="ID:")
        self.id_book_label.pack()
        self.id_book_entry = tk.Entry(self.master)
        self.id_book_entry.pack()

        self.remove_button = tk.Button(self.master, text="Удалить", command=self.remove_book_from_inventory)
        self.remove_button.pack()

    def remove_book_destroy(self):
        """Удаление виджетов после удаления книги."""
        self.remove_book_label.destroy()
        self.id_book_label.destroy()
        self.id_book_entry.destroy()
        self.remove_button.destroy()

    def list_books_items(self):
        """Отображение списка книги."""
        books_items = self.book_inventory.list_books_items()
        messagebox.showinfo("List of Items", books_items if books_items else "No items in inventory")

    def add_book_to_inventory(self):
        """Добавление книги в инвентарь."""
        books_id = int(self.id_book_entry.get())
        books_author = self.author_book_entry.get()
        books_name = self.name_book_entry.get()
        books_genre = self.genre_book_entry
        books_price = float(self.price_book_entry.get())
        book = Book(books_id, books_author, books_name, books_genre, books_price)
        self.book_inventory.add_books_item(book)
        messagebox.showinfo("Item Added", f"Added {book}")
        self.master.after(500, self.open_books_menu)
        self.add_book_destroy()

    def remove_book_from_inventory(self):
        """Удаление книги из инвентаря."""
        books_id = int(self.id_book_entry.get())
        books_item = self.book_inventory.get_books_item(books_id)
        if books_item:
            self.book_inventory.remove_item(books_id)
            messagebox.showinfo("Item Removed", f"Removed {books_id}")
        else:
            messagebox.showerror("Error", f"Item {books_id} not found")
        self.master.after(500, self.open_books_menu)
        self.remove_book_destroy()

    def open_electronics_menu(self):
        """Открытие меню техники."""
        self.inventory_label.destroy()
        self.products_list_button.destroy()
        self.commamd_button.destroy()
        self.books_list_button.destroy()
        self.electronics_list_button.destroy()
        self.quit_button.destroy()

        self.electronics_label = tk.Label(self.master, text="Выберите изменения", font=("Arial", 16))
        self.electronics_label.pack()

        self.add_electronic_button = tk.Button(self.master, text="Добавить новую технику", command=self.add_electronic)
        self.add_electronic_button.pack()

        self.remove_electronic_button = tk.Button(self.master, text="Удалить продукт", command=self.remove_electronic)
        self.remove_electronic_button.pack()

        self.electronic_listbox = Listbox(self.master, width=60)
        self.electronic_listbox.pack()

        for electronic_item in self.electronic_inventory.list_electronics_items():
            self.electronic_listbox.insert(
                0,
                f"ID: {electronic_item.electronics_id} | Брэнд: {electronic_item.brand} | Название техники: {electronic_item.electronics_name} | Вид техники: {electronic_item.electronics_type} | Стоимость: {electronic_item.electronics_price}"
            )


    def add_electronic(self):
        """Добавление новой техники."""
        self.electronics_label.destroy()
        self.add_electronic_button.destroy()
        self.remove_electronic_button.destroy()
        self.electronic_listbox.destroy()

        self.add_electronic_label = tk.Label(self.master, text="Добавить новую технику")
        self.add_electronic_label.pack()

        self.id_electronic_label = tk.Label(self.master, text="ID:")
        self.id_electronic_label.pack()
        self.id_electronic_entry = tk.Entry(self.master)
        self.id_electronic_entry.pack()

        self.brand_electronic_label = tk.Label(self.master, text="Брэнд:")
        self.brand_electronic_label.pack()
        self.brand_electronic_entry = tk.Entry(self.master)
        self.brand_electronic_entry.pack()

        self.name_electronic_label = tk.Label(self.master, text="Название техники:")
        self.name_electronic_label.pack()
        self.name_electronic_entry = tk.Entry(self.master)
        self.name_electronic_entry.pack()

        self.type_electronic_label = tk.Label(self.master, text="Вид техники:")
        self.type_electronic_label.pack()
        self.type_electronic_entry = tk.Entry(self.master)
        self.type_electronic_entry.pack()

        self.price_electronic_label = tk.Label(self.master, text="Стоимость:")
        self.price_electronic_label.pack()
        self.price_electronic_entry = tk.Entry(self.master)
        self.price_electronic_entry.pack()

        self.add_button = tk.Button(self.master, text="Добавлено", command=self.add_electronic_to_inventory)
        self.add_button.pack()

    def add_elecetronic_destroy(self):
        """Удаление виджетов после добавления техники."""
        self.add_elecetronic_label.destroy()
        self.id_elecetronic_label.destroy()
        self.id_elecetronic_entry.destroy()
        self.brand_electronic_label.destroy()
        self.brand_electronic_entry.destroy()
        self.name_elecetronic_label.destroy()
        self.name_elecetronic_entry.destroy()
        self.type_electronic_label.destroy()
        self.type_electronic_entry.destroy()
        self.price_elecetronic_label.destroy()
        self.price_elecetronic_entry.destroy()
        self.add_elecetronic.destroy()

    def remove_electronic(self):
        """Удаление техники."""
        self.electronics_label.destroy()
        self.add_electronic_button.destroy()
        self.remove_electronic_button.destroy()
        self.electronic_listbox.destroy()
        self.quit_button.destroy()

        self.remove_electronic_label = tk.Label(self.master, text="Удалить товар")
        self.remove_electronic_label.pack()

        self.id_electronic_label = tk.Label(self.master, text="ID:")
        self.id_electronic_label.pack()
        self.id_electronic_entry = tk.Entry(self.master)
        self.id_electronic_entry.pack()

        self.remove_button = tk.Button(self.master, text="Удалить", command=self.remove_electronic_from_inventory)
        self.remove_button.pack()

    def remove_electronic_destroy(self):
        """Удаление виджетов после удаления техники."""
        self.remove_electronic_label.destroy()
        self.id_electronic_label.destroy()
        self.id_electronic_entry.destroy()
        self.remove_button.destroy()

    def list_electronics_items(self):
        """Отображение списка техники."""
        electronics_items = self.electronic_inventory.list_items()
        messagebox.showinfo("List of Items", electronics_items if electronics_items else "No items in inventory")

    def add_electronic_to_inventory(self):
        """Добавление техники в инвентарь."""
        electronic_id = int(self.id_product_entry.get())
        electronic_brand = self.brand_electronic_entry.get()
        electronic_name = self.name_product_entry.get()
        electronic_type = self.type_electronic_entry.get()
        electronic_price = float(self.price_product_entry.get())
        electronic_item = Electronics(electronic_id, electronic_brand, electronic_name,electronic_type, electronic_price)
        self.electronic_inventory.add_electronic_item(electronic)
        messagebox.showinfo("Item Added", f"Added {electronic}")
        self.master.after(500, self.open_electronics_menu)
        self.add_electronic_destroy()

    def remove_electronic_from_inventory(self):
        """Удаление техники из инвентаря."""
        electronic_id = int(self.id_electronic_entry.get())
        electronic_item = self.electronic_inventory.get_electronic_item(electronic_id)
        if electronic_item:
            self.electronic_inventory.remove_electronic_item(electronic_id)
            messagebox.showinfo("Item Removed", f"Removed {electronic_id}")
        else:
            messagebox.showerror("Error", f"Item {electronic_id} not found")
        self.master.after(500, self.open_electronics_menu)
        self.remove_electronic_destroy()


def main():
    """Главная функция."""
    product = Product(id=1, name="1", price=1)
    product2 = Product(id=2, name="2", price=2)
    inv = InventoryProducts()
    inv.add_item(product)
    inv.add_item(product2)
    print(inv.list_items())
    product = Product(id=1, name="a", price=1)
    inv.update_item(1, product)
    print(inv.list_items())
    book = Book(id=1, name="1", price=1)
    book2 = Book(id=2, name="2", price=2)
    inv = InventoryProducts()
    inv.add_book_item(book)
    inv.add_book_item(book2)
    print(inv.list_books_items())
    bood = Book(id=1, name="a", price=1)
    inv.update_book_item(1, book)
    print(inv.list_books_items())
    electronic = Electronics(id=1, name="1", price=1)
    electronic2 = Electronics(id=2, name="2", price=2)
    inv = InventoryProducts()
    inv.add_electronic_item(electronic)
    inv.add_electronic_item(electronic2)
    print(inv.list_electronic_items())
    electronic = Electronics(id=1, name="a", price=1)
    inv.update_electronic_item(1, electronic)
    print(inv.list_electronic_items())

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()