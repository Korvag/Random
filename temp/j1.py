import pyodbc
import maskpass

user = input("Enter your J1 username: ")
current = maskpass.askpass(prompt="Enter your current password: ",mask="*")

while True:
    new = "'"+maskpass.askpass(prompt="Enter your new password: ",mask="*")+"'"
    confirm = "'"+maskpass.askpass(prompt="Confirm your new password: ",mask="*")+"'"

    if new != confirm:
        print ("Passwords don't match")
    else:
        break

connectionString = f'DRIVER={{SQL Server}};SERVER=JICEX;DATABASE=TmsEPrd;UID={user};PWD={current}'
conn = pyodbc.connect(connectionString)

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

cursor = conn.cursor()
cursor.execute(sql_query)
error = cursor.fetchall()
print(error[0])

conn.commit()
cursor.close()
conn.close()