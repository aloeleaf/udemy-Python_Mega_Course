languages = ['English', 'German', 'Spanish']
# with open('languages.txt', 'w') as file:
#     #filenames = [lanuage + '.txt' for lanuage in languages]
#     for language in languages:
#         file.write(language + '.txt\n')

for language in languages:
    with open(language + '.txt', 'w') as file:
        file.write(f'{language}')