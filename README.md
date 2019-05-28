# WikiScrape

We collect data from [Wikipedia](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population) about the top cities in the United States. The collected data is targeted to predict which party will win the mayor election based on latest racial decomposition data reported by the US Census Bureau. We can also use Mayor's name to exctract more data e.g. [gender](http://web.b.ebscohost.com/abstract?site=ehost&scope=site&jrnl=19384122&AN=125676755&h=ypzTlFHkz6dlcPoQQ%2bwyWw3D4XZUuS0fiG95SaztiSOC3iwKyTeRzpmVXBlk7eyM6W3DgXxswEPUfBiwCnpojw%3d%3d&crl=c&resultLocal=ErrCrlNoResults&resultNs=Ehost&crlhashurl=login.aspx%3fdirect%3dtrue%26profile%3dehost%26scope%3dsite%26authtype%3dcrawler%26jrnl%3d19384122%26AN%3d125676755).

## The Algorithm

We use BeautifulSoup and Requests Python Standard Libraries To retrieve and parse the Wikipedia page and search for specific elements. For each city we collect the latest racial composition data ('White', 'Black', 'Asian', 'Latino') and the current mayor’s political affiliation ('D', 'R', 'I', 'L', 'G', 'C'). We use Scaling (MinMaxScaler) and Label Encoding (LabelEncoder) methods for further data processing. The output file is in CSV format ready to be uploaded to a BigQuery table.

## The Code

To run this demo, you will need:

- Python 2.7
-	Pip
-	Scikit-learn
-	Numpy
-	BeautifulSoup
-	Requests
-	Regex
-	Pandas

### Setup the code
```$ git clone git@github.com:https://github.com/maralamir/WikiScrape.git

$ sudo pip install numpy
$ sudo pip install scikit-learn
$ sudo pip install requests
$ sudo pip install beautifulsoup4
$ sudo pip install regex
$ sudo pip install pandas

