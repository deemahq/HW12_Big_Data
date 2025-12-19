# Modified by: Deemah Qaq
# Assignment: HW12 Big Data
# Based on Deitel & Deitel, Section 17.2

import sqlite3
import pandas as pd

def main():
    connection = sqlite3.connect('books.db')

    print("Authors Table:")
    print(pd.read_sql('SELECT * FROM authors', connection, index_col='id'))
    print()

    print("Titles Table:")
    print(pd.read_sql('SELECT * FROM titles', connection))
    print()

    print("Author_ISBN Table:")
    print(pd.read_sql('SELECT * FROM author_ISBN', connection))
    print()

    connection.close()

if __name__ == "__main__":
    main()
