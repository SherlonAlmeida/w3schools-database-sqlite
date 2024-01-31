/*----------------------------------------------------------*/
/* Table structure for table categories */

CREATE TABLE IF NOT EXISTS categories (
  CategoryID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  CategoryName VARCHAR(255),
  Description VARCHAR(255)
);

/*----------------------------------------------------------*/
/* Table structure for table customers */

CREATE TABLE IF NOT EXISTS customers (
  CustomerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  CustomerName VARCHAR(255),
  ContactName VARCHAR(255),
  Address VARCHAR(255),
  City VARCHAR(255),
  PostalCode VARCHAR(255),
  Country VARCHAR(255)
);

/*----------------------------------------------------------*/
/* Table structure for table employees */

CREATE TABLE IF NOT EXISTS employees (
  EmployeeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(255),
  FirstName VARCHAR(255),
  BirthDate date,
  Photo VARCHAR(255),
  Notes TEXT(500)
);

/*----------------------------------------------------------*/
/* Table structure for table orders */

CREATE TABLE IF NOT EXISTS orders (
  OrderID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  CustomerID INT,
  EmployeeID INT,
  OrderDate date,
  ShipperID INT,
  FOREIGN KEY (CustomerID) REFERENCES customers (CustomerID),
  FOREIGN KEY (EmployeeID) REFERENCES employees (EmployeeID),
  FOREIGN KEY (ShipperID) REFERENCES shippers (ShipperID)
);

/*----------------------------------------------------------*/
/* Table structure for table orderDetails */

CREATE TABLE IF NOT EXISTS orderDetails (
  OrderDetailID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  OrderID INT,
  ProductID INT,
  Quantity INT,
  FOREIGN KEY (OrderID) REFERENCES orders (OrderID),
  FOREIGN KEY (ProductID) REFERENCES products (ProductID)
);

/*----------------------------------------------------------*/
/* Table structure for table products */

CREATE TABLE IF NOT EXISTS products (
  ProductID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ProductName VARCHAR(255),
  SupplierID INT,
  CategoryID INT,
  Unit VARCHAR(255),
  Price DECIMAL,
  FOREIGN KEY (CategoryID) REFERENCES categories (CategoryID),
  FOREIGN KEY (SupplierID) REFERENCES suppliers (SupplierID)
);

/*----------------------------------------------------------*/
/* Table structure for table shippers */

CREATE TABLE IF NOT EXISTS shippers (
  ShipperID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ShipperName VARCHAR(255),
  Phone VARCHAR(255)
);

/*----------------------------------------------------------*/
/* Table structure for table suppliers */

CREATE TABLE IF NOT EXISTS suppliers (
  SupplierID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  SupplierName VARCHAR(255),
  ContactName VARCHAR(255),
  Address VARCHAR(255),
  City VARCHAR(255),
  PostalCode VARCHAR(255),
  Country VARCHAR(255),
  Phone VARCHAR(255)
);