"""

___Author___ = Joshua Cowan
"""
print("Welcome! To the Spongebob Squarepants quiz!"), '\n'
print(
    'Here you will be asked a series of questions regarding food, activities,'
    ' etc. to see who you resemble most from '
    'Spongebob!')


def invalid_input():
    print("Invalid input, please make sure there are no grammatical errors or"
          " incorrect capitals. :)")


quiz_end = False

questions = int(1)

patrick = 0
sandy = 0
mrkrabs = 0
plankton = 0
spongebob = 0
squidward = 0

while not quiz_end:
    if questions == 1:
        print()
        print("Which of these foods would you choose?"),
        print(input("Money, Chum, Ice Cream, or Krabby Patties?"))
        print()

        if input == "Money" or input == "money":
            mrkrabs = 2

        elif input == "Chum" or input == "chum":
            plankton = 2

        elif input == "Ice Cream" or input == "ice cream":
            patrick = 2

        elif input == "Krabby patties" or input == "Krabby Patties":
            spongebob = 2
            sandy = 2

        else:
            print("this selection is invalid, please correct any spelling"
                  " errors, or choose a valid response ")
            questions == 1
    questions += 1
#The transition here is hard to keep working while also keeping the Q loop
#Next time doing massive loops, try to utilize classes to make working
#On the loop easier instead of having to change EVERYTHING
    if questions == 2:
        print()
        print("Which of the following is your favorite pass time?"),
        print(input("Money, Cooking, Science, Jellyfishing, or Sleeping?"))

        if input == "Money" or input == "money":
            mrkrabs + int(1)

        elif input == "science" or input == "Science":
            plankton + int(1)
            sandy + int(1)

        elif input == "Sleeping" or input == "sleeping":
            patrick + int(1)

        elif input == "Cooking" or input == "cooking":
            spongebob + int(1)

        elif input == "Jelly Fishing" or input == "jellyfishing":
            spongebob + int(1)
            patrick + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                        "errors, or choose a valid response :)")
            questions = 2
    questions += 1

    if questions == 3:
        print()
        print("Pick a word?"),
        print(input("Money, Cheerful, Imagination, Science, Music"))

        if input == "Money" or input == "money":
            mrkrabs + int(1)

        elif input == "Cheerful" or input == "cheerful":
            spongebob + int(1)

        elif input == "Imagination" or input == "imagination":
            patrick + int(1)
            spongebob + int(1)

        elif input == "Science" or input == "science":
            sandy + int(1)

        elif input == "Music" or input == "music":
            squidward + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                        "errors, or choose a valid response :)")
            questions = 3
    questions += 1

    if questions == 4:
        print()
        print("Pick a color?"),
        print(input("Yellow, Pink, Green, Blue, Red"))

        if input == "Yellow" or input == "yellow":
            spongebob + int(1)

        elif input == "Pink" or input == "pink":
            patrick + int(1)

        elif input == "Green" or input == "green":
            mrkrabs + int(1)

        elif input == "Blue" or input == "blue":
            squidward + int(1)

        elif input == "Red" or input == "Red":
            mrkrabs + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                        "errors, or choose a valid response :)")
            questions = 4
    questions += 1

    if questions == 5:
        print()
        print("What's your favorite Holiday?"),
        print(input("Leif Erikson Day, Annoy Squidward Day, Halloween,"
                    " Give Mr. Krabs Money Day, Opposite Day"))

        if input == "Leif Erikson Day":
            patrick + int(1)

        elif input == "Annoy Squidward Day":
            spongebob + int(1)

        elif input == "Halloween":
            squidward + int(1)

        elif input == "Give Mr. Krabs Money Day":
            mrkrabs + int(1)

        elif input == "Opposite Day":
            plankton + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 5
    questions += 1

    if questions == 6:
        print()
        print("How would your friends describe you?")
        print(input("Stupid, Creative, Smart, Stingy, Grumpy"))

        if input == "Stupid":
            patrick + int(1)

        elif input == "Creative":
            plankton + int(1)

        elif input == "Smart":
            sandy + int(1)

        elif input == "Stingy":
            mrkrabs + int(1)

        elif input == "Grumpy":
            squidward + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 6
    questions += 1

    if questions == 7:
        print()
        print("Which Bikini Bottom Resident would you like to hang out with?")
        print(input("Karen, Larry, Mrs. Puff, Gary, Nobody"))

        if input == "Karen":
            plankton + int(1)

        elif input == "Larry":
            patrick + int(1)

        elif input == "Mrs. Puff":
            mrkrabs + int(1)

        elif input == "Gary":
            spongebob + int(1)

        elif input == "Nobody":
            squidward + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 7
    questions += 1

    if questions == 8:
        print()
        print("Pick an instrument")
        print(input("Clarinet, Mayonnaise, Drums, Violin, Guitar"))

        if input == "Clarinet":
            squidward + int(1)

        elif input == "Mayonnaise":
            patrick + int(1)

        elif input == "Drums":
            sandy + int(1)

        elif input == "Violin":
            mrkrabs + int(1)

        elif input == "Guitar":
            spongebob += 1

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 8
    questions += 1

    if questions == 9:
        print()
        print("What's your favorite item?")
        print(input("A Krabby Patty, Secret Box, Chocolate, Walnuts"))

        if input == "A Krabby Patty":
            mrkrabs + int(1)
            plankton + int(1)

        elif input == "Secret Box":
            patrick + int(1)

        elif input == "Chocolate":
            spongebob + int(1)

        elif input == "Walnuts":
            sandy + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
             "errors, or choose a valid response :)")
            questions = 9
    questions += 1

    if questions == 10:
        print()
        print("Are you ready?")
        print(input("I'm Ready. I'm Ready!, Ready for what?, Oh no.,"
                    "Ready to count me money!, Ready for the secret formula!"))

        if input == "I'm ready. I'm ready!":
            spongebob + int(1)

        elif input == "Ready for what?":
            patrick + int(1)

        elif input == "Oh no.":
            squidward + int(1)

        elif input == "Ready to count me money!":
            mrkrabs + int(1)

        elif input == "Ready for the secret formula":
            plankton + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
             "errors, or choose a valid response :)")
            questions = 10

    quiz_end = True


