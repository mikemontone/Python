def city_country(city,country):
    """ Return a city and country, neatly formatted. """
    neat_name = city + ' ' + country
    return neat_name.title()

while True:
    print("\n Please tell me your city:")
    print("(enter 'q' at any time to quit)")

    city_name = input("City name: ")
    if city_name == 'q':
        break
    
    country_name = input("Country name: ")
    if country_name == 'q':
        break
    
    formatted_neat_name = city_country(city_name,country_name)
    print(city_name.title() + ',' + country_name.title())
