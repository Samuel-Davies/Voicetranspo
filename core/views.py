from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as connector
import speech_recognition
import pyttsx3

# Create your views here.

def results(request):
    return render(request, 'account/results.html')




def main(request):
    if request.method == 'POST':
        #CREATE CONNECTION OBJECT TO THE DATABASE
        try:
            db1 = connector.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            database = "VoiceTranspo" 
            )
            print("Connection To Database Successful",end="\n\n")

        except connector.errors.ProgrammingError:
            print("Could Not Connect to Database")

        else:
            system_talk = pyttsx3.init()

            while True:
                system_talk.say("Where would you like to Go To? ") 
                system_talk.runAndWait()
                print(f"Where would you like to Go To? ", end= "  ")
                destination =  audio_text()
                system_talk.endLoop()

                print(f"Did you say?: {destination}")
                system_talk.say(f"Did you say {destination} ?")  
                system_talk.runAndWait()

                print("Yes or No ?")
                user_choice = audio_text()
                system_talk.endLoop()
                print(user_choice)

                if user_choice in ["no", "none", "nope"]:
                    continue
                elif user_choice in ["yes", "yeah"]:
                    break
                else:
                    continue

            while True: 
                #system_talk.endLoop()
                system_talk.say("What is your location? ")
                system_talk.runAndWait()
                print("What is your location? ", end= "  ")
                station =  audio_text()
                system_talk.endLoop()
                print(f"Did you say?: {station}")
                system_talk.say(f"Did you say {station} ?")  
                system_talk.runAndWait()

                print("Yes or No ?")
                user_choice = audio_text()
                system_talk.endLoop()
                #user_choice = input("(Y/N) = ").lower()
                print()
                if user_choice in ["no", "none", "nope"]:
                    continue
                elif user_choice in ["yes", "yeah"]:
                    break
                else:
                    continue


            default_query = """ SELECT station.name AS "FROM", destination.name AS "TO", time.departure AS  "DEPARTURE", 
                                time.arrival AS "ARRIVAL", vehicle.brand AS "VEHICLE BRAND", vehicle.type AS    "VEHICLE TYPE",
                                vehicle.capacity AS "VEHICLE CAPACITY", vehicle.color AS "VEHICLE COLOR"
                                FROM station
                                JOIN destination
                                ON station.destination_id = destination.id
                                JOIN time
                                ON station.time_id = time.id
                                JOIN vehicle
                                ON station.vehicle_id = vehicle.id
                            """

            # CREATE A CURSOR OBJECT TO NAVIGATE AND QUERY DATABASE
            mycursor = db1.cursor()

            # QUERY THE DATABASE
            mycursor.execute(f"{default_query}" + f"WHERE station.location = '{station}' AND destination.location   = '{destination}';")

            # STORE RESULT FROM DB IN VARIABLE
            result_set = mycursor.fetchall()

            columns = ["STATION", "DESTINATION", "DEPARTURE TIME", "ARRIVAL TIME", "VEHICLE BRAND", "VEHICLE  TYPE","VEHICLE CAPACITY","VEHICLE COLOR"]
            row_dict = {}
            result_list = []
            display_frontend = ""

           # Convert row_list into a List of Dictionaries in row_dict
            for i,row in enumerate(result_set):
                for j in range(len(columns)):
                    row_dict[columns[j]] = row[j]
                result_list.insert(i,row_dict)
                row_dict = {}

            # PRINT RESULTS
            for dic in result_list:
                for key,value in dic.items():
            
                    display_frontend += f"{key} = {value}\n"
            
                #print(display_frontend)
                #display_frontend = ""
                print()

            # Speak Results in First Row
            first_row = result_list[0]
            speak_first_row = f"""
            The available is station is {first_row['STATION']}. Your destination is {first_row['DESTINATION']} 
            The departure time is {first_row['DEPARTURE TIME']}am and the estimated arrival time is {first_row['ARRIVAL TIME']}am.
            """
            print(speak_first_row)
            system_talk.say(f"{speak_first_row}")
            system_talk.runAndWait()

            print("the result set is read out loud to user")
            system_talk.endLoop()   
             
            return render(request, 'account/results.html', {
                    
                    'frontendResults':display_frontend,

                })




        
# FUNCTION TO CAPTURE SPEECH AND CONVERT TO TEXT
def audio_text():
    
    recognizer = speech_recognition.Recognizer()
    try:
        #Open Audio Souce i.e Microphone
        with speech_recognition.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic,duration=0.05)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            final_text = text.lower()
            return final_text
    except Exception as e:
        print(f"Try Again, {e}")

if __name__ == "__main__":
    main()

