#the function loadCSVData is used to load information from the inputted csv filename. 
def loadCSVData(file_Name):

    openFile = open(file_Name, "r")  #the command "open" is used to open the file that is inputted by the user in read only mode.
    readlinesFile = openFile.readlines()    #this reads the lines from the user inputted csv file and stores it in this variable.
    openFile.close()    #this closes the user inputted csv file
    count = 0   #index counter to count the lines in the file inputted by the user 
    fileInfo = []   # this array is initialized to store the data from the inputted file.

    for line in readlinesFile:  #the for loop is used to format all information read in readlinesFile. The loop[ runs until there are lines in the file
        fileInfo.append(readlinesFile[count].upper().rstrip().split(","))   #converting the information into upper case and storing as sentences by splitting the lines at the character "," and then removing ","
        count = count + 1 # incrementing the counter and counting the lines

    fileInfo.pop(0) #this removes the header (as we are popping index(0))
    return fileInfo #returning the 


def getInformation(selectedCountry, topUniFileName, capitalsFileName):

    topUniInfo = delCertain([7,6,5,4], loadCSVData(topUniFileName)) #obtaining raw information and eliminating the unrequired data.
    capitalInfo = delCertain([4,3,2], loadCSVData(capitalsFileName))
    result = joinLists(topUniInfo, capitalInfo)#combining the 2 list we obtained using the function loadCSVData.
    
    selectedCountry = selectedCountry.upper()   #converting user selected country to uppercase so that we can handle the data .
    
    #topuni data for international and national unis.
    #topuniintindex -> top university international index
    #topuninatindex -> top university national index
    topUniIntIndex = TopIntUni(selectedCountry, result)
    topUniNatIndex = TopNatUni(selectedCountry, result)
    
    topUniIntInfo = result[topUniIntIndex]
    topUniNatInfo = result[topUniNatIndex]
    
    outputFile = open("output.txt", "w")    #opening the text file given in write mode 
    
    #opening and then writing information in the output.txtfile as asked
    outputFile.write("Total number of universities => %d\n" %(len(topUniInfo)))
    outputFile.write("Available countries => " + allCountries(capitalInfo) + "\n")

    outputFile.write("Available continents => " + allContinents(capitalInfo) + "\n")
    outputFile.write("At international rank => %s the university name is => %s\n" %(topUniIntIndex+1,topUniIntInfo[1]))

    outputFile.write("At national rank => %s the university name is => %s\n" %(topUniNatInfo[3], topUniNatInfo[1]))
    outputFile.write("The average score => {}%\n".format(scoreAverage(selectedCountry, result)))

    outputFile.write("The relative score to the top university in {} is => ({}/{}) x 100% = {:.2f}%\n".format(topUniIntInfo[6], scoreAverage(selectedCountry, result), getHighScore(topUniIntInfo[6], result), ((scoreAverage(selectedCountry, result)/getHighScore(topUniIntInfo[6], result))*100)))
    outputFile.write("The capital is => %s\n" %(topUniIntInfo[5]))
    outputFile.write("The universities that contain the capital name =>%s" %(uniCapitalString(topUniIntInfo[5], result)))

    outputFile.close()#closing the output.txtfile.

def TopIntUni(selectedCountry, data):
    for i in range(len(data)):  #go through each uni from top to bottom
        if(data[i][2] == selectedCountry):  #return index of first match of countries
            return i

def TopNatUni(selectedCountry, data):
    for i in range(len(data)):  #go through each uni
        if(data[i][3] == "1" and data[i][2] == selectedCountry):    #if national rank is 1 and country names match
            return i

        
def delCertain(allIndex, rawInfo):  #the function delCertain removes certain elements.
    temporaryList = ["temp"]    #this is a temporary variable.

    for i in range(len(rawInfo)):#this goes through each sub list in rawinfo.
        temporaryList = rawInfo[i]#this assigns element to the temporary variable "temporaryList"
        for j in range(len(allIndex)):#this removes all indexes
            del temporaryList[allIndex[j]]

        rawInfo[i] = temporaryList #

    return rawInfo #returning the rawInfo array with the elements stored in the temporaryList

def joinLists(list1, list2):
    count = 1
    for i in range(len(list2)): #going through each country
        for j in range(len(list1)): #going through each university
            if(list2[i][0] == list1[j][2]): #check if both countries match
                list1[j].append(list2[i][1])
                list1[j].append(list2[i][2]) #add capitals and continents

    return list1

def uniCapitalString(capital, data):
    unisCaptlString = ""
    count = 1
    for i in range(len(data)):   #loop through each university
        if(capital in data[i][1]):
            unisCaptlString = unisCaptlString + "\n\t#{} {}".format(count, data[i][1])  #formatting the string
            count = count + 1 #incrementing the counter
    return unisCaptlString

def allContinents(listOfCapitals):
    continents = [] #an array to store the continents
    for i in range(len(listOfCapitals)):    #loop through each country
        if(continents.count(listOfCapitals[i][2]) == 0):  #if continent not in continents list, add it to list
            continents.append(listOfCapitals[i][2]) #appending the continents that were not in the list

    continentListString = continents[0] #turn list to string
    for i in range(len(continents)-1):
        continentListString = continentListString + ", " + continents[i+1]  #adding continents to string

    return continentListString

def allCountries(listOfCapitals):
    countries = listOfCapitals[0][0] #to avoid ", " in the end
    for i in range(len(listOfCapitals)-1):  #loop through each country from second to last
        countries = countries + ", " + listOfCapitals[i+1][0]   #adding countries to string

    return countries

def getHighScore(selectedContinent, data):
    highScore = float(0)
    for i in range(len(data)):  #find the highest score in the continent
        if(data[i][6] == selectedContinent):    #check if continent matches
            if(highScore < float(data[i][4])):
                highScore = float(data[i][4])   #if the highScore is less than the data stored at the array, then store the higher value in the variable 

    return highScore

def scoreAverage(selectedCountry, data):
    finalScore = float(0)
    totUnis = 0
    for i in range(len(data)):  #loop through each university
        if (data[i][2] == selectedCountry): #check if countries match
            finalScore = finalScore + float(data[i][4])  #add to total score and total unis
            totUnis = totUnis + 1 #incrementing value

    return round((finalScore/totUnis), 2)    #return rounded average
