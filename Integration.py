#Joshua Cowan\n
#I want to create a buzzfeed quiz that is fun and simple for my friends and family to enjoy. Afterwards I will pool the results.
print (2+3)
print ("Hello! Welcome to 'Which Spongebob character are you?'")
#I need to create a defined system for the Q/A format
class question:
    def __init__(self, prompt, selection):
        self.prompt = prompt
        self.prompt = selection
question_prompts = [
    "What do you like to do for fun?\n(a) Sleeping\n(b) Playing Music\n(c) Reading\n(d) Jellyfishing\n(e) Watch TV"
#Keeping this template in mind, I should have roughly 4-7 answers for each question.
#Sponge, Pat, Squid, Sandy, Gary, Krabs, Plankton
    "Where is your ideal place to work?"
    "If you could live anywhere in the world, where would it be?"
    "Pick a word"
    "What is your favorite food?"
    "What is your favorite Spongebob episode?"
    "You have a big assignment coming up. How do you deal with the workload?"

]

def run_test(question):
        spongebobScore= 0
        squidwardScore= 0
        patrickScore= 0
        sandyScore= 0
        garyScore= 0
        krabsScore= 0
        planktonScore= 0
    #Figure out how to fix test(quiz question loop)
for question in question_prompts:
    selection = input(question.prompt)
    print ("Correct")
