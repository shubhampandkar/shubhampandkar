import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import messagebox
import sqlite3
from tkinter import BOTH, END, LEFT
from tkinter import ttk
import random
import datetime
from datetime import date


def validateLogin(username, password):
    username = username.get()
    password = password.get()
    global prim
    prim = username
    conn = sqlite3.connect('Newark_IT.db')
    c = conn.cursor()
    q1 = (username, password)
    find = "select * from CUSTOMER where CID=? and password=?"
    c.execute(find, q1)
    result = c.fetchall()
    conn.close()
    if result:
        messagebox.showinfo("Title", "Your login was done successfully")
        screen1 = tk.Toplevel(tkWindow)
        screen1.geometry('400x150')
        screen1.title('SELECTION WINDOW')
        # ONLINE SALE button
        online_sale_button = Button(screen1, text="ONLINE SALE", command=onlinesale).grid(row=4, column=0)
        # Sale Statistics button
        sale_button = Button(screen1, text="SALE STATISTICS", command=salestats).grid(row=4, column=1)

        update_button = Button(screen1, text="UPDATE DETAILS", command=update).grid(row=4, column=2)
    else:
        messagebox.showinfo("Title", "Invalid login id password")
    return


def onlinesale():
    global my_cart

    def my_list():
        my_w = tk.Tk()
        my_w.geometry("1200x500")
        my_w.title("Online Sale")
        global p_name
        global cat1
        total_str = tk.DoubleVar()
        price_str = tk.DoubleVar()
        sb1_str = tk.IntVar()
        b1_p_id = tk.StringVar()
        cat1 = {1: 'Computer', 2: 'Printer'}  # list of categories
        # Using treeview widget
        trv = ttk.Treeview(my_w, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4", "5", "6")
        # Defining heading
        trv['show'] = 'headings'
        # width of columns and alignment
        trv.column("1", width=10, anchor='w')
        trv.column("2", width=10, anchor='w')
        trv.column("3", width=200, anchor='w')
        trv.column("4", width=100, anchor='w')
        trv.column("5", width=15, anchor='w')
        trv.column("6", width=250, anchor='w')
        # respective columns
        trv.heading("1", text="PRODUCTID")
        trv.heading("2", text="PRODUCTNAME")
        trv.heading("3", text="PRODUCTPRICE")
        trv.heading("4", text="PRODUCTTYPE")
        trv.heading("5", text="QUANTITY")
        trv.heading("6", text="DESCRIPTION")

        def display_data():
            conn = sqlite3.connect('Newark_IT.db')
            c = conn.cursor()
            query = "SELECT * from PRODUCT"
            r_set = c.execute(query)

            for dt in r_set:
                trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
            conn.close()

        def update_total():
            total_str.set(int(sb1_str.get()) * int(price_str.get()))

        def update_stock(p_id):
            global num
            num = random.randint(1, 100000)
            conn = sqlite3.connect('Newark_IT.db')
            c = conn.cursor()
            q1 = "INSERT INTO BASKET VALUES (?, ?)"
            var = (num, prim)
            c.execute(q1, var)
            val = (num, p_id, sb1_str.get(), total_str.get())
            print(val)

            query = "INSERT INTO APPEARS_IN VALUES (?, ?, ?, ?)"
            c.execute(query, val)
            # q2 = "INSERT INTO TRANS VALUES (?, ?, ?, ?, ?, ?)"
            # var2 = (num, )
            q4 = "select CCNumber from CREDIT_CARD where CID = ?"
            c.execute(q4, [prim])
            cc = c.fetchall()

            q5 = "select SAName from SHIPPING_ADDRESS where CID = ?"
            c.execute(q5, [prim])
            sn = c.fetchall()

            num1 = random.randint(1, 1000)
            
            today=date.today()
            today1=today.strftime("%B %d, %Y")
           

            q6 = "insert into TRANS values (?,?,?,?,?,?)"
            vals = (num, cc[0][0], prim, sn[0][0], today1, num1)
            
            c.execute(q6, vals)
            conn.commit()
            conn.close()
            messagebox.showinfo("Title", "Order is placed")
            

        def data_show(*args):
            
            p_id = trv.selection()[0]
            conn = sqlite3.connect('Newark_IT.db')
            c = conn.cursor()
            # print(p_id)
            query = 'SELECT * FROM PRODUCT WHERE PRODUCTID=?'
            c.execute(query, [p_id])
            row = c.fetchall()
            # print(row)
            
            l_product.config(text=row[0][2])
            price_str.set(row[0][3])
            b1_p_id.set(row[0][0])
            # print(p_id(row[4]))
            if (row[0][4] > 0):  # if stock is available
                sb1.config(state='normal', to=row[0][4])
                sb1_str.set(1)
                total_str.set(str(row[0][3]))
                b1.config(state='normal')
            else:
                sb1_str.set(1)
                sb1.config(state='disabled')
                total_str.set(0)
                b1.config(state='disabled')

        trv.bind("<<TreeviewSelect>>", data_show)
        font1 = ('Times', 24, 'bold')
        font2_product = ('Times', 18, 'normal')
        font_price = ('Times', 16, 'normal')
        l_product = tk.Label(my_w, text='data ', bg='lightblue', font=font2_product, width=30)
        l_product.grid(row=1, column=2, columnspan=2, padx=20, sticky='w')
        l_price = tk.Label(my_w, text='Price')
        l_price.grid(row=3, column=2, padx=10, pady=10)
        price = tk.Label(my_w, textvariable=price_str, font=font_price)
        price.grid(row=3, column=3, padx=10, pady=10)
        l_stock = tk.Label(my_w, text='Quantity')
        l_stock.grid(row=4, column=2, padx=10, pady=10)
        sb1 = Spinbox(my_w, from_=1, to=10, width=5, font=font1, state='disabled',
                      textvariable=sb1_str, command=lambda: update_total())
        sb1.grid(row=4, column=3, padx=10)
        l_total = tk.Label(my_w, text='Total')
        l_total.grid(row=5, column=2, padx=10, pady=10)
        total = tk.Label(my_w, textvariable=total_str, font=font_price, bg='lightgreen')
        total.grid(row=5, column=3)
        b1 = tk.Button(my_w, text='add to cart and pay'
                       , command=lambda: update_stock(b1_p_id.get()))
        b1.grid(row=6, column=2, columnspan=2)
        b2 = tk.Button(my_w, text='see transactions'
                       , command=lambda: tran_det())
        b2.grid(row=7, column=2, columnspan=2)
        display_data()  # show the top data

    #### show the cart content ####3
    my_list()
def tran_det():
    tra = tk.Toplevel(tkWindow)
    tra.geometry('1200x500')
    tra.title('Transactions')
    trv = ttk.Treeview(tra, selectmode='browse')
    trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
        # number of columns
    trv["columns"] = ("1", "2", "3", "4", "5", "6")
        # Defining heading
    trv['show'] = 'headings'
        # width of columns and alignment
    trv.column("1", width=10, anchor='w')
    trv.column("2", width=10, anchor='w')
    trv.column("3", width=200, anchor='w')
    trv.column("4", width=100, anchor='w')
    trv.column("5", width=15, anchor='w')
    trv.column("6", width=250, anchor='w')
        # respective columns
    trv.heading("1", text="CARTID")
    trv.heading("2", text="CARD NUMBER")
    trv.heading("3", text="USERID")
    trv.heading("4", text="SHIPPING ADDRESS NAME")
    trv.heading("5", text="TRANS DATE")
    trv.heading("6", text="TRANS TAG")
    conn = sqlite3.connect('Newark_IT.db')
    c = conn.cursor()
    query = "SELECT * from TRANS where CID = ?"
    r_set = c.execute(query,[prim])

    for dt in r_set:
        trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
    conn.close()

def salestats():
    sale = tk.Toplevel(tkWindow)
    sale.title('Sale stats')
    option1 = tk.StringVar(sale)
    option1.set("filters")  # default value

    def disp1(option1):
        go1 = partial(go_choice_1, option1)
        go1_button = Button(sale, text="GO", command=go1).grid(row=4, column=0)

    l1 = tk.Label(sale, text='Select One', width=10)
    l1.grid(row=2, column=1)
    fill = ["1", "2", "3", "4", "5"]

    om1 = tk.OptionMenu(sale, option1, *fill, command=disp1)
    om1.grid(row=2, column=2)


def update():
    global up
    up = tk.Toplevel(tkWindow)
    up.title('USER INFO UPDATE')
    option2 = tk.StringVar(up)
    option2.set("Details")  # default value

    def disp2(option2):
        go2 = go_choice2(option2)
        go2_button = Button(up, text="GO", command=go2).grid(row=4, column=0)

    l1 = tk.Label(up, text='Select One', width=10)
    l1.grid(row=2, column=1)
    det = ["password", "First name", "Last name", "email", "phone", "Card number", "Sec Number", "Owner name",
           "Card type", "billing address", "shipping address name", "Recipient name", "Shipping address number",
           "Street", "City", "Country", "State", "Zip"]

    om1 = tk.OptionMenu(up, option2, *det, command=disp2)
    om1.grid(row=2, column=2)


def go_choice_1(choice):
    global fil
    fil = tk.Toplevel(tkWindow)
    fil.geometry('400x150')
    fil.title('Filter')
    fromdataLabel = Label(fil, text="fromdate").grid(row=0, column=0)
    fromdate = StringVar()
    usernameEntry = Entry(fil, textvariable=fromdate).grid(row=0, column=1)

    todateLabel = Label(fil, text="todate").grid(row=1, column=0)
    todate = StringVar()
    todateEntry = Entry(fil, textvariable=todate).grid(row=1, column=1)
    search1 = partial(search_1, choice, fromdate, todate)
    Search_button = Button(fil, text="Search", command=search1).grid(row=2, column=0)


def search_1(choice, fromdate, todate):
    fromdate = fromdate.get()
    todate = todate.get()
    if choice == "1":
        s1 = tk.Toplevel(tkWindow)
        s1.geometry('1200x500')
        s1.title('Transactions')
        trv = ttk.Treeview(s1, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
            # number of columns
        trv["columns"] = ("1", "2")
            # Defining heading
        trv['show'] = 'headings'
            # width of columns and alignment
        trv.column("1", width=100, anchor='w')
        trv.column("2", width=100, anchor='w')
        
            # respective columns
        trv.heading("1", text="PRODUCTID")
        trv.heading("2", text="COUNT")
        
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        valu = (fromdate, todate)
        query = "select PRODUCTID, COUNT(Quantity) from APPEARS_IN INNER JOIN TRANS WHERE CARTID = BID AND TDATE BETWEEN ? AND ? GROUP BY PRODUCTID ORDER BY COUNT(Quantity) DESC"
     
        c.execute(query,valu)
        r_set = c.fetchall()
        

        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1]))
        conn.close()
   
    elif choice == "2":
        s1 = tk.Toplevel(tkWindow)
        s1.geometry('1200x500')
        s1.title('Transactions')
        trv = ttk.Treeview(s1, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
            # number of columns
        trv["columns"] = ("1", "2")
            # Defining heading
        trv['show'] = 'headings'
            # width of columns and alignment
        trv.column("1", width=100, anchor='w')
        trv.column("2", width=100, anchor='w')
        
            # respective columns
        trv.heading("1", text="PRODUCTID")
        trv.heading("2", text="COUNT")
        
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        valu = (fromdate, todate)
        query = "select PRODUCTID, COUNT(DISTINCT(CID)) from APPEARS_IN INNER JOIN TRANS WHERE CARTID = BID AND TDATE BETWEEN ? AND ? GROUP BY PRODUCTID ORDER BY COUNT(DISTINCT(CID)) DESC"
     
        c.execute(query,valu)
        r_set = c.fetchall()
        

        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1]))
        conn.close()
    elif choice == "3":
        s1 = tk.Toplevel(tkWindow)
        s1.geometry('1200x500')
        s1.title('Transactions')
        trv = ttk.Treeview(s1, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
            # number of columns
        trv["columns"] = ("1", "2")
            # Defining heading
        trv['show'] = 'headings'
            # width of columns and alignment
        trv.column("1", width=100, anchor='w')
        trv.column("2", width=100, anchor='w')
        
            # respective columns
        trv.heading("1", text="CUSTOMER ID")
        trv.heading("2", text="SUM OF MONEY SPENT")
        
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        valu = (fromdate, todate)
        query = "select CID, SUM(PriceSold) from APPEARS_IN INNER JOIN TRANS WHERE CARTID = BID AND TDATE BETWEEN ? AND ? GROUP BY CID ORDER BY SUM(PriceSold) DESC"
     
        c.execute(query,valu)
        r_set = c.fetchall()
        

        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1]))
        conn.close()
    elif choice == "4":
        s1 = tk.Toplevel(tkWindow)
        s1.geometry('1200x500')
        s1.title('Transactions')
        trv = ttk.Treeview(s1, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
            # number of columns
        trv["columns"] = ("1", "2")
            # Defining heading
        trv['show'] = 'headings'
            # width of columns and alignment
        trv.column("1", width=100, anchor='w')
        trv.column("2", width=100, anchor='w')
        
            # respective columns
        trv.heading("1", text="Credit Card Number")
        trv.heading("2", text="Max Basket Total")
        
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        valu = (fromdate, todate)
        query = "select CCNumber, MAX(PriceSold) from APPEARS_IN INNER JOIN TRANS WHERE CARTID = BID AND TDATE BETWEEN ? AND ? GROUP BY CCNumber"
     
        c.execute(query,valu)
        r_set = c.fetchall()
        

        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1]))
        conn.close()
    elif choice == "5":
        s1 = tk.Toplevel(tkWindow)
        s1.geometry('1200x500')
        s1.title('Transactions')
        trv = ttk.Treeview(s1, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20, rowspan=10)
            # number of columns
        trv["columns"] = ("1", "2")
            # Defining heading
        trv['show'] = 'headings'
            # width of columns and alignment
        trv.column("1", width=100, anchor='w')
        trv.column("2", width=100, anchor='w')
        
            # respective columns
        trv.heading("1", text="PRODUCT TYPE")
        trv.heading("2", text="AVG PRICE SOLD")
        
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        valu = (fromdate, todate)
        
        query = "select PType, AVG(PriceSold) from APPEARS_IN NATURAL JOIN PRODUCT WHERE NOT EXISTS (SELECT * FROM TRANS WHERE TDATE BETWEEN ? AND ?) GROUP BY PTYPE"
     
        c.execute(query,valu)
        r_set = c.fetchall()
        

        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1]))
        conn.close()
    else:
        pass


