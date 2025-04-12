from rich_menu import Menu

menu = Menu(
    "Option 1",
    "Option 2",
    "Option 3",
    "Exit",
    color="red",
    align="center",

)
selected = menu.ask(screen=False)

match menu.ask():
    case "Option 1":
        print("first option selected")
    case "Option 2":
        print("second option selected")
    case "Option 3":
        print("third option selected")
    case "Exit":
        exit()