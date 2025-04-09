def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user['posts']} postów.")

def add_user(users_data: list)->None:
    new_name=input("Podaj imie: ")
    new_location=input("Podaj lokalizacje: ")
    new_post=input("Podaj liczbe postów: ")
    users_data.append({"name": new_name,"location": new_location,"posts": new_post})