while quiz_end = True:
    if (patrick > sandy
            and patrick > mrkrabs
            and patrick > squidward
            and patrick > spongebob
            and patrick > plankton):
          print("You got Patrick Star! The lovable, albeit slow starfish.")
    
    elif (sandy > patrick
          and sandy > mrkrabs
          and sandy > spongebob
          and sandy > plankton
          and sandy > squidward):
          print("You got Sandy Cheeks! The smart and sassy squirrel")
    
    elif (spongebob > patrick
        and spongebob > sandy
        and spongebob > plankton
        and spongebob > mrkrabs
        and spongebob > squidward):
          print("You got Spongebob Squarepants! The Happy-go Lucky Sponge.")
    
    elif (plankton > spongebob
          and plankton > squidward
          and plankton > sandy
          and plankton > patrick
          and plankton > mrkrabs):
            print("You got Plankton! The Evil genius who always wants the"
                  "secret formula")
          
    elif (squidward > spongebob
        and squidward > patrick 
        and squidward > sandy 
        and squidward > mrkrabs 
        and squidward > plankton):
            print("You got Squidward! The depressed artist type.")
    
    elif (mrkrabs > spongebob
        and mrkrabs > squidward
        and mrkrabs > sandy
        and mrkrabs > plankton
        and mrkrabs > patrick):
            print("You got Mr. Krabs! The money obsessed owner of"
                  "the Krusty Krab.")
    else:
        print("Sorry, you do not have a strong leaning towards any of"
              "the characters, please try again!")
print ("Thank you for taking my Spongebob quiz!")
