from passengerClass import *


passengerList = open('TitanicPassengers.txt','r')

titanicPassengers = []

for passenger in passengerList:
    
    person = passenger.split(',')
    cabin = person[0]
    age = float(person[1])
    gender = person[2]
    survived = person[3]
    lastname = person[4]
    firstname = person[5]
    p1 = Passenger(cabin,age,gender,survived,lastname,firstname)
    titanicPassengers += [p1]
   
   
   
total = 0
howMany = 0
for i in titanicPassengers:
    member = titanicPassengers[0]
    age = i.getAge()
    total = total + age
    howMany +=1
avgAge = round(total/howMany,2)



OneDeaths = 0
OneSurvives = 0
OneTotal = 0

TwoDeaths = 0
TwoSurvives = 0
TwoTotal = 0

ThreeDeaths = 0
ThreeSurvives = 0
ThreeTotal = 0
for member in titanicPassengers:
    cabin = member.getCabin()
    
    if cabin == '1':
        if member.getSurvived() == '1':
            OneSurvives +=1
        else:
            OneDeaths +=1
        OneTotal +=1
    elif cabin == '2':
        if member.getSurvived() == '1':
            TwoSurvives +=1
        else:
            TwoDeaths +=1
        TwoTotal +=1
    elif cabin == '3':
        if member.getSurvived() == '1':
            ThreeSurvives +=1
        else:
            ThreeDeaths +=1
        ThreeTotal +=1
        
oneSurvivalRate = round(OneSurvives/OneTotal*100,2)
twoSurvivalRate = round(TwoSurvives/TwoTotal*100,2)
threeSurvivalRate = round(ThreeSurvives/ThreeTotal*100,2)



passengerList.close()


