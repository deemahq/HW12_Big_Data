# Modified by: Deemah Qaq
# Assignment: HW12 Part III – Exercise 17.1
# Textbook: Deitel & Deitel – Intro to Python for Computer Science and Data Science

import sqlite3
import pandas as pd

def main():
    connection = sqlite3.connect('books.db')

    print("a) Authors last names (descending):")
    print(pd.read_sql(
        "SELECT last FROM authors ORDER BY last DESC;",
        connection
    ))
    print()

    print("b) Book titles (ascending):")
    print(pd.read_sql(
        "SELECT title FROM titles ORDER BY title ASC;",
        connection
    ))
    print()

    print("c) Books by author Deitel:")
    print(pd.read_sql(
        """
        SELECT title, copyright, titles.isbn
        FROM titles
        INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
        INNER JOIN authors ON authors.id = author_ISBN.id
        WHERE authors.last = 'Deitel'
        ORDER BY title;
        """,
        connection
    ))
    print()

    cursor = connection.cursor()

    print("d) Inserting new author...")
    cursor.execute(
        "INSERT INTO authors (id, first, last) VALUES (6, 'Jane', 'Smith');"
    )

    print("e) Inserting new title and linking author...")
    cursor.execute(
        """
        INSERT INTO titles (isbn, title, edition, copyright)
        VALUES ('9999999999', 'Python for Data Analysis', 1, 2024);
        """
    )

    cursor.execute(
        "INSERT INTO author_ISBN (id, isbn) VALUES (6, '9999999999');"
    )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
