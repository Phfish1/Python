

### EVIL NAME CHECKER AND LOGGER ### 



## Names to BAN
evil_names = ["Ben", "Jens", "PP"]


def rememberer():

    ## Welcome
    name = input("What is your name: ")

    ## Evil_name checker
    for bad_guys in range(len(evil_names)):
        if name == evil_names[bad_guys]:
            print("U evil")
            
            ## To return the user out of the def
            return

    ## Greeter
    print("Hi "+ name)

    ## Evil_true checker and stores Evil name
    evil = input("Are you Evil? ")


    if evil == "Yes" or evil == "yes":
        print("bye bye")
        evil_names.append(name)
        return
    
    print("Welcome in ;)")



## Loop to run everything
done = False

while done == False:
    rememberer()
    print("Evil names: " + str(evil_names))

    more = input("Try again? [Y/N] ")
    if more == "y" or more == "Y":
        done = False
    else:
        done = True


print("\nYou are Done :)")
