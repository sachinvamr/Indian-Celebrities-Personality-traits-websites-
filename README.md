# Indian-Celebrities-Personality-traits-websites-
Search bio in websites and use that bio to predict Personality traits of Celebrity

websites used:
https://en.wikipedia.org/wiki/List_of_Indian_film_actresses
https://en.wikipedia.org/wiki/List_of_Indian_film_actors
https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1
https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=2

Order to run:
Indian_celebrities.py
celebrities2.py
combine_and_predict.py

Columns description in "celebrities_personalityTraits_dataset.csv" 
'Names' :Name of the celebrity
'bio' :to predict Personality traits
'Images' :Images of the celebrity in numpy array form (can be converted in to image by 'cv2.imdecode(image, cv2.IMREAD_COLOR)' in python)
Rest of the columns are the characteristics: 1) columns without 'raw' appended at last is the data comparing with a sample population
                                             2) columns with 'raw' appended at last is the data without comparing with a sample population

