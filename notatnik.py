users:list=[
    {"name":"Mateusz","location":"Węgorzowo","posts":100},
    {"name":"Tomek","location":"Węgorzowo","posts":100},
]

print(users)


def update_user(users_data: list[dict]) -> None:
    user_name=input("Podaj imie znajomego do aktualizacji: ")
    for user in users:
        if user["name"] == user_name:
            user["name"] =input("Podaj nowe imie znajomego:")
            user["location"] = input("Podaj nową miejscowość:")
            user["posts"] =int( input("Podaj nowa liczbę postów:"))



update_user(users)
print(users)


