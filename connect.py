import mysql.connector as mysql
#functions
def insert():
    c=mysql.connect(host="localhost",user="root",passwd="",database="shop",charset="utf8")
    cu=c.cursor()
    
    x=int(input("enter the P_id"))
    y=input("enter the name of product")
    z=int(input("enter the price"))
    a=int(input("enter the quantity"))
    
    st="INSERT INTO ITEMS(p_id,p_name,p_price,p_qt)VALUES({},'{}',{},{})".format(x,y,z,a)
    cu.execute(st)
    c.commit()
def show():
    c=mysql.connect(host="localhost",user="root",passwd="",database="shop",charset="utf8")
    cu=c.cursor()
    st="SELECT * FROM ITEMS"
    cu.execute(st)
    q=cu.fetchall()
    for i in q:
        print(i)
def search():
    c=mysql.connect(host="localhost",user="root",passwd="",database="shop",charset="utf8")
    cu=c.cursor()
    u=input("enter the name of product")
    st="SELECT * FROM ITEMS WHERE p_name LIKE '{}'".format(u)
    cu.execute(st)
    q=cu.fetchall()
    for i in q:
        print(i)



def update():
    c=mysql.connect(host="localhost",user="root",passwd="",database="shop",charset="utf8")
    cu=c.cursor()
    u=int(input("enter the P_id"))
    l=int(input("enter the new price"))
    st="UPDATE ITEMS SET p_price={} WHERE p_id={}".format(l,u)
    cu.execute(st)
    c.commit()


#main
c=1
while c==1:
    print("To insert new record :Press :1")
    print("To show the data:Press: 2")
    print("To search data by  product name:Press:3")
    print("To update the product name :Press:4")
    s=int(input("enter the choice:"))
    if s==1:
        insert()
    elif s==2:
        show()
    elif s==3:
        search()
    elif s==4:
        update()
    else:
        print("Invalid Choice")
    c=int(input("Press 1 for more and 0 to stop"))
c.close()
