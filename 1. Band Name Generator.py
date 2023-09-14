def band_name_generator():
    city = input(str("What\'s the name of the city you grew up in?"))
    pet = input(str("What\'s you pet\'s name?"))
    return f'Your band name could be {city} {pet}'
name_generator = band_name_generator()
print(name_generator)