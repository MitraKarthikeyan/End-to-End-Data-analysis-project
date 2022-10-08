# End to End Data-Analaysis-Project

<p align="center">

  [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Problem Statement:
Rising urbanisation, booming industrialisation, and associated anthropogenic activities are the prime reasons that lead to air pollutant emissions and poor air quality. According to HEI's report, particulate matter (PM) pollution was considered the third important cause of death in 2017 and this rate was found to be highest in India. Air pollution was considered to cause over 1.1 million premature deaths in 2017 in India (HEI 2019), of which 56% was due to exposure to outdoor PM2.5 concentration and 44% was attributed to household air pollution. 
So I've decided to collect real-time data and analyse it to see what's going on. In this project, I examined the rate of air pollution in Indian cities in terms of major air pollutants.
  
### I have uploaded the data collected to Kaggle, please find the dataset link, it's a 1.35 GB File [Data Set](https://www.kaggle.com/datasets/gokulguugu/air-pollution-india)

My Project architecture answers the question:

    1. How to collect the real time data from an API?
    2. How and were to store the collected data?
    3. How at create a end to end pipeline? So that we can automate the job and keep process running 24*7
    4. How to interact  with the Virtual machine and AWS RDS
    5. Connecting AWS RDS to MySql workbench.
    6. Pushing the data from database to Jupyter NoteBook for analysis.
    
 # Project Architecture:
 ![System design](https://github.com/MitraKarthikeyan/End-to-End-Data-analysis-project/blob/main/Documentation/proj_arc.jpg)

  From the collected data, I am tring to answer the question,
  
     1. Which State in India has the highest number of pollutant emittance from 2019 to 2021?
     2. What are the Major Pollutant emit component for the air pollution caused in Delhi?
     3. Which are the Cities that have highest number of pollutant emit?
     4. Affect of festivals like Diwali and Dussehra on the air pollution level.
     5. Is the pollution level less in winter months like January and February compared to November and December?
  
  # To find the answer, I have used the following tools 🛠️:
  ![Tools Used](https://raw.githubusercontent.com/GokulArumugam/End-to-End-Data-Analyst-Project/main/Air%20pollution%20media/Tools.png)
  
  # Visuals from my Analysis:
  ![Glimpse 1](https://raw.githubusercontent.com/GokulArumugam/End-to-End-Data-Analyst-Project/main/Air%20pollution%20media/polluted%20cities.png)
  ![Glimpse 2](https://raw.githubusercontent.com/GokulArumugam/End-to-End-Data-Analyst-Project/main/Air%20pollution%20media/Comparision.png)
  ![Glimpse 3](https://raw.githubusercontent.com/GokulArumugam/End-to-End-Data-Analyst-Project/main/Air%20pollution%20media/States%20with%20max%20Pollutant%20emit.png)
  
  # Conclution:
  
In this analytical project, we have examined a number of different matrices in order to assess the data we have gathered and make wise judgments that will benefit the environment and atmosphere, improve air quality, and generally make the world a better place to live. It has been discovered that -
  
When counting, it appears that **Delhi has the highest number of pollutant emittance**; however, this may be an unfair comparison because, when considering the **surface area of Delhi to the population**, it has the highest count.
  
**Based on the data, it appears that each state contributes at a different level to different pollutant levels, which could be due to the geographical location of the states.**
  
Let's take the example of Delhi itself, based on the data the pollutant emittent `PM2.5` and `NO2` have the highest count. It's understandable given the large number of vehicles and pollutants emitted by the industries themselves.
  
Infact, the air pollution in **Delhi is so bad that, it has the total pollutant emit of Delhi is equal to rest of the six cities (Mumbai, Bengaluru, Kolkata, Hyderabad, Ghaziabad, Patna) combained.**
  
The fact that the pollution level rose from **55 to over 80 in just three to five days is a striking indication that firecrackers can significantly raise the air pollution level.**
  
According to the above line map, the average **air pollution level from November through February ranged from 50 to 70.**
  
But the months of **November and December are when air pollution reaches its worst levels.** And during the months of January and February, the amount of air pollution typically drops from 50 to 60 to 40 to 30.
  
# Documentation:

[High Level Documentation HLD](https://github.com/MitraKarthikeyan/End-to-End-Data-analysis-project/blob/main/Documentation/High-Level%20Design.pdf)

[WireFrame](https://github.com/MitraKarthikeyan/End-to-End-Data-analysis-project/blob/main/Documentation/WireFrame%20Air_Pollution.pdf)
  
[Project Architecture](https://github.com/MitraKarthikeyan/End-to-End-Data-analysis-project/blob/main/Documentation/Project%20Architecture.pdf)
  
# Feedback
If you have any feedback, please reach out to me via [LinkedIn](https://www.linkedin.com/in/mitra-karthikeyan-6269a8185/)
