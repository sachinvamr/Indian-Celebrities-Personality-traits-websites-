# Indian-Celebrities-Personality-traits-websites-
Search bio in websites and use that bio to predict Personality traits of Celebrity

websites used:
 https://en.wikipedia.org/wiki/List_of_Indian_film_actresses <br /> 
 https://en.wikipedia.org/wiki/List_of_Indian_film_actors <br />
 https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1 <br />
 https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=2 <br />


Order to run:
1)Indian_celebrities.py <br />
2)celebrities2.py <br />
3)combine_and_predict.py <br />

Columns description in "celebrities_personalityTraits_dataset.csv" <br />
1)'Names' :Name of the celebrity <br />
2)'bio' :to predict Personality traits <br />
3)'Images' :Images of the celebrity in numpy array form (can be converted in to image by 'cv2.imdecode(image, cv2.IMREAD_COLOR)' in python) <br />
4)Rest of the columns are the characteristics: 1) columns without 'raw' appended at last is the data comparing with a sample population
                                             2) columns with 'raw' appended at last is the data without comparing with a sample                                                         population

