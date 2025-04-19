print("Welcome to the Mad Libs Game!")

# Define the story template with placeholders
story_template = """
It was a {adjective1} day when {name} decided to visit the {place}.
They found a {adjective2} {animal} that was {activity}.
Surprised, {name} exclaimed, "What a {adjective3} sight!" and decided to join the fun.
"""

# Prompt the user for inputs to fill the placeholders
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
activity = input("Enter an activity (e.g., running, dancing): ")
adjective3 = input("Enter one more adjective: ")

# Fill the story with the user's words
final_story = story_template.format(
    name=name, place=place, adjective1=adjective1, adjective2=adjective2,
    animal=animal, activity=activity, adjective3=adjective3
)

# Display the completed story
print("\nHere's your Mad Libs story!\n")
print(final_story)