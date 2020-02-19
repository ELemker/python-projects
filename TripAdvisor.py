# 
# Name: Evan Lemker
# Date: 2/3/2020
# Filename: TripAdvisor.py
# Description: #1 A function that calculates the cost of a trip and other information based on a given set of values.
               #2 A function that compares two vehicles that could be used for the trip and deciding which vehicle would be more cost effective.
               #3 A function that uses test cases to ensure the first function works correctly.
               #4 A function that uses test cases to ensure the second function works correctly.
#

# 1
def tripCostAndInfo(distanceKM, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):

# Calculating the number of nights you will need to stay in a hotel based on how long the trip will take
    timeOfTrip = distanceKM / (vehSpeedMPS * 3600 * .001) 
    
    if (timeOfTrip % 8) > 0:
        numHotelNights = int(timeOfTrip // 8)

    else:
        numHotelNights = int((timeOfTrip - .1) // 8)

    hotelCostOfTrip = numHotelNights * hotelCostPerNight
    
# Calculating the cost of gas for the trip based on values given
    gasCostOfTrip = (distanceKM / vehKPL) * gasCostPerLiter
    
# Calculating the cost of food for the trip based on values given and meals calculated
    numOfBreakfasts = numHotelNights
    numOfLunches = int(numHotelNights + ((timeOfTrip % 8) // 4)) 
    numOfDinners = numHotelNights

    foodCostOfTrip = (numOfBreakfasts * breakfastCostPerDay) + (numOfLunches * lunchCostPerDay) + (numOfDinners * dinnerCostPerDay)

# Calculating the total cost of the trip based on the seperate expenses
    totalCostOfTrip = hotelCostOfTrip + gasCostOfTrip + foodCostOfTrip

# Returning the calculated values to be used in part 2
    return totalCostOfTrip, gasCostOfTrip, numHotelNights, numOfLunches, foodCostOfTrip;


# 2
def compareVehiclesForTrip(distanceM, veh1Name, veh1SpeedMPH, veh1MPG, veh2Name, veh2SpeedMPH, veh2MPG, gasCostPerGallon, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):

# Converting the general given values to units that can be used by the first function 
    distanceKM = distanceM * 1.60934
    gasCostPerLiter = gasCostPerGallon * .264172

# Converting given values for vehicle 1 to units that can be used by the first function
    vehSpeedMPS = (veh1SpeedMPH * 1609.34) / 3600
    vehKPL = (veh1MPG / 3.78541) * 1.60934

# Calculating the info for vehicle 1 using the first function, then printing it to the screen
    veh1TotalCost, gasCostOfTrip, numHotelNights, numOfLunches, foodCostOfTrip = tripCostAndInfo(distanceKM, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight)

    print(str(distanceM) + " miles in vehicle '" + str(veh1Name) + "' will cost $" + str("%.2f" % veh1TotalCost) + ", including:" + "\n" + "   $" + str("%.2f" % (hotelCostPerNight * numHotelNights)) +
          " for " + str(numHotelNights) + " hotel nights, $" + str("%.2f" % gasCostOfTrip) + " for gas, and $" + str("%.2f" % foodCostOfTrip) + " for food (inluding " + str(numOfLunches) + " lunches)")

# Converting given values for vehicle 2 to units that can be used by the first function
    vehSpeedMPS = (veh2SpeedMPH * 1609.34) / 3600
    vehKPL = (veh2MPG / 3.78541) * 1.60934

# Calculating the info for vehicle 2 using the first function, then printing it to the screen
    veh2TotalCost, gasCostOfTrip, numHotelNights, numOfLunches, foodCostOfTrip = tripCostAndInfo(distanceKM, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight)   

    print(str(distanceM) + " miles in vehicle '" + str(veh2Name) + "' will cost $" + str("%.2f" % veh2TotalCost) + ", including:" + "\n" + "   $" + str("%.2f" % (hotelCostPerNight * numHotelNights)) +
          " for " + str(numHotelNights) + " hotel nights, $" + str("%.2f" % gasCostOfTrip) + " for gas, and $" + str("%.2f" % foodCostOfTrip) + " for food (inluding " + str(numOfLunches) + " lunches)")

# Printing a suggestion for which vehicle to use based on the info calculated for both the vehicles
    if (veh1TotalCost > veh2TotalCost):
        print("To save money, use '" + str(veh2Name) + "'")

    elif (veh1TotalCost < veh2TotalCost):
        print("To save money, use '" + str(veh1Name) + "'")

    else:
        print("Both vehicles will cost the same amount for a trip.")

    return

#3
def testQ1():

# test cases used to esnure that the tripCostAndInfo function works correctly
    print(tripCostAndInfo(500.0, 6.0, 100.0, 2.4, 20.0, 14.0, 18.0, 16.0))
    print("Cost should be: $162.00"  + "\n")
    print(tripCostAndInfo(1000.0, 1.0, 97.0, 3.8, 10.0, 25.0, 16.0, 20.0))
    print("Cost should be: $2478.17"  + "\n")
    print(tripCostAndInfo(1250.0, 8.0, 27.0, 1.2, 54.0, 13.0, 14.0, 18.0))
    print("Cost should be: $550.55"  + "\n")
    print(tripCostAndInfo(1500.0, 3.0, 7.0, 3.4, 49.0, 28.0, 15.0, 17.0))
    print("Cost should be: $2581.57"  + "\n")
    print(tripCostAndInfo(2000.0, 2.0, 84.0, 3.1, 30.0, 14.0, 22.0, 30.0))
    print("Cost should be: $3351.80"  + "\n")

    return

#4
def testQ2():

# test cases used to ensure that the compareVehicleForTrip function works correctly
    compareVehiclesForTrip(250.0, "Civic", 60.0, 50.0, "Wrangler", 35.0, 50.0, 2.1, 10.0, 25.0, 16.0, 20.0)
    print("Both should be equally efficient" + "\n")
    compareVehiclesForTrip(500.0, "Mustang", 50.0, 20.0, "Charger", 45.0, 30.0, 3.2, 20.0, 14.0, 18.0, 16.0)
    print("More efficient vehicle should be: 'Charger'" + "\n")
    compareVehiclesForTrip(750.0, "Accord", 70.0, 30.0, "Hellcat", 50.0, 35.0, 4.3, 30.0, 14.0, 22.0, 30.0)
    print("More efficient vehicle should be: 'Hellcat'" + "\n")
    compareVehiclesForTrip(1000.0, "Camry", 45.0, 40.0, "Outback", 65.0, 50.0, 2.5, 54.0, 13.0, 14.0, 18.0)
    print("More efficient vehicle should be: 'Outback'" + "\n")
    compareVehiclesForTrip(1250.0, "Corolla", 30.0, 35.0, "Explorer", 35.0, 25.0, 2.7, 49.0, 28.0, 15.0, 17.0)
    print("More efficient vehicle should be: 'Explorer'" + "\n")

    return
