with open('story.txt', 'r') as file:
    story = file.read()

with open('story_copy.txt', 'w') as file:
    file.write(story)