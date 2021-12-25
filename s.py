def s():
    import json
    d_1 = "\n Enter 1 - Show all clients\n"
    d_2 = "Enter 2 - Client search\n"
    d_3 = "Enter 3 - Show available apartments for purchase\n"
    d_4 = "Enter 4 - Show sold apartments\n"
    d_5 = "Enter 5 - Show the most expensive apartment\n"
    d_6 = "Enter 6 - Show the cheapest apartment\n"
    d_7 = "Enter 7 - Sell an apartment\n"
    d_8 = "Enter 8 - Rent out an apartment\n"
    d_9 = "Enter 9 - Show free objects\n"
    d_10 = "Enter 10 - Display of rented objects\n"
    print(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10)
    sale = int(input("Please dial the menu number to work with the program,\n If you're done, dial 9:"))
    if sale == 1:
        with open("clients.json", "r") as file:
            clients = json.load(file)
            for item in clients:
                print(item["client"], item["do"])
            s()
    elif sale == 2:
        def Check():
            s_client = input("Enter customer name to search: ")
            with open("clients.json", "r") as file:
                clients = json.load(file)
                person = clients.get("clients")
                for item in person:
                    if s_client == "Kani":
                        print("Client was found: ")
                        print(item.get("client"), item.get("do"))
                        s()
                    elif s_client == "Khabib":
                        print("Client was found: ")
                        print(item.get("client"), item.get("do"))
                        s()
                    elif s_client == "John":
                        print("Client was found: ")
                        print(item.get("client"), item.get("do"))
                        s()
                    elif s_client == "Slava":
                        print("Client was found: ")
                        print(item.get("client"), item.get("do"))
                        s()
                    elif s_client == "Yo Yo":
                        print("Client was found: ")
                        print(item.get("client"), item.get("do"))
                        s()
                    else:
                        print("Incorrect name of client. Try again!")
                        Check()
        print(Check())
        s()
    elif sale == 3:
        print("Free Apartments: ")
        with open("free_ap.json", "r") as file:
            free_ap = json.load(file)
            for item in free_ap:
                print(item["number"], item["place"])
    elif sale == 4:
        print("Sold Apartments: ")
        with open("sold_ap.json", "r") as file:
            sold_ap = json.load(file)
            for item in sold_ap:
                print(item["number"], item["place"])
            s()
    elif sale == 5:
        expensive = "Apartment 75: Jal-29,18. Cost: 366 $ per month"
        print("Most expensive apartment: ", expensive)
        s()
    elif sale == 6:
        cheep = "Apartment 111: Tokombaeva 21/3"
        print("The cheapest apartment: ", cheep)
        s()
    elif sale == 7:
        f = "adress"
        n = "name"
        adr = input("Please write the sales address: ")
        host = input("Please write the new owner of the apartment: ")
        with open("sale-buildings.json", "r") as file:
            sale_buildings = json.load(file)
            for item in sale-b:
                if adr == "Tynystanova 12":
                    sale_buildings[0][f] = adr
                    sale_buildings[0][n] = host
                    with open("sale-buildings.json", "w") as w_file:
                        json.dump(sale_buildings, w_file)
    elif sale == 8:
        with open("rent.json", "r") as file:
            rent = json.load(file)
            for i in rent:
                print(i["adress"], i["name"], i["sum"], i["dline"], i["status"])
        f = "adress"
        n = "name"
        status = "status"
        fin = "occupied"
        adr = input("Please write the sales address: ")
        host = input("Please write the new owner of the apartment: ")
        with open("rent.json", "r") as file:
            rent = json.load(file)
            for item in rent:
                if adr == "Tynystanova 12":
                    rent[1][f] = adr
                    rent[1][n] = host
                    rent[1][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                    with open("rent.json", "r") as file:
                        rent = json.load(file)
                        for i in rent:
                            print(i["adress"], i["name"], i["sum"], i["dline"], i["status"])
                elif adr == "Abay 4":
                    rent[3][f] = adr
                    rent[3][n] = host
                    rent[3][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                    with open("rent.json", "r") as file:
                        rent = json.load(file)
                        for i in rent:
                            print(i["adress"], i["name"], i["sum"], i["dline"], i["status"])