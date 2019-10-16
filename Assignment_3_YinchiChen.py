from textblob import TextBlob
from pprint import pprint
import pandas as pd
import os
os.getcwd()

male = open('/Users/yinchichen/Desktop/FE595/hw/Assignment_3/HE.txt', 'r')
female = open('/Users/yinchichen/Desktop/FE595/hw/Assignment_3/SHE.txt', 'r')
male = "".join(male)
female = "".join(female)
male_list = []
female_list = []

blob_male = TextBlob(male)
blob_female = TextBlob(female)

male_list.append([blob_male.sentiment.polarity, male])
female_list.append([blob_female.sentiment.polarity, female])


data_male = pd.DataFrame(male_list, columns=['Number', 'Sentence'])
data_male = data_male.sort_values(by="Number", ascending=False)

data_female = pd.DataFrame(female_list, columns=['Number', 'Sentence'])
data_female = data_female.sort_values(by="Number", ascending=False)

top_male = data_male.head(10)
bottom_male = data_male.tail(10)

top_female = data_female.head(10)
bottom_female = data_female.tail(10)

pprint(top_male)
pprint(bottom_male)
pprint(top_female)
pprint(bottom_female)