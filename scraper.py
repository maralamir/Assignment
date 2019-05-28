try:
	from bs4 import BeautifulSoup
	import requests
	import csv
	import re
	import pandas as pd
	from sklearn.preprocessing import MinMaxScaler
	from sklearn.preprocessing import LabelEncoder
except ImportError:
	print("Please install BeautifulSoup,Requests,cvs,pandas, sklearn, StandardScaler, MinMaxScaler, LabelEncoder Module.")



class ScrapperClass:

	d = {}
	race = {'White' : 0, 'Black' : 1,  'African American': 1, 'Asian': 2, 'Latino': 3}
	partylist = ['D','R', 'I', 'L', 'G', 'C']


	@staticmethod
	def getSoup(url1):
		website_url = requests.get(url1).text
		return BeautifulSoup(website_url, 'lxml')


# store cities and wiki links
	def listCities(self, table):
		for row in table.findAll('tr')[1:]:
			symbol_cell = row.find_all('td')[1]
			a = symbol_cell.find('a')
			link = 'https://wikipedia.org' + a.get('href')
			city = a.get('title').split(',')[0]
			self.d[city] = {}
			self.d[city]['link'] = link


# scrape city wikipedia 
	def scrapeCities(self):
		csv_file = open( 'data/output.csv', 'w')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['City', 'Link', 'Mayor', 'Party', 'White', 'Black', 'Asian', 'Latino'])


		for key, value in self.d.iteritems():
			link = value['link']
			rlist = {0:0, 1:0, 2:0, 3:0} # list of races for each city
			website_url = requests.get(link).text
			soup = BeautifulSoup(website_url, 'lxml')
			table = soup.find('table','th', class_='wikitable sortable collapsible')

	# racial composition 
			try:
				rows = table.find_all('tr')[1:] 
				for row in rows:
					str = row.find_all('td')[0].text
					find = filter(lambda x:  x in str, self.race) #find values in race 
					if find:
						ratio = row.find_all('td')[1].text
						lst = ratio.split() 
						ratio = filter (lambda x: '%' in x, lst)[0] #find percentage
						rlist[self.race[find[0]]] = ratio[:ratio.find("%")]
					else:
						continue
			
		
	# political party of Mayor 
				infotable = soup.find('table', class_='infobox')
				rows = infotable.find_all('tr','th', class_='mergedrow')
				for row in (row for row in rows if row.find('th') and row.find('th').find(text = 'Mayor') != None): #check if we have 'Mayor' within <th> tag
					mayor = row.find('td').text
					party = mayor[mayor.find("(")+1]
					self.d[key]['party'] = filter(lambda x:  x in party, self.partylist)[0] #if in partylist
					mayor = re.sub(r'\(.*\)', '', mayor) #clean () data
					self.d[key]['mayor'] = re.sub(r'\[[^\]]*\]', '', mayor) #clean [] data
				csv_writer.writerow([key.encode('utf-8'), link.encode('utf-8'), self.d[key]['mayor'].encode('utf-8'), self.d[key]['party'].encode('utf-8'), rlist[0], rlist[1], rlist[2], rlist[3]])  
			except Exception as e:
				# print e.__class__, e.__doc__, e.message
				continue
		csv_file.close()


# process data
	def dataprocessing(self):
		df = pd.read_csv('data/output.csv')


# drop NaN
		columns = ['Party']
		df = df.dropna(axis=0, how='any', subset=columns).fillna(0)	


# scaling & standardize
		
		cols1 = ['White', 'Black', 'Asian', 'Latino']
		cols2 = ['White Normalize', 'Black Normalize', 'Asian Normalize', 'Latino Normalize']
		df[cols1] = df[cols1].apply(pd.to_numeric, errors='coerce')
		scaled_df = MinMaxScaler().fit_transform(df[cols1])
		scaled_df = pd.DataFrame(scaled_df, columns=cols2)
		df = pd.concat([df, scaled_df], axis=1, join_axes=[df.index])
		df[cols2] = df[cols2].round(2)


# label encoding:
		LE = LabelEncoder()
		df['Encoded Party'] = LE.fit_transform(df['Party'])
		df.to_csv('data/output.csv')












