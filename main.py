from final import ScrapperClass

sc = ScrapperClass()

# Wikipedia page listed top US cities 
wikiurl = 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'

# create soup object
soup = sc.getSoup(wikiurl)

# find top cities list 
citiesTable = soup.find('table', class_='wikitable sortable')

# store cities url
sc.listCities(citiesTable)

# scrape cities
sc.scrapeCities()

#normalize
sc.dataprocessing()