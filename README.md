# Indian-Celebrities-Personality-traits-websites-
Search bio in websites and use that bio to predict Personality traits of Celebrity

## Table of Contents
  * [Introduction](#general-info)
  * [Tecnologies](#technologies)
  * [Setup](#setup)
  * [Order of Running](#order-of-run)
  * [Status and Demo](#status)
  * [Columns description](#features--to-do)
 
### Introduction
It takes data from the mentioned websites and gives it a prediction and then creates an organized .csv file for their personality traits.

### Technologies
  - 100% python
#### websites used:
* [https://en.wikipedia.org/wiki/List_of_Indian_film_actresses](https://en.wikipedia.org/wiki/List_of_Indian_film_actresses)
* [https://en.wikipedia.org/wiki/List_of_Indian_film_actors](https://en.wikipedia.org/wiki/List_of_Indian_film_actors)
* [https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1](https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1)
* [https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=2](https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=2)

### Setup
```
  - Python IDE
  - install bs4, urllib.request,pandas, ibm_watson, ibm_cloud_sdk_core.authenticators, csv libraries
```

### Order of Running
  - Indian_celebrities.py
  - celebrities2.py
  - combine_and_predict.py
  
### Status and Demo
  - The project is completed and runnable. 
  - Created .csv file is uploaded as an example.

### Columns description in "celebrities_personalityTraits_dataset.csv"  

  - 'Names' :Name of the celebrity  
  - 'bio' :to predict Personality traits  
  - 'Images' :Images of the celebrity in numpy array form (can be converted in to image by 'cv2.imdecode(image, cv2.IMREAD_COLOR)' in python)  
  - Rest of the columns are the characteristics:
	  - a) columns without 'raw' appended at last is the data comparing with a sample population 
	  - b) columns with 'raw' appended at last is the data without comparing with a sample population
