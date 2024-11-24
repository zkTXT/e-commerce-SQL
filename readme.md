# Database Schema Documentation

## Warning ⚠️  
The script must be executed on an **empty database** to avoid conflicts.

---

## Table Creation Scripts

```sql
-- CLIENT Table
-- Stores client details, including their name, laptop, email, and date of birth.
CREATE TABLE CLIENT (
    ID_CLIENT INT PRIMARY KEY,
    NOM TEXT,
    PRENOM TEXT,
    LAPTOP TEXT,
    EMAIL TEXT,
    DATE_NAISSANCE DATE
);

-- ADRESS Table
-- Stores address information linked to clients.
CREATE TABLE ADRESS (
    ID_ADRESS INT PRIMARY KEY,
    ID_CLIENT INT,
    ADRESSE TEXT,
    VILLE TEXT,
    CODE_POSTAL TEXT,
    PAYS TEXT,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);

-- PRODUCT Table
-- Stores product information, including name, description, price, and stock.
CREATE TABLE PRODUCT (
    ID_PRODUCT INT PRIMARY KEY,
    NOM TEXT,
    DESCRIPTION TEXT,
    PRIX REAL,
    STOCK INT
);

-- CART Table
-- Represents a client's shopping cart and links it to the client.
CREATE TABLE CART (
    ID_CART INT PRIMARY KEY,
    ID_CLIENT INT,
    DATE_ACHAT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);

-- COMMANDE Table
-- Represents orders placed by clients and links them to the client.
CREATE TABLE COMMANDE (
    ID_COMMANDE INT PRIMARY KEY,
    ID_CLIENT INT,
    DATE_COMMANDE DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);

-- commerce_product Table
-- Links products, carts, orders, and invoices. This table is used for tracking which products are included in which carts or orders.
CREATE TABLE commerce_product (
    ID_CART INT,
    ID_PRODUCT INT,
    ID_INVOICE INT,
    ID_COMMANDE INT,
    QUANTITY INT,
    FOREIGN KEY (ID_CART) REFERENCES CART(ID_CART),
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT),
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE)
);

-- INVOICE Table
-- Represents invoices linked to orders.
CREATE TABLE INVOICE (
    ID_INVOICE INT PRIMARY KEY,
    ID_COMMANDE INT,
    DATE_FACTURE DATE,
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE)
);

-- PHOTO Table
-- Stores photos linked to clients or products.
CREATE TABLE PHOTO (
    ID_PHOTO INT PRIMARY KEY,
    ID_CLIENT INT,
    ID_PRODUCT INT,
    URL TEXT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
);

-- PAIMENT Table
-- Records payment transactions and links them to clients and invoices.
CREATE TABLE PAIMENT (
    ID_PAIMENT INT PRIMARY KEY,
    ID_CLIENT INT,
    ID_INVOICE INT,
    DATE_PAIMENT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE)
);

-- MODE_PAIMENT Table
-- Stores different payment methods available.
CREATE TABLE MODE_PAIMENT (
    ID_MODE_PAIMENT INT PRIMARY KEY,
    NOM TEXT
);

-- RATE Table
-- Stores product ratings provided by clients.
CREATE TABLE RATE (
    ID_RATE INT PRIMARY KEY,
    ID_PRODUCT INT,
    RATE INT,
    ID_CLIENT INT,
    MODE_PAIMENT INT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
);
