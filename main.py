
def sign_up():
    import sqlite3
    import datetime
    con = sqlite3.connect('C:/Users/sadaf/Desktop/project/bank.db')
    c = con.cursor()
    num = 0
    newaccount_num = 9000 + num
    num += 1
    newdate_account = datetime.datetime.now()
    newid_user = (input("Enter ID number:"))
    if newid_user.isdigit():
        newfirstname = input("Enter firstname:")
        int(newid_user)
        if newfirstname.isalpha():
            newlastname = input("Enter lastname:")
            if newlastname.isalpha():
                newmiddle_name = input("Enter middle_name:")
                newage = (input("Enter age:"))
                if newage.isdigit():
                    int(newage)
                    newgender = input("Enter gender:")
                    if newgender.isalpha():
                        newcity = input("Enter city:")
                        if newcity.isalpha():
                            newcountry = input("Enter country:")
                            if newcountry.isalpha():
                              newphone_number = input("Enter phone_number:")
                              if newphone_number.isdigit():
                                  int(newphone_number)
                                  newemail = input("Enter email:")
                                  b = newemail.split('@')
                                  if b[1] == 'gmail.com' or b[1] == 'yahoo.com':
                                      newaddress = input("Enter address:")
                                      if newaddress.isalpha():
                                          newusername = input("Enter username:")
                                          newpassword = input("Enter password:")
                                          if len(newpassword) >= 8 :
                                            print('ok')
                                          else:
                                            print('invalid password')
                                      else:
                                          print('invalid address')
                                  else:
                                      print('invalid email')
                              else:
                                  print('invalid phone number')
                            else:
                                print('invalid country')
                        else:
                            print('invalid city')

                    else:
                        print('invalid gender')
                else:
                    print('invalid age')
            else:
                print('invalid lastname')
        else:
            print('invalid firstname')
    else:
        print('invalid ID')
    try:
        c.execute("""insert into user(id_user,firstname,lastname,middle_name,age,gender,city,country,\
        phone_number,email,address,username,password,account_num,date_account) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """,(newid_user,newfirstname, newlastname\
                , newmiddle_name, newage, newgender, newcity, newcountry, newphone_number, newemail\
                , newaddress, newusername, newpassword, newaccount_num, newdate_account))
        con.commit()
    except:
        print('error')
        con.rollback()

    con.close()
sign_up()





