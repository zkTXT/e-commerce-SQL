import sqlite3

# Connexion à la base de données
connection = sqlite3.connect("e-commerce.db")
cursor = connection.cursor()

# Création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS CLIENT (
    ID_CLIENT INT PRIMARY KEY,
    NOM TEXT,
    PRENOM TEXT,
    LAPTOP TEXT,
    EMAIL TEXT,
    DATE_NAISSANCE DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ADRESS (
    ID_ADRESS INT PRIMARY KEY,
    ID_CLIENT INT,
    ADRESSE TEXT,
    VILLE TEXT,
    CODE_POSTAL TEXT,
    PAYS TEXT,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCT (
    ID_PRODUCT INT PRIMARY KEY,
    NOM TEXT,
    DESCRIPTION TEXT,
    PRIX REAL,
    STOCK INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CART (
    ID_CART INT PRIMARY KEY,
    ID_CLIENT INT,
    DATE_ACHAT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS COMMANDE (
    ID_COMMANDE INT PRIMARY KEY,
    ID_CLIENT INT,
    DATE_COMMANDE DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS commerce_product (
    ID_CART INT,
    ID_PRODUCT INT,
    ID_INVOICE INT,
    ID_COMMANDE INT,
    QUANTITY INT,
    FOREIGN KEY (ID_CART) REFERENCES CART(ID_CART),
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE),
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS INVOICE (
    ID_INVOICE INT PRIMARY KEY,
    ID_COMMANDE INT,
    DATE_FACTURE DATE,
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PHOTO (
    ID_PHOTO INT PRIMARY KEY,
    ID_CLIENT INT,
    ID_PRODUCT INT,
    URL TEXT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PAIMENT (
    ID_PAIMENT INT PRIMARY KEY,
    ID_CLIENT INT,
    ID_INVOICE INT,
    DATE_PAIMENT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS MODE_PAIMENT (
    ID_MODE_PAIMENT INT PRIMARY KEY,
    NOM TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS RATE (
    ID_RATE INT PRIMARY KEY,
    ID_PRODUCT INT,
    RATE INT,
    ID_CLIENT INT,
    MODE_PAIMENT INT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
)
""")

# Insertion des données
clients = [
    (1, 'Chris', 'Paul', '0612345678', 'paul.chris@example.com', '1990-08-20'),
    (2, 'Majid', 'Mohamed', '0623456789', 'mohamed.majid@example.com', '1977-04-08'),
    (3, 'Claire', 'Suzane', '0634567890', 'suzane.claire@example.com', '1994-01-13'),
    (4, 'Jordan', 'Axel', '0645678901', 'axel.jordan@example.com', '1968-11-02'),
    (5, 'Giovanni', 'Lucas', '0656789012', 'lucas.giova@example.com', '1981-01-03'),
]

adresses = [
    (1, 1, '1 Rue de Rivoli', 'Paris', '75000', 'France'),
    (2, 2, '1 Rue de la Paix', 'Paris', '75000', 'France'),
    (3, 3, '1 Avenue Montaigne', 'Paris', '75000', 'France'),
    (4, 4, '1 Rue Victor Hugo', 'Paris', '75000', 'France'),
    (5, 5, '1 Rue Pierre Brossolette', 'Paris', '75000', 'France'),
]

products = [
    (1, 'MacBook Air 13', 'Laptop', 979.0, 10),
    (2, 'Lenovo LOQ 15', 'Laptop', 699.99, 10),
    (3, 'Asus Vivobook 17', 'Laptop', 977.88, 10),
    (4, 'HP 17', 'Laptop', 279.99, 10),
    (5, 'Asus Zenbook 14', 'Laptop', 799.99, 10),
]

carts = [
    (1, 1, '2024-12-20'),
    (2, 2, '2025-01-10'),
    (3, 3, '2025-02-01'),
    (4, 4, '2025-02-15'),
    (5, 5, '2025-03-07'),
]

commandes = [
    (1, 1, '2024-12-20'),
    (2, 2, '2025-01-10'),
    (3, 3, '2025-02-01'),
    (4, 4, '2025-02-15'),
    (5, 5, '2025-03-07'),
]

invoices = [
    (1, 1, '2024-12-20'),
    (2, 2, '2025-01-10'),
    (3, 3, '2025-02-01'),
    (4, 4, '2025-02-15'),
    (5, 5, '2025-03-07'),
]

commerce_products = [
    (1, 3, 1, 1, 4),
    (2, 1, 2, 2, 5),
    (3, 4, 3, 3, 1),
    (4, 5, 4, 4, 2),
    (5, 2, 5, 5, 3),
]

paiments = [
    (1, 1, 1, '2024-12-20'),
    (2, 2, 2, '2025-01-10'),
    (3, 3, 3, '2025-02-01'),
    (4, 4, 4, '2025-02-15'),
    (5, 5, 5, '2025-03-07'),
]

cursor.executemany("INSERT INTO CLIENT VALUES (?, ?, ?, ?, ?, ?)", clients)
cursor.executemany("INSERT INTO ADRESS VALUES (?, ?, ?, ?, ?, ?)", adresses)
cursor.executemany("INSERT INTO PRODUCT VALUES (?, ?, ?, ?, ?)", products)
cursor.executemany("INSERT INTO CART VALUES (?, ?, ?)", carts)
cursor.executemany("INSERT INTO COMMANDE VALUES (?, ?, ?)", commandes)
cursor.executemany("INSERT INTO INVOICE VALUES (?, ?, ?)", invoices)
cursor.executemany("INSERT INTO commerce_product VALUES (?, ?, ?, ?, ?)", commerce_products)
cursor.executemany("INSERT INTO PAIMENT VALUES (?, ?, ?, ?)", paiments)

# Validation des changements
connection.commit()
connection.close()
