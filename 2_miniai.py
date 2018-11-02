
import numpy as np
#create an array of all 1 train stations
one_train_stations = [242,238,231,225,215,207,191,181,168,157,145,137,125,116,110,103,96,86,79,72,66,59,50,42,34,28,23,18,14]
#grab user input
user_street = int (input ("What street are you on? (just type in the name eg: '86')"))

#function that calculates the distance between the user and each station
def calculate_distance (staions):
    distances = []
    for station in staions:
        #caluclulate the distance from user to every station in stations
        distance = user_street - station
        #take the absolute value (to avoid negative distances)
        distance = np.abs(distance)
        #add the distance to an array
        distances.append(distance)
    #sort the array of distances from lowest to highest
    distances = sorted(distances)
    #return array
    return distances

#function that figures out the closest station based on the distances
def figure_out_which_station(distance):
    #if the station distance + the user location is in the one_train_stations array, return the station
    if user_street + shortest_distance in one_train_stations:
        return str(user_street + shortest_distance)
    #otherwise,  distance - the user location is in the one_train_stations array. After that, return the station
    else:
        return str(user_street - shortest_distance)

#get shortest distance from station (first element in sorted array)
shortest_distance = calculate_distance(one_train_stations)[0]
#print everything out, calling the figure_out_which_station function
print ("The closest staion is on " + figure_out_which_station(shortest_distance) + " street, which is " + str(shortest_distance)+" blocks away")
