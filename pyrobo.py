import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()

    print("Welcome to robo speaker, please type what you want me to speak. Type q to exit. Type s for settings.")
    engine.say("Welcome to robo speaker, please type what you want me to speak")
    engine.runAndWait()

    def change_rate():
        rate = engine.getProperty('rate')
        print("Type a new rate or leave blank")
        while True:
            print(f"The current rate is : {rate}")
            try:
                new_rate = int(input("New rate : "))
                if new_rate != "":
                    engine.setProperty("rate", new_rate)
                    print("Rate successfully changed to : " + str(new_rate))
                    engine.runAndWait()
                    pass
                    break
                else:
                    pass
            except ValueError:
                print("Rate must be a number, not alpabets")

    def change_volume():
        volume = engine.getProperty("volume")
        print("Type to set a new volume between 0.0 to 1.0 or leave blank")
        while True:
            print(f"The current volume is : {volume}")
            try:
                new_volume = float(input("Volume : "))
                if new_volume != "" and new_volume >= 0.0 and new_volume <= 1.0:
                    engine.setProperty("volume", new_volume)
                    print("Volume successfully changed to : " + str(new_volume))
                    engine.runAndWait()
                    break
                elif new_volume == "":
                    break
                else:
                    print("Volume must be between 0.0 to 1.0")
                    pass
            except ValueError:
                print("Volume must be between 0.0 to 1.0, not alphabets")

    def current_active_voice():
    # Different function to get current voice because, by default it prints id not name
        current_voice_id = engine.getProperty('voice')
        voices = engine.getProperty('voices')
        for i in range(1, len(voices)):
            voice = voices[0]
            voice_name = voice.id
            if current_voice_id == voice_name:
                current_voice = voice.name
                print(f"The current voice is : {current_voice}")
        for i in range(1, len(voices)):
            voice = voices[1]
            voice_name = voice.id
            if current_voice_id == voice_name:
                current_voice = voice.name
                print(f"The current voice is : {current_voice}")

    def change_voice():
        current_active_voice()
        while True:
            gender = input("Select by typing Male or Female : ")
            voices = engine.getProperty('voices')
            if gender == 'Male' or gender == 'male':
                print("Voices Available :")
                voice_list = []
                for i in range(1,len(voices)):
                    voice = voices[0]
                    voice_name = voice.name
                    voice_id = voice.id
                    voice_list.append(voice_id)
                    print(f"{str(i)}. {voice_name}")
                while True:
                    try:
                        select_voice_number = int(input(f"Type the number to select a voice from 1 to {str(len(voice_list))} : "))
                        if select_voice_number > 0 and select_voice_number <= len(voice_list):
                            select_voice = voice_list[select_voice_number-1]
                            engine.setProperty("voice", select_voice)
                            engine.runAndWait()
                            print("Voice changed successfully")
                            break
                        else:
                            print(f"Please select and option between 1 and {str(len(voice_list))} :")
                    except ValueError:
                        print(f"The input should be a number between 1 and {str(len(voice_list))}, not alphabets")
                break
            elif gender == 'Female' or gender == 'female':
                print("Voices Available :")
                voice_list = []
                for i in range(1,len(voices)):
                    voice = voices[1]
                    voice_name = voice.name
                    voice_id = voice.id
                    voice_list.append(voice_id)
                    print(f"{str(i)}. {voice_name}")
                while True:
                    try:
                        select_voice_number = int(input(f"Type the number to select a voice from 1 to {str(len(voice_list))} : "))
                        if select_voice_number > 0 and select_voice_number <= len(voice_list):
                            select_voice = voice_list[select_voice_number-1]
                            engine.setProperty("voice", select_voice)
                            engine.runAndWait()
                            print("Voice changed successfully")
                            break
                        else:
                            print(f"Please select and option between 1 and {str(len(voice_list))} :")
                    except ValueError:
                        print(f"The input should be a number between 1 and {str(len(voice_list))}, not alphabets")
                break
            else:
                print("Invalid option")
                pass

    def settings():
        while True:
            option = input("select an option (rate, voice, volume, type q to exit settings) : ")
            if option == "rate":
                change_rate()
            elif option == "voice":
                change_voice()
            elif option == "volume":
                change_volume()
            elif option == "q":
                start_robo()
                break
            else:
                print("Unknown option, please try again")

    def start_robo():
        while True:
            text = input("Text : ")
            if text ==  "q":
                engine.setProperty('rate', 180)
                engine.setProperty('volume', 1)
                engine.say("Thank you for using robo speaker.")
                engine.runAndWait()
                break
            elif text == "s":
                settings()
                break
            engine.say(text)
            engine.runAndWait()

    start_robo()