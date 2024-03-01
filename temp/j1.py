import pyodbc
import maskpass
import time,os

while True:
    user = input("Enter your J1 username: ")
    current = maskpass.askpass(prompt="Enter your current password: ",mask="*")
    os.system('cls')

    connectionString = f'DRIVER={{SQL Server}};SERVER=JICEX;DATABASE=TmsEPrd;UID={user};PWD={current}'
    try:
        conn = pyodbc.connect(connectionString)
        break
    except pyodbc.Error as err:
        state = err.args[1].split(']')
        state = state[4].split('.')
        print(state[0])
        time.sleep(3)
        os.system('cls')


cursor = conn.cursor()

while True:
    while True:
        new = "'"+maskpass.askpass(prompt="Enter your new password: ",mask="*")+"'"
        confirm = "'"+maskpass.askpass(prompt="Confirm your new password: ",mask="*")+"'"

        if new != confirm:
            print ("Passwords don't match")
        else:
            break

    os.system('cls')

    current = "'"+current+"'"

    sql_query=f"""
    declare @return varchar(max)
    begin try
        alter login {user} with password={confirm} old_password={current}
    end try
    begin catch
        select @return = error_message()
    end catch
    select @return = isnull(@return,'Password reset')
    select @return
    """

    cursor.execute(sql_query)
    error = cursor.fetchall()

    msg = str(error[0])
    msg = msg.strip("(),'")
    
    os.system('cls')
    
    if msg == 'Password reset':
        print(msg)
        break
    else:
        print ("Password doesn't meet length, age, or complexity requirements.")
        time.sleep(3)
        os.system('cls')

conn.commit()
cursor.close()
conn.close()

time.sleep(3)