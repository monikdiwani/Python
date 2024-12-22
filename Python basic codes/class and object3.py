#WAP to print bookdata as title,year,author etc with class and object concept

class Book:
    def __init__(self, title, year, author, genre):
        # Initializes the book object
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre

    def display_info(self):
        # Displays book information
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

# Creating book objects
book1 = Book("Malgudi Days", 1943, "R. K. Narayan", "Fiction")
book2 = Book("The God of Small Things", 1997, "Arundhati Roy", "Fiction")
book3 = Book("Train to Pakistan", 1956, "Khushwant Singh", "Historical Fiction")

# Displaying book information
book1.display_info()
book2.display_info()
book3.display_info()
