# World WAR

With this project, our group set out to visualize where the best baseball players in the world come from.

In order to answer this question, we needed some measure of who the best players are. For this, we turned to a metric called Wins Above Replacement-- WAR.

WAR is a complex (arguably just complicated) metric,and explaining it in great detail is far beyond the purview of this project. But in layman's terms, WAR is a metric designed to measure a baseball player's overall value in a single number. A metric like this allows analysts to compare players in a variety of interesting and valuable ways. 

To be clear, WAR is not perfect-- it's an imprecise measure which depends on some significant assumptions. But it lends itself to any study like ours that does not require a high degree of precision.

Our source is a site called Baseball-Reference, an internet baseball encyclopedia which is the gold standard of publicly available baseball data.

Baseball-Reference.com has a built-in tool that allows users to run basic queries of their data. Combining this tool with our newly acquired web-scraping skills, we were able to extract the top 200 hitters and top 200 pichers (according to WAR) from every country that has produced a Major League Baseball player. In instances where a country produced many players, we were limited to the top 200 players because the query tool on Baseball-Reference only produces 200 records per page. The mechanics of how we scraped this data prevented us from extracting every single hitter and pitcher from each country.

In addition to WAR data, we extracted from Baseball-Reference the city and country of birth for each player in our study, as well as the season in which each player made their MLB debut. 

![ETL-Project (1)](https://github.com/JMNugent1/war-by-country/blob/main/images/ETL%20Project%203.png)
