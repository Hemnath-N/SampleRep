# Show the list of Movies
# Doing this for creating Feature Branch
movies = {"96":{"Age":3,"Tkts":500},
          "Ratsasan":{"Age":14,"Tkts":500},
          "Vada Chennai":{"Age":18,"Tkts":500}}
exit = True

while exit:
    
    # Check for the customers Age

    cust_Name = input("Please enter your name: ").strip()
    chk_Age = int(input("Please enter your Age: ").strip())

    print(movies.keys())
    sel_Movie = input("Please enter the Movie name: ").strip().title()

    # If the age is not appropriate show some message
    # If age is valid and then allow to go further

    if sel_Movie in movies:
        
        if (chk_Age >= (movies[sel_Movie]["Age"])):
            num_Tickets = int(input("Enter number of seats to book: "))
            if num_Tickets <= (movies[sel_Movie]["Tkts"]):
                print("Tickets Booked Succssfully!")
                movies[sel_Movie]["Tkts"] = (movies[sel_Movie]["Tkts"]) - num_Tickets
                print("Balance Tickets: {}".format(movies[sel_Movie]["Tkts"]))
            else:
                print("Sorry! Seats are not available")

        else:
            print("Sorry! Your Age is inapproriate to watch the movie selected...")
            print("Please select other movie")

    else:
        print("Sorry! the movie enterered is not available at the moment!!!")
    
    t_Exit = input("Do you want to Conitinue(Y/N)? ").strip().lower()

    if t_Exit == "n":
        exit = False
    else:
        exit = True
