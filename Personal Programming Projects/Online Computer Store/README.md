# The Online Computer Store

## GOAL: 

Implement The Online Computer Store. The android application is implemented using Python, SQLite3 as a backend in order to interact with the database 
and Python tkinter at the frontend (UI). All the functions that are included in the application are as mentioned  

•	Users can login with store by providing the  username and password.
•	The user can sign-up with user’s personal information, credit card details and shipping address.
•	Users can link credit card with their account. The account has a card number, a security  number,  
  the name of its owner, the billing address, the type  of  credit  card, and an expiry date.
•	Basic validation criteria were implemented on registration process.
•	A customer can specify shipping address and are identified by the name the customer choses for the 
  address (which is unique among the shipping addresses of this customer) and the ID of the customer. 
  For a shipping address the zip code, street name, street number, city, state and country are provided. 
  If a customer is deleted, we need not keep track of her shipping addresses any longer.
•	Each product has its own product ID, a name, a recommended price, and a brief textual description. 
  It also has a unique product type. The quantity of each product in stock is recorded in the database.
•	A shopping basket is always non-empty. It is created with the first item added.
•	A successful sales transaction is recorded in the database, a customer buys a shopping basket (with products). 
  The price and the quantity of every product in the transaction is available as well as the total amount of the transaction. 
•	There are three main categories of product types: Desktop, laptops, and printers. 

## IMPLEMENTATION: 
This application satisfies all the needs of a typical online computer store which helps all the people involved in manual purchasing of the computers. 
The online computer store database application has been made to provide the admin and users with better facilities to perform the functionalities 
mentioned in the goals of the project. The main purpose of this is to provide easy and convenient access to the users to add a product to cart and 
purchase it using credit card to a specific shipping address. The registration information can be edited by the user. 
The user can also view their transactions history.
 
The admin can generate statistics to analyse its sales and customers. He can generate five types of statistical data based on transaction date range: 
1)	Most frequently sold products
2)	Products sold to highest number of distinct customers 
3)	Ten best customers in terms of most money spent 
4)	Maximum basket total per credit card
5)	Average sold product price per product type.

Started process with creating the sql queries in Sqlite3, we first created all the tables without any constraints and determining the primary key 
and foreign keys. Then we inserted random data, making sure that the inserts are successful.  
Created the front end with Python Tkinter, by creating a simple looking screen for Registration, login page, Main Menu, Online Sale, 
Sale Statistics and Update user information.  
After doing the major work, we connected the front UI with the backend of Sqlite3, so that all the data can be easily accessed by the end user. 
So, while clicking any button or link it will fetch the details in the backend (DB) and after processing it will display the result to the user. 

![alt text](https://github.com/shubhampandkar/online_store_DBMS_UI/blob/main/images/registration.png "Registration")

![alt text](https://github.com/shubhampandkar/online_store_DBMS_UI/blob/main/images/login.png "Login")

![alt text](https://github.com/shubhampandkar/online_store_DBMS_UI/blob/main/images/main_screen.png "Main Screen")

![alt text](https://github.com/shubhampandkar/online_store_DBMS_UI/blob/main/images/online_Sale.png "Online Sale")

![alt text](https://github.com/shubhampandkar/online_store_DBMS_UI/blob/main/images/sale_stats.png "Sale Statistics")

![alt text](https://github.com/shubhampandkar/online_store_DBMS_UI/blob/main/images/Update_user_Details.png "Update User Details")