def go_choice2(choice):
    up_win = tk.Toplevel(up)
    up_win.geometry('400x150')
    up_win.title('Update')
    if choice == "password":
        temp = 1
        passwordLabel = Label(up_win, text="Password").grid(row=0, column=0)
        password = StringVar()
        passwordEntry = Entry(up_win, textvariable=password, show='*').grid(row=1, column=1)
        go3 = partial(go_choice3, password, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "First name":
        temp = 2
        FnameLabel = Label(up_win, text="First Name").grid(row=0, column=0)
        Fname = StringVar()
        FnameEntry = Entry(up_win, textvariable=Fname).grid(row=0, column=1)
        go3 = partial(go_choice3, Fname, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Last name":
        temp = 3
        LnameLabel = Label(up_win, text="Last Name").grid(row=0, column=0)
        Lname = StringVar()
        LnameEntry = Entry(up_win, textvariable=Lname).grid(row=0, column=1)
        go3 = partial(go_choice3, Lname, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "email":
        temp = 4
        emailLabel = Label(up_win, text="email").grid(row=0, column=0)
        email = StringVar()
        emailEntry = Entry(up_win, textvariable=email).grid(row=0, column=1)
        go3 = partial(go_choice3, email, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "phone":
        temp = 5
        phoneLabel = Label(up_win, text="phone").grid(row=0, column=0)
        phone = StringVar()
        phoneEntry = Entry(up_win, textvariable=phone).grid(row=0, column=1)
        go3 = partial(go_choice3, phone, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Card number":
        temp = 6
        CnumLabel = Label(up_win, text="Credit card number").grid(row=0, column=0)
        Cnum = IntVar()
        CnumEntry = Entry(up_win, textvariable=Cnum).grid(row=0, column=1)
        go3 = partial(go_choice3, Cnum, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Sec Number":
        temp = 7
        SnumLabel = Label(up_win, text="sec").grid(row=0, column=0)
        Snum = IntVar()
        SnumEntry = Entry(up_win, textvariable=Snum).grid(row=0, column=1)
        go3 = partial(go_choice3, Snum, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Owner name":
        temp = 8
        OnameLabel = Label(up_win, text="Owner Name").grid(row=0, column=0)
        Oname = StringVar()
        OnameEntry = Entry(up_win, textvariable=Oname).grid(row=0, column=1)
        go3 = partial(go_choice3, Oname, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Card type":
        temp = 9
        CtypeLabel = Label(up_win, text="Card type").grid(row=0, column=0)
        Ctype = StringVar()
        CtypeEntry = Entry(up_win, textvariable=Ctype).grid(row=0, column=1)
        go3 = partial(go_choice3, Ctype, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "billing address":
        temp = 10
        BAddress = Label(up_win, text="Billing Address").grid(row=0, column=0)
        BAddress = StringVar()
        BAddressEntry = Entry(up_win, textvariable=BAddress).grid(row=0, column=1)
        go3 = partial(go_choice3, BAddress, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "shipping address name":
        temp = 11
        Sname = Label(up_win, text="Shipping Address name").grid(row=0, column=0)
        Sname = StringVar()
        SnameEntry = Entry(up_win, textvariable=Sname).grid(row=0, column=1)
        go3 = partial(go_choice3, Sname, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Recipient name":
        temp = 12
        RnameLabel = Label(up_win, text="Recepient Name").grid(row=0, column=0)
        Rname = StringVar()
        RnameEntry = Entry(up_win, textvariable=Rname).grid(row=0, column=1)
        go3 = partial(go_choice3, Rname, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Shipping address number":
        temp = 13
        SanumLabel = Label(up_win, text="Address number").grid(row=0, column=0)
        Sanum = IntVar()
        SanumEntry = Entry(up_win, textvariable=Sanum).grid(row=0, column=1)
        go3 = partial(go_choice3, Sanum, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Street":
        temp = 14
        Street = Label(up_win, text="Street name").grid(row=0, column=0)
        Street = StringVar()
        StreetEntry = Entry(up_win, textvariable=Street).grid(row=0, column=1)
        go3 = partial(go_choice3, Street, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "City":
        temp = 15
        City = Label(up_win, text="City").grid(row=0, column=0)
        City = StringVar()
        CityEntry = Entry(up_win, textvariable=City).grid(row=0, column=1)
        go3 = partial(go_choice3, City, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Country":
        temp = 16
        Country = Label(up_win, text="Country").grid(row=0, column=0)
        Country = StringVar()
        CountryEntry = Entry(up_win, textvariable=Country).grid(row=0, column=1)
        go3 = partial(go_choice3, Country, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "State":
        temp = 17
        State = Label(up_win, text="State").grid(row=0, column=0)
        State = StringVar()
        StateEntry = Entry(up_win, textvariable=State).grid(row=0, column=1)
        go3 = partial(go_choice3, State, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    elif choice == "Zip":
        temp = 18
        Zip = Label(up_win, text="Zip Code").grid(row=0, column=0)
        Zip = IntVar()
        ZipEntry = Entry(up_win, textvariable=Zip).grid(row=0, column=1)
        go3 = partial(go_choice3, Zip, temp)
        go3_button = Button(up_win, text="GO", command=go3).grid(row=2, column=0)

    else:
        messagebox.showinfo("Title", "Some error occurred")


def go_choice3(new, temp):
    if temp == 1:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CUSTOMER SET password = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Password Updated")
    elif temp == 2:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CUSTOMER SET FName = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "FIRST NAME Updated")
    elif temp == 3:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CUSTOMER SET LName = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "LAST NAME Updated")
    elif temp == 4:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CUSTOMER SET Email = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "EMAIL Updated")
    elif temp == 5:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CUSTOMER SET Phone = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "PHONE Updated")
    elif temp == 6:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE TOP (1) CREDIT_CARD SET CCNumber = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Credit card number Updated")
    elif temp == 7:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CREDIT_CARD SET SecNumber = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "SEC NUMBER Updated")
    elif temp == 8:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CREDIT_CARD SET OwnerName = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Owner name Updated")
    elif temp == 9:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CREDIT_CARD SET CCType = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Card Type Updated")
    elif temp == 10:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE CREDIT_CARD SET BilAddress = ? where CID = ?"
        c.execute(upd1, n1)
        upd2 = "UPDATE CUSTOMER SET Address = ? where CID = ?"
        c.execute(upd2, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Billing address Updated")
    elif temp == 11:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET SAName = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "shipping address name Updated")
    elif temp == 12:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET RecipientName = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Recipient name Updated")
    elif temp == 13:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET SNumber = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Shipping address number Updated")
    elif temp == 14:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET Street = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Street Updated")
    elif temp == 15:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET City = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "City Updated")
    elif temp == 16:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET Country = ? where CID = ? "
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Country Updated")
    elif temp == 17:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET State = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "State Updated")
    elif temp == 18:
        x1 = new.get()
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        n1 = (x1, prim)
        upd1 = "UPDATE SHIPPING_ADDRESS SET Zip = ? where CID = ?"
        c.execute(upd1, n1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Zip Updated")
    else:
        pass


def validateRegister(username, password, Fname, Lname, email, phone, Cnum, Snum, Oname, Ctype, Expdate,
                     BAddress, Sname, Rname, Sanum, Street, City, State, Country, Zip):
    username = username.get()
    password = password.get()
    Fname = Fname.get()
    Lname = Lname.get()
    email = email.get()
    phone = phone.get()
    Cnum = Cnum.get()
    Snum = Snum.get()
    Oname = Oname.get()
    Ctype = Ctype.get()
    Expdate = Expdate.get()
    BAddress = BAddress.get()
    Sname = Sname.get()
    Rname = Rname.get()
    Sanum = Sanum.get()
    Street = Street.get()
    City = City.get()
    State = State.get()
    Country = Country.get()
    Zip = Zip.get()

    global username1
    global password1
    global Fname1
    global Lname1
    global email1
    global phone1
    global Cnum1
    global Snum1
    global Oname1
    global Ctype1
    global BAddress1
    global Sname1
    global Rname1
    global Sanum1
    global Street1
    global City1
    global State1
    global Country1
    global Zip1

    username1 = username
    password1 = password
    Fname1 = Fname
    Lname1 = Lname
    email1 = email
    phone1 = phone
    Cnum1 = Cnum
    Snum1 = Snum
    Oname1 = Oname
    Ctype1 = Ctype
    BAddress1 = BAddress
    Sname1 = Sname
    Rname1 = Rname
    Sanum1 = Sanum
    Street1 = Street
    City1 = City
    State1 = State
    Country1 = Country
    Zip1 = Zip
    if username == "":
        messagebox.showinfo("Title", "Please Enter username Name")
    elif password == "":
        messagebox.showinfo("Title", "Please Enter Password")
    elif Fname == "":
        messagebox.showinfo("Title", "Please Enter First Name")
    elif Lname == "":
        messagebox.showinfo("Title", "Please Enter Last Name")
    elif email == "":
        messagebox.showinfo("Title", "Please Enter Email id")
    elif phone == 0:
        messagebox.showinfo("Title", "Please Enter Phone Number")
    elif Cnum == 0:
        messagebox.showinfo("Title", "Please Enter Card Number")
    elif Snum == 0:
        messagebox.showinfo("Title", "Please Enter Sec Number")
    elif Oname == "":
        messagebox.showinfo("Title", "Please Enter Owner Name")
    elif Ctype == "":
        messagebox.showinfo("Title", "Please Enter Card Type")
    elif Expdate == "":
        messagebox.showinfo("Title", "Please Enter Expiration Date")
    elif BAddress == "":
        messagebox.showinfo("Title", "Please Enter Billing Address")
    elif Sname == "":
        messagebox.showinfo("Title", "Please Enter Shipping Address Name")
    elif Rname == "":
        messagebox.showinfo("Title", "Please Enter Recipient Name")
    elif Sanum == "":
        messagebox.showinfo("Title", "Please Enter Shipping Address Number")
    elif Street == "":
        messagebox.showinfo("Title", "Please Enter Street")
    elif City == "":
        messagebox.showinfo("Title", "Please Enter City")
    elif State == "":
        messagebox.showinfo("Title", "Please Enter State")
    elif Country == "":
        messagebox.showinfo("Title", "Please Enter Country")
    elif Zip == "":
        messagebox.showinfo("Title", "Please Enter Zip Code")
    else:
        conn = sqlite3.connect('Newark_IT.db')
        c = conn.cursor()
        d1 = (username, Fname, Lname, email, BAddress, phone, password)
        save = "insert into CUSTOMER values (?,?,?,?,?,?,?)"
        c.execute(save, d1)
        conn.commit()
        d2 = (Cnum, Snum, Oname, Ctype, BAddress, Expdate, username)
        save1 = "insert into CREDIT_CARD values (?,?,?,?,?,?,?)"
        c.execute(save1, d2)
        conn.commit()
        d3 = (username, Sname, Rname, Street, Sanum, City, Zip, State, Country)
        save2 = "insert into SHIPPING_ADDRESS values (?,?,?,?,?,?,?,?,?)"
        c.execute(save2, d3)
        conn.commit()
        num = random.randint(1, 100000)
        d4 = (num, username)
        save3 = "insert into BASKET values (?,?)"
        c.execute(save3, d4)
        conn.commit()
        conn.close()

        messagebox.showinfo("Title", "Registered Successfully")
        screen.destroy()

    return


def RegisterPage():
    global screen
    screen = tk.Toplevel(tkWindow)
    screen.geometry('1000x500')
    screen.title('Register')

    # username label and text entry box
    usernameLabel = Label(screen, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(screen, textvariable=username).grid(row=0, column=1)

    # password label and password entry box
    passwordLabel = Label(screen, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(screen, textvariable=password, show='*').grid(row=1, column=1)

    # first name
    FnameLabel = Label(screen, text="First Name").grid(row=2, column=0)
    Fname = StringVar()
    FnameEntry = Entry(screen, textvariable=Fname).grid(row=2, column=1)

    # last name
    LnameLabel = Label(screen, text="Last Name").grid(row=2, column=2)
    Lname = StringVar()
    LnameEntry = Entry(screen, textvariable=Lname).grid(row=2, column=3)

    # email
    emailLabel = Label(screen, text="email").grid(row=3, column=0)
    email = StringVar()
    emailEntry = Entry(screen, textvariable=email).grid(row=3, column=1)

    # phone
    phoneLabel = Label(screen, text="phone").grid(row=4, column=0)
    phone = StringVar()
    phoneEntry = Entry(screen, textvariable=phone).grid(row=4, column=1)

    # credit card label and credit card entry box
    CnumLabel = Label(screen, text="Credit card number").grid(row=5, column=0)
    Cnum = IntVar()
    CnumEntry = Entry(screen, textvariable=Cnum).grid(row=5, column=1)

    SnumLabel = Label(screen, text="sec").grid(row=6, column=0)
    Snum = IntVar()
    SnumEntry = Entry(screen, textvariable=Snum).grid(row=6, column=1)

    OnameLabel = Label(screen, text="Owner Name").grid(row=6, column=2)
    Oname = StringVar()
    OnameEntry = Entry(screen, textvariable=Oname).grid(row=6, column=3)

    CtypeLabel = Label(screen, text="Card type").grid(row=7, column=0)
    Ctype = StringVar()
    CtypeEntry = Entry(screen, textvariable=Ctype).grid(row=7, column=1)

    ExpdateLabel = Label(screen, text="Expiration Date").grid(row=7, column=2)
    Expdate = StringVar()
    ExpdateEntry = Entry(screen, textvariable=Expdate).grid(row=7, column=3)

    BAddress = Label(screen, text="Billing Address").grid(row=8, column=0)
    BAddress = StringVar()
    BAddressEntry = Entry(screen, textvariable=BAddress).grid(row=8, column=1)

    # shipping address label and shipping address entry box
    SAddress = Label(screen, text="Shipping Address").grid(row=9, column=0)
    Sname = Label(screen, text="Shipping Address name").grid(row=10, column=0)
    Sname = StringVar()
    SnameEntry = Entry(screen, textvariable=Sname).grid(row=10, column=1)
    RnameLabel = Label(screen, text="Recepient Name").grid(row=10, column=2)
    Rname = StringVar()
    RnameEntry = Entry(screen, textvariable=Rname).grid(row=10, column=3)
    SanumLabel = Label(screen, text="Address number").grid(row=10, column=4)
    Sanum = IntVar()
    SanumEntry = Entry(screen, textvariable=Sanum).grid(row=10, column=5)
    Street = Label(screen, text="Street name").grid(row=11, column=0)
    Street = StringVar()
    StreetEntry = Entry(screen, textvariable=Street).grid(row=11, column=1)
    City = Label(screen, text="City").grid(row=11, column=2)
    City = StringVar()
    CityEntry = Entry(screen, textvariable=City).grid(row=11, column=3)
    State = Label(screen, text="State").grid(row=11, column=4)
    State = StringVar()
    StateEntry = Entry(screen, textvariable=State).grid(row=11, column=5)
    Country = Label(screen, text="Country").grid(row=12, column=0)
    Country = StringVar()
    CountryEntry = Entry(screen, textvariable=Country).grid(row=12, column=1)
    Zip = Label(screen, text="Zip Code").grid(row=12, column=2)
    Zip = StringVar()
    ZipEntry = Entry(screen, textvariable=Zip).grid(row=12, column=3)

    validateregister = partial(validateRegister, username, password, Fname, Lname, email, phone, Cnum, Snum, Oname,
                               Ctype, Expdate, BAddress, Sname, Rname, Sanum, Street, City, State, Country,
                               Zip)
    register_button = Button(screen, text="Register", command=validateregister).grid(row=13, column=3)


def main_screen():
    # window
    conn = sqlite3.connect('Newark_IT.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS CUSTOMER "
              "(CID VARCHAR(20) PRIMARY KEY,FName VARCHAR(20) NOT NULL, "
              "LName VARCHAR(20) NOT NULL, Email VARCHAR(20) NOT NULL, Address VARCHAR(50) NOT NULL, "
              "Phone VARCHAR(15) NOT NULL, Password VARCHAR(20) NOT NULL)")

    c.execute("CREATE TABLE IF NOT EXISTS CREDIT_CARD "
              "(CCNumber VARCHAR(16) PRIMARY KEY, SecNumber VARCHAR(4) NOT NULL, "
              "OwnerName VARCHAR(20) NOT NULL, CCType VARCHAR(10) NOT NUll, BilAddress VARCHAR(50), "
              "ExpDate CHAR(6) NOT NULL, CID VARCHAR(20) REFERENCES CUSTOMER(CID))")

    c.execute("CREATE TABLE IF NOT EXISTS SHIPPING_ADDRESS "
              "(CID VARCHAR(20) REFERENCES CUSTOMER(CID), SAName VARCHAR(20), "
              "RecipientName VARCHAR(20) NOT NULL, Street VARCHAR(10) NOT NULL, SNumber VARCHAR(5), "
              "City VARCHAR(10) NOT NULL, Zip VARCHAR(5), State VARCHAR(10), Country VARCHAR(20) NOT NULL, "
              "PRIMARY KEY(CID,SAName))")

    c.execute("CREATE TABLE IF NOT EXISTS BASKET "
              "(CARTID VARCHAR(10) PRIMARY KEY,CID VARCHAR(10) REFERENCES CUSTOMER(CID) NOT NULL)")

    c.execute("CREATE TABLE IF NOT EXISTS APPEARS_IN "
              "(CARTID VARCHAR(10) REFERENCES BASKET(CARTID), PRODUCTID VARCHAR(10), Quantity INTEGER(5) NOT NULL,  "
              "PriceSold DOUBLE(10) NOT NULL, PRIMARY KEY (CARTID, PRODUCTID))")

    c.execute("CREATE TABLE IF NOT EXISTS PRODUCT "
              "(PRODUCTID VARCHAR(10) PRIMARY KEY, PType VARCHAR(10),"
              "PName VARCHAR(20), PPrice DOUBLE(10) NOT NULL, Quantity INTEGER(5), Description VARCHAR(10))")

    c.execute("CREATE TABLE IF NOT EXISTS SILVER_AND_ABOVE "
              "(CID VARCHAR(10) PRIMARY KEY REFERENCES CUSTOMER(CID), CreditLine DOUBLE(10))")

    c.execute("CREATE TABLE IF NOT EXISTS TRANS "
              "(BID VARCHAR(10) REFERENCES BASKET(BID), CCNumber VARCHAR(20) REFERENCES CREDIT_CARD(CCNumber), "
              "CID VARCHAR(10), SAName VARCHAR(10), TDate DATETIME(20) NOT NULL, TTag VARCHAR(10), "
              "PRIMARY KEY (BID, CCNumber, CID, SAName), "
              "FOREIGN KEY (CID, SAName) REFERENCES SHIPPING_ADDRESS(CID, SAName))")

    c.execute("CREATE TABLE IF NOT EXISTS OFFER_PRODUCT "
              "(PID VARCHAR(10) PRIMARY KEY, OfferPrice DOUBLE(10))")

    c.execute("CREATE TABLE IF NOT EXISTS PRINTER "
              "(PID VARCHAR(10) PRIMARY KEY REFERENCES PRODUCT(PID), "
              "PrinterType VARCHAR(10), Resolution VARCHAR(10))")

    c.execute("CREATE TABLE IF NOT EXISTS COMPUTER "
              "(PID VARCHAR(10) PRIMARY KEY REFERENCES PRODUCT(PID), CPUType VARCHAR(10))")

    c.execute("CREATE TABLE IF NOT EXISTS LAPTOP "
              "(PID VARCHAR(10) PRIMARY KEY REFERENCES COMPUTER(PID), BType VARCHAR(10), WEIGHT DOUBLE(10))")

    c.execute("INSERT OR IGNORE INTO CREDIT_CARD VALUES "
              "('234193784293784', '123', 'jack', 'visa', '123', '032024', 'john1')")

    c.execute("INSERT OR IGNORE INTO PRODUCT VALUES "
              "('2432424', 'COMPUTER', 'pc1', 400.00, 5, 'hp')")

    c.execute("INSERT OR IGNORE INTO PRODUCT VALUES "
              "('242624', 'COMPUTER', 'pc2', 500.00, 7, 'dell')")

    c.execute("INSERT OR IGNORE INTO PRODUCT VALUES "
              "('54532442', 'PRINTER', 'printer1', 300.00, 10, 'canon')")

    c.execute("INSERT OR IGNORE INTO COMPUTER VALUES "
              "('2432424', 'sda')")

    c.execute("INSERT OR IGNORE INTO PRINTER VALUES "
              "('54532442', 'inkjet', '2400x3200')")

    c.execute("INSERT OR IGNORE INTO LAPTOP VALUES "
              "('242624', 'sfdsd', 130.5)")

    conn.commit()
    conn.close()

    global tkWindow
    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Login')

    # username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

    validatelogin = partial(validateLogin, username, password)
    # login button
    login_button = Button(tkWindow, text="Login", command=validatelogin).grid(row=4, column=0)
    # Register button
    register_button = Button(tkWindow, text="Register", command=RegisterPage).grid(row=4, column=1)

    tkWindow.mainloop()


main_screen()
