# Practice1
person1 = {
    'first':'zhang',
    'last':'yiju',
    'location':'zhengzhou'
}
person2 = {
    'first':'zhang',
    'last':'ci',
    'lacation':'zhumadian'
}
people = [person1,person2]
for person in people:
    print(person)

# Practice2
favorite_place = {
    'zhang':'zhengzhou',
    'wang':'beijing',
    'li':'tianjin',
    'zhao':'shanghai'
}
for name,place in favorite_place.items():
    print(name.title() + ' likes ' + place.title() + ' very much!')
    
# Practice3
cities = {
    'beijing':{
        'country':'China',
        'population':'much',
        'fact':'none'
    },
    'shanghai':{
        'country':'China',
        'population':'more',
        'fact':'yes'
    }
}
for city,city_info in cities.items():
    print(city)
    print(city_info['country'],city_info['population'],city_info['fact'])
        
        
        
        