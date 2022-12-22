# World WAR

With this project, our group set out to visualize where the best baseball players in the world come from.

In order to answer this question, we needed some measure of who the best players are. For this, we turned to a metric called Wins Above Replacement-- WAR.

WAR is a complex (arguably just complicated) metric,and explaining it in great detail is far beyond the purview of this project. But in layman's terms, WAR is a metric designed to measure a baseball player's overall value in a single number. A metric like this allows analysts to compare players in a variety of interesting and valuable ways. 

To be clear, WAR is not perfect-- it's an imprecise measure which depends on some significant assumptions. But it lends itself to any study like ours that does not require a high degree of precision.

Our source is a site called Stathead Baseball, an internet baseball encyclopedia which is the gold standard of publicly available baseball data.

Stathead.com has a built-in tool that allows users to run basic queries of their data. Combining this tool with our newly acquired web-scraping skills, we were able to extract the top 200 hitters and top 200 pichers (according to WAR) from every country that has produced a Major League Baseball player. In instances where a country produced many players, we were limited to the top 200 players because the query tool on Baseball-Reference only produces 200 records per page. The mechanics of how we scraped this data prevented us from extracting every single hitter and pitcher from each country.

In addition to WAR data, we extracted from Stathead Baseball the city and country of birth for each player in our study, as well as the season in which each player made their MLB debut. 

First, we used BeautifulSoup to web scrape the three letter country codes for the players and stored them in an array which we used as a parameter for another web scrape. Then we used BeautifulSoup python library to web scrape stathead.com to pull data such as player name, rank, WAR score, the year the player entered the league, the year the player retired, their age, and place of birth. With this information, we created two dictionaries, one for hitters, and one for pitchers. We then used for loops to scrape information based on country codes for the players and to get the information we wanted and stored in an array called “player_list” for each player. This process was repeated to get the information for the pitchers. The data we collected was imported into a Pandas dictionary for manipulation, and all of our data was saved as CSV files. 

With our clean data, the CSV file was read in order to load it into a SQLite file. From there, we created an engine to write our data to a SQLite file. Lastly, we created a SQL connection to our SQLite database. 


![ETL-Project (1)](https://github.com/JMNugent1/war-by-country/blob/main/images/ETL%20Project%203.png)
