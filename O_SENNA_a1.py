import pandas as df

#----------------------------------------PART ONE NO CSV FILE---------------------
#-----------------------------------------------------------------------------------

MyObject =	{
  "id": [0,1,2,3,4,4,5,6,7,8],
  "age": [21,22,23,24,25,25,26,27,"28",29],
  "height": [180,170,None,175,190,190,195,200,205,210],     #Reason for None is because my DataFrame could not read two commas as the value is empty
  "weight":[70,65,"80",75,90,90,95,100,105,110]
}

#----------------clean Data------------------------

results = df.DataFrame(MyObject)

##Drop the id colum since we will have one autometically
results.drop(['id'], inplace=True, axis=1)

##drop rows with an empty spaces
results.dropna(inplace=True)

##fix row 8 by removing inverted comma
results.loc[8, 'age'] = 28

##drop duplicate values
results.drop_duplicates(inplace=True)

##reset our index
results.reset_index(drop=True, inplace=True)
print(results)



##--------------------------MEAN, MEDIAN AND SD---------------------

def summary_statistics(dataframe,column_name):
    count = 0
    temp = 0
    
    for i in dataframe[column_name]:    #go over every value of the weight list in the object
        count = count + 1               #Count every value of the loop
        temp = temp + int(i)            #temp will hold and every value of the loop
        # print(i)
    
    #temp will be divided by the count to get the mean value
    mean = temp / count
    print("\nWeight \n------------------------")
    print("Mean: ", mean)
    
    count = 0           #reset count

    getDigits = dataframe[column_name]  #assign the weight List to the getDigits
    values = getDigits[3:5]             #Assign the two middle values to a variable 'values'
    for k in values:                    #Go to every values in the variable 'values'
        count = count + int(k)          #hold the 2 values which is the 2 middle values and add them
    median = count / 2                  #Divide count values by 2 to get the median value
    print("Median: ", median)
    
    count = 0           #reset count and temp to 0
    temp = 0
    
    for j in dataframe[column_name]:    #go over every value of the weight list in the object
        count = ((int(j) - mean) ** 2)  #Subtract each value of the loop by mean and square them by 2
        #hold count values and add them together
        temp = temp + count
        # print(count)

    # print(sum)
    standard_Devi = (temp / count - 1)  #divide temp value by count value and subtract by 1 to get the Standard Deviation
    print("Standard Deviation: ", standard_Devi)

summary_statistics(results,"weight")





#----------------------------------------PART TWO WITH CSV FILE---------------------
#-----------------------------------------------------------------------------------

import pandas as pd

#----------------clean Data------------------------


# Open the CSV file and declare by sep that semi-colon will be the separator
df = pd.read_csv('data.csv', sep=';')

##Drop the id colum since we will have one autometically
df.drop(['id'], inplace=True, axis=1)

##drop rows with an empty spaces
df.dropna(inplace=True)

##fix row 8 by removing inverted comma
df.loc[8, 'age'] = 28

##drop duplicate values
df.drop_duplicates(inplace=True)

##reset our index
df.reset_index(drop=True, inplace=True)
#print("\n",df)

def summary_statistics2(dataframe,column_name):
    count = 0
    temp = 0
    
    for i in dataframe[column_name]:
        count = count + 1
        temp = temp + int(i)
        # print(i)
    mean = temp / count
    print("\nWeight \n------------------------")
    print("Mean: ", mean)
    
    count = 0

    getDigits = dataframe[column_name]
    values = getDigits[3:5]
    for k in values:
        count = count + int(k)
    median = count / 2
    print("Median: ", median)
    
    count = 0
    temp = 0
    
    for j in dataframe[column_name]:
        count = ((int(j) - mean) ** 2)
        temp = temp + count
        # print(count)

    # print(sum)
    standard_Devi = (temp / count - 1)
    print("Standard Deviation: ", standard_Devi)

#summary_statistics2(df,"weight")