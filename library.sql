-- Add User and Book Info

INSERT INTO users (name, email)
VALUES ('Alice Smith', 'alice.smith@gmail.com'), 
('Bob Johnson', 'bob.johnson@gmail.com.com'),
('Charlie Brown', 'charlie.brown@gamil.com'),
('David Lee', 'david.lee@gmail.com'),
('Emma Davis', 'emma.davis@gmail.com'),
('Jack Harris', 'jack.harris@gmail.com');


INSERT INTO books (title, isbn, publication_date, availability)
VALUES ('The Great Gatsby', '9780743273565', '2004-09-30', '1'),
('To Kill a Mockingbird', '9780061120084', '2006-10-11', '1'),
('1984', '9780451524935', '1950-07-01', '1'),
('Pride and Prejudice', '9780486284736', '1995-08-01', '1'),
('Harry Potter and the Sorcerers Stone', '9780590353427', '1998-09-08', '1'),
('The Catcher in the Rye', '9780316769488', '2001-05-01', '1');