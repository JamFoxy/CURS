def d():
    import json
    d_1 = "\n Enter 1 - Show a list of all coverage areas\n"
    d_2 = "Enter 2 - Show list of budget categories\n"
    d_3 = "Enter 3 - Show dedicated budget for a specific category of marketing sites\n"
    d_4 = "Enter 4 - Show current marketing funds\n"
    d_5 = "Enter 5 - Show total budget required for salary\n"
    d_6 = "Enter 6 - Increase the salary of an employee\n"
    d_7 = "Enter 7 - Lower the salary of an employee\n"
    d_8 = "Enter 8 - Show a list of equipment for the construction of objects\n"
    print(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8)
    ab = int(input("Please dial the menu number to work with the program,\n If you're done, dial 9:"))
    if ab == 1:
        print("List of all coverage for specific areas")
        with open("areas.json", "r") as file:
            areas = json.load(file)
            for i in areas:
                print(i["c"], i["n"])
        d()
    if ab == 2:
        def b():
            budg = input("Choose a category of budget m/s: ")
            mark = "The marketing budget: 400.000$"
            sal = "Salary budget: 380.000$"
            if budg == "m":
                print(mark)
                d()
            elif budg == "s":
                print(sal)
                d()
            else:
                print("Try again")
                b()
        print(b())
        d()
    if ab == 3:
        print("Marketing Zones Budget::")
        bu = int(input("\n1 - Facebook \n2 - Instagram \n3 - Google Ads \n4 - YouTube \nSelect one from the list (1-4):"))
        if bu == 1:
            print("1100$")
            d()
        if bu == 2:
            print("450$")
            d()
        if bu == 3:
            print('129.44$')
            d()
        if bu == 4:
            print('85$')
            d()
        else:
            print("You must type numbers from 1 to 4!")
    if ab == 4:
        print("General marketing media: ")
        with open("cost.json", "r") as r_file:
            costos = json.load(r_file)
            print(costos)
    if ab == 5:
        print("Salary budget: ")