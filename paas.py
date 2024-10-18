import streamlit as st
import os
import json

# Define the files to store books and users
book_file = 'books.json'
user_file = 'users.json'

# Load books and users from files or create new files
def load_books():
    if os.path.exists(book_file):
        with open(book_file, 'r') as file:
            return json.load(file)
    return []

def load_users():
    if os.path.exists(user_file):
        with open(user_file, 'r') as file:
            return json.load(file)
    return []

def save_books(books):
    with open(book_file, 'w') as file:
        json.dump(books, file, indent=4)

def save_users(users):
    with open(user_file, 'w') as file:
        json.dump(users, file, indent=4)

# Streamlit app
def main():
    st.set_page_config(page_title="Library Management System", page_icon="📚")
    st.title("Library Management System")
    
    # Sidebar for navigation
    menu = ["Add Book", "View Books", "Borrow Book", "Return Book", "Register User", "View Users"]
    choice = st.sidebar.selectbox("Select an option", menu)

    st.markdown("---")  # Horizontal line for separation

    if choice == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Enter book title")
        author = st.text_input("Enter book author")
        
        if st.button("Add Book"):
            if title and author:
                books = load_books()
                books.append({'title': title, 'author': author, 'available': True})
                save_books(books)
                st.success(f"Book '{title}' added.", icon="✅")
            else:
                st.error("Please fill in all fields.", icon="🚫")

    elif choice == "View Books":
        st.subheader("Available Books")
        books = load_books()
        if books:
            for i, book in enumerate(books):
                status = 'Available' if book['available'] else 'Borrowed'
                st.markdown(f"**{i + 1}. {book['title']}** by *{book['author']}* - {status}")
                st.markdown("---")
        else:
            st.info("No books available.")

    elif choice == "Borrow Book":
        st.subheader("Borrow a Book")
        books = load_books()
        if books:
            book_id = st.number_input("Enter the book ID to borrow", min_value=1, max_value=len(books), step=1)
            if st.button("Borrow"):
                if books[book_id - 1]['available']:
                    books[book_id - 1]['available'] = False
                    save_books(books)
                    st.success(f"You have borrowed '{books[book_id - 1]['title']}'.", icon="✅")
                else:
                    st.error("This book is already borrowed.", icon="🚫")
        else:
            st.info("No books available to borrow.")

    elif choice == "Return Book":
        st.subheader("Return a Book")
        books = load_books()
        if books:
            book_id = st.number_input("Enter the book ID to return", min_value=1, max_value=len(books), step=1)
            if st.button("Return"):
                if not books[book_id - 1]['available']:
                    books[book_id - 1]['available'] = True
                    save_books(books)
                    st.success(f"You have returned '{books[book_id - 1]['title']}'.", icon="✅")
                else:
                    st.error("This book is not borrowed.", icon="🚫")
        else:
            st.info("No books available to return.")

    elif choice == "Register User":
        st.subheader("Register a New User")
        username = st.text_input("Enter username")
        
        if st.button("Register"):
            users = load_users()
            if any(user['username'] == username for user in users):
                st.error("Username already exists.", icon="🚫")
            else:
                users.append({'username': username})
                save_users(users)
                st.success(f"User '{username}' registered.", icon="✅")

    elif choice == "View Users":
        st.subheader("Registered Users")
        users = load_users()
        if users:
            for i, user in enumerate(users):
                st.markdown(f"{i + 1}. {user['username']}")
                st.markdown("---")
        else:
            st.info("No users registered.")

if __name__ == "__main__":
    main()
