#python
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" not in counties:
    print ("El Paso is not the list of counties.")
else:
    print("El Paso is in the list of coutnies")
    #testing if two conditions are true
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of coutnies.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")
#output from the list counties
for county in counties:
    print(county)

numbers = [0,1,2,3,4,5]
for num in numbers:
    print(num)
for i in range(len(counties)):
    print(counties[i])
#using voting data - dictionary to print data
