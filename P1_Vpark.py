#"*******************************Vpark-Vehicle Parking Management***********************"

#"*************************************Initial Inputs First Time***********************************"

Car_input = int(input("please Enter Total Car Parking Spaces:  "))
C_park = []
for c in range(Car_input):
     C_park.append(c+1)
print ('Car parking Spaces:', C_park, sep= ' ')

Mbike_input = int (input("please Enter Total Motorbike Parking Spaces: "))
M_park = []
for b in range(Mbike_input):
     M_park.append(b+1)
print ('Motorbike parking Space:', M_park, sep= '')

Car_Charge = input("please Enter Car Parking Chrge/Hour:  ")
Bike_Charge = input("please Enter Bike Parking Charge/Hour:  ")

#**************************************Initial Input End ****************************************
#**************************************Vehicle Input*********************************************

