## Data Visualization Final Project - Mapping Gentrification in NYC

### Team Members:
Gerardo Rodríguez (grv232)  
Julián Ferreiro (jif245)

![alt text](https://lh4.googleusercontent.com/-9UEy9CyEAaE/U7rAhlyPoeI/AAAAAAAABoY/IqaH8FCVZIs/s618/unnamed-001.jpg)


### Objectives of the project:
Gentrification in cities refers to the process where low income groups are displaced and replaced by higher income groups. 
This constitutes a problem because this lower income groups then need to incur in higher cost both when searching a new home and also for being relocated to areas that have less access to jobs or that have less facilities nearby.


### Data set involves
The map was build using an index of gentrification developed by Karen Chapple.
This index created different categories of gentrification risk using data available in the American Community Survey Census.
This information was at the census tract level. We use the platform Carto to perferom a spatial join between the census tract and a shapefile of NYC neighborhoods. 

Since census tract is highly granular level, it was decided to aggregate the data to neighborhood. 
The neighbourhood level is more meaningful to a policy maker: it constitues a category that is common knowledge for newyorkers and is what is used to analyze political variables like PlanNYC projects, voting results, etc.

### Visualization Design Choices
We use a cloropeth of NYC neighborhoods colored by the percentage of census tract of each category.
Due our technicall limiations and inabilities we couldn't create a deep analyzis tools, like showing the exact percentage when clicking on a nieghborhood or showing this same map for different years of the census. 

Originally we wanted to given a click on a neighborhood in the map, create a visualization with the distribution of the categories inside that neighbourhood. We couldn't achieve this. The python code that uses altair is in this folder.  

### Outcome and Evaluation
This will help visualize which neighbourhoods are at risk and which ones aren't. 
Since this index was not yet validated, it will help researchers to look for discrepancies with the index and ground thruth. If a neighborhood is shown to have an ongoing gentrification with the index but this is not correlated with field data, researchers will be able to adjust the index. 

The tool will also help to quickly assess policy or evaluate risk of applying a new one. Although we don't believe the index is perfect, it can help make better informed decisions to where to prioritize different type of developments such as an affordable housing policy, a PlanNYC project, etc. 


Link to blocks: https://bl.ocks.org/geeroovaa/4318e74922f5553f1a2cf9f7dd06338f
