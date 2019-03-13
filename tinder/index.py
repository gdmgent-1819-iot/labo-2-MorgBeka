from sense_hat import SenseHat
import json
import requests
import sys

sense = SenseHat()

print('test')

namePerson = ' '

def personLikeOrDislike(newPerson):
    with open('data.json', "a") as json_file:
        json_file.write("{}\n".format(json.dumps(newPerson)))

    loadPerson()



                                      
def loadMessage(getFirstName, getAge):
    sense.show_message(getFirstName, text_colour = (255, 50, 50))
    sense.show_message(getAge, text_colour = ( 0, 255, 0)) 

    event = sense.stick.wait_for_event()
    if event.direction == "left":
        print('like')
        newPerson={'name; ': getFirstName, 'age;': getAge, 'chose; ': 'like'}
        personLikeOrDislike(newPerson) 

    elif event.direction == "right":
        print('dislike')
        newPerson={'name; ': getFirstName, 'age;': getAge, 'chose; ': 'dislike'}
        personLikeOrDislike(newPerson) 
    

def loadPerson():
    loadData = requests.get('https://randomuser.me/api/').json()
    getName = loadData['results'][0]['name']
    getFirstName = getName['first']
    print(getFirstName)
    getAge = loadData['results'][0]['dob']['age']
    

    loadMessage(getFirstName, str(getAge))
   
loadPerson()




