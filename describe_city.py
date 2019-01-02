def describe_city(city,country='U.S.A.'):
    """ Describes a city and the country it is located in """
    print(city.title() + " is a lovely city, located in " + country.title())

describe_city(city='Philadelphia')
describe_city(city='Dallas')
describe_city(city='paris',country='france')
