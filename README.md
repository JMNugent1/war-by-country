# World W.A.R: An Analysis Of Win Above Replacement 

With this project, our group set out to visualize where the best MLB players are from.

In order to answer this question, we needed some measure of who the best players are. For this, we turned to a metric called Wins Above Replacement-- WAR.

WAR is a complex (arguably just complicated) metric,and explaining it in great detail is far beyond the purview of this project. But in layman's terms, WAR is a metric designed to measure a baseball player's overall value in a single number. A metric like this allows analysts to compare players in a variety of interesting and valuable ways. 

To be clear, WAR is not perfect-- it's an imprecise measure which depends on some significant assumptions. But it lends itself to any study like ours that does not require a high degree of precision.

Our source is a site called Stathead Baseball, an internet baseball encyclopedia which is the gold standard of publicly available baseball data.

Stathead.com has a built-in tool that allows users to run basic queries of their data. Combining this tool with our newly acquired web-scraping skills, we were able to extract the top 200 hitters and top 200 pichers (according to WAR) from every country that has produced a Major League Baseball player. In instances where a country produced many players, we were limited to the top 200 players because the query tool on Baseball-Reference only produces 200 records per page. The mechanics of how we scraped this data prevented us from extracting every single hitter and pitcher from each country.

In addition to WAR data, we extracted from Stathead Baseball the city and country of birth for each player in our study, as well as the season in which each player made their MLB debut. 

First, we used BeautifulSoup to web scrape the three letter country codes for the players and stored them in an array which we used as a parameter for another web scrape. Then we used BeautifulSoup python library to web scrape stathead.com to pull data such as player name, rank, WAR score, the year the player entered the league, the year the player retired, their age, and place of birth. With this information, we created two dictionaries, one for hitters, and one for pitchers. We then used for loops to scrape information based on country codes for the players and to get the information we wanted and stored in an array called “player_list” for each player. This process was repeated to get the information for the pitchers. The data we collected was imported into a Pandas dictionary for manipulation, and all of our data was saved as CSV files. 

With our clean data, the CSV file was read in order to load it into a SQLite file. From there, we created an engine to write our data to a SQLite file. Lastly, we created a SQL connection to our SQLite database. 

## Technology and Methodology

- Python
- SQLite
- HTML
- Javascript
- CSS

## Work Flow - Project ETL

![ETL-Project (1)](https://github.com/JMNugent1/war-by-country/blob/main/images/ETL%20Project%203.png)

## Data 
Data Source:

- Statehead Baseball 

The data is composed of:
- Player Name
- Age 
- Birth location
- Country 
- Coordinates 
- Position
- Win Above Replacement 


### ETL 

The data was extracted from Stathead Baseball using python's beautifulsoup library to webscrape for the specific data values mentioned above. specifically from filtering by player season & career finder for both pitchers and hitters.
Country and birth city were both available from the webscrape but coordinates were not. Thus, the python geopy library was used to iterate through city and country to return coordinates.

[Webscraping file here](https://github.com/JMNugent1/war-by-country/blob/main/development/main.ipynb)
[Coordinate extraction here](https://github.com/JMNugent1/war-by-country/blob/main/development/coordinates%20.ipynb)

### Transformation 

The data is then imported into a pandas dataframe where we merged coordinates to the main dataset. Here the data was also cleaned to remove players whose birth country coordinates could not be obtained from geopy.

### Load

We created a database on our local computer using SQLalchemy to store our final dataframe on an SQLite file. A flask app is used to store the data as geojson format inorder to call it later in javascript. 

![geojson](https://github.com/JMNugent1/war-by-country/blob/main/images/geojson.png)

- A relational SQL database was chosen over a non-relational NoSQL database because of it's ridigity . In other words, our tables are rigid meaning that the data is nomalized in a strictly defined table. SQL was chosen because of its ability to scale vertically and not horizontally, meaning we can update the data over time but keep all the variables (columns) the same. SQlite was our preferred flavore because of its single compact file that was easy to load to flask. 

[SQLite loader here](https://github.com/JMNugent1/war-by-country/blob/main/sqlite_loader.ipynb)
[geojason]

### Final Presentation 

The final data was imported into javascript to create our front end web page. Using the flask app we were able to host our api locally for testing. ultimatly, due to github pages lack of flask support, we were not able to host our final presentation on github pages. Though we are looking at potential workarounds such as hosting the api on AWS. 

The Final website is a leaflet street map with ability to filter by All players, hitters, pitchers, and a heat map. 

![All Players](https://github.com/JMNugent1/war-by-country/blob/main/images/all_players.png)

![Hitters](https://github.com/JMNugent1/war-by-country/blob/main/images/hitters.png)

![Pitchers](https://github.com/JMNugent1/war-by-country/blob/main/images/pitcher.png)

![Heat Map](https://github.com/JMNugent1/war-by-country/blob/main/images/heat%20map.png)
