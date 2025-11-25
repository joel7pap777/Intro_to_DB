shopping_list = []

while True:
 user_choice=  input('enter an option(1.add an item 2.remove an item 3.view list 4.exit):')
 if user_choice == '1':
      user_input = input('what item do you want to add:')
      shopping_list.append(user_input)
      print(f"you have added {user_input} to shopping list")
 elif user_choice == '2':
       user_input = input('what item do you want to remove:')
       shopping_list.remove(user_input)
       print(f"you have removed {user_input} from shopping list")
       
 elif user_choice == '3':
     print(shopping_list)
     
 elif user_choice == '4':
     print('you have exited the application')
     break
 else:
     print('invalid input')
     
     
    
    
             
    
