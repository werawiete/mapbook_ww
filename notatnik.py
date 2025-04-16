users:list=[
    {"name":"Mateusz","location":"Węgorzowo","posts":100},
    {"name":"Tomek","location":"Węgorzowo","posts":100},
]

print(users)


def remove_user(users_data: list[dict]) -> None:
    user_name=input("Podaj imie znajomego do usunięcia: ")
    for user in users:
        if user["name"] == user_name:
            users_data.remove(user)
print(users)