from db_helpers import *
from dbcreds import *




print("You successfully hacked the system , Congrats")
print("-------------------------------------------")
print ("What would you like to take a look at ?")
print("1.Enter new content ")
print("2.See all content")
print("3.See all content except yours  ")
print("4.EXIT ")
option = input ("1/2/3/4 :")

if option == "1":
    content = input("Enter your content :")
    run_query("INSERT INTO exploits(content) VALUES (?)",[content])
elif option == "2":
    view_content= run_query("SELECT content FROM exploits")
    print(view_content)
elif option =="3":
    view_some_content = run_query("SELECT content FROM exploit WHERE id=?" , [login])
elif option == "4":
    exit()




# user_id: input ("Enter user login :")




# users=run_query("SELECT alias FROM hackers WHERE id ='21'")
# print(users)





# user_id: input ("Enter user login :")
# if input : 
#     run_query("SELECT alias from user")
# else : 
#     print("Alias does not exist")
    
# # password : input("Enter password :")

# # run_query("SELECT alias from user")

