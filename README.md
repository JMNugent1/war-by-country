# World W.A.R: An Analysis of Where The Best Baseball Players Come From

With this project, our group set out to visualize where the best MLB players are from.

In order to answer this question, we needed some measure of who the best players are. For this, we turned to a metric called Wins Above Replacement-- WAR.

WAR is a complex (arguably just complicated) metric, and explaining it in great detail is far beyond the purview of this project. But in layman's terms, WAR is a metric designed to measure a baseball player's overall value in a single number. A metric like this allows analysts to compare players in a variety of interesting and valuable ways. 

To be clear, WAR is not perfect-- it's an imprecise measure which depends on some significant assumptions. But it lends itself to any study like ours that does not require a high degree of precision.

Our source is a site called Stathead Baseball, an internet baseball encyclopedia which is the gold standard of publicly available baseball data.

Stathead.com has a built-in tool that allows users to run basic queries of their data. Combining this tool with our newly acquired web-scraping skills, we were able to extract the top 200 hitters and top 200 pichers (according to WAR) from every country that has produced a Major League Baseball player. In instances where a country produced many players, we were limited to the top 200 players because the query tool on Stathead Baseball only produces 200 records per page. The mechanics of how we scraped this data prevented us from extracting every single hitter and pitcher from each country.

In addition to WAR data, we extracted from Stathead Baseball the city and country of birth for each player in our study, as well as the season in which each player made their MLB debut. 

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

The data was extracted from Stathead Baseball using python's BeautifulSoup library to webscrape for the specific data values mentioned above, specifically from filtering by player season & career finder for both pitchers and hitters, creating a dictionary for both. Country and birth city were both available from the webscrape but coordinates were not. Thus, the python geopy library was used to iterate through city and country to return coordinates. 

Links to webscraping and coordinate code:

- [Webscraping code here](https://github.com/JMNugent1/war-by-country/blob/main/development/main.ipynb)
- [Coordinate extraction here](https://github.com/JMNugent1/war-by-country/blob/main/development/coordinates%20.ipynb)

### Transformation 

The data was then imported into a Pandas dataframe where we merged coordinates to the main dataset. Here, the data was also cleaned to remove players whose birth country coordinates could not be obtained from geopy. All of the data we collected and cleaned was exported to CSV files for ease of use in later coding and as an emergency back-up. 

### Load

We created a database on our local computer using SQLalchemy to store our final dataframe on an SQLite file. A flask app was used to store the data in geojson format in order to use it in javascript later for front-end development. 

![geojson](https://github.com/JMNugent1/war-by-country/blob/main/images/geojson.png)

- A relational SQL database was chosen over a non-relational NoSQL database because of its ridigity and its ability to scale vertically and not horizontally, meaning we can update the data over time, but keep all the variables (columns) the same in case we decided to incorporate other leagues in the future. SQlite was our preferred flavor of SQL because of its single compact file that was easy to load into flask. 

[SQLite loader here](https://github.com/JMNugent1/war-by-country/blob/main/sqlite_loader.ipynb)
[geojason]

### Final Presentation 

The final data was imported into JavaScript to create our front-end web page. Using the flask app, we were able to host our API locally for testing. Ultimatly, due to GitHub pages lack of flask support, we were not able to host our final presentation on GitHub pages, though we are looking at potential workarounds such as hosting the API on AWS. 

The final website is a leaflet street map with the ability to filter by all players, hitters, pitchers, and a heat map. Each point on the map will display player name, war value, and position.

##### Front-end Popup
![Popup](https://github.com/JMNugent1/war-by-country/blob/main/images/popup.png)

##### Front-end filtered by All Players
![All Players](https://github.com/JMNugent1/war-by-country/blob/main/images/all_players.png)

##### Front-end filtered by Hitters
![Hitters](https://github.com/JMNugent1/war-by-country/blob/main/images/hitters.png)

##### Front-end filtered by Pitchers
![Pitchers](https://github.com/JMNugent1/war-by-country/blob/main/images/pitcher.png)

##### Front-end filtered by Heatmap
![Heat Map](https://github.com/JMNugent1/war-by-country/blob/main/images/heat%20map.png)

### Project limitations

- Coordinates need to be reiterated with the addition of a player name to insure quality control of the data when merging. Orginally, coordinates were iterated seperatly and then added to the main database. 

- Githubs incompatibility with flask apps. Potential solutions include storing geojason on a AWS server for use with D3 library. 

- Further analysis is required to determine where the best players come from and not just an analysis of the MLB as the majority of its players are from the United States. This could be solved with the addition of leagues in other countries for less bias data.
