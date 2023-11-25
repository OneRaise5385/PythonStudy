from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['zhang'] = 'Python'
favorite_languages['wang'] = 'Java'
favorite_languages['li'] = 'C'
favorite_languages['zhao'] = 'C++'

print(favorite_languages)
for name,language in favorite_languages.items():
    print(name.title() + ' loves ' + language.title())