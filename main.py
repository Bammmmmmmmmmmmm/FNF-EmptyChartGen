import json

songName = ""
def playerOneQuestion():
    print("What's the name of player1? (bf side)")
    response = ''
    while response.lower() == "":
        response = input("")
    return response.lower()
def playerTwoQuestion():
    print("What's the name of player2? (dad/enemy side)")
    response = ''
    while response.lower() ==  "":
        response = input("")
    return response.lower()
def gfVersionQuestion():
    print("What's the name of gf?")
    response = ''
    while response.lower() ==  "":
        response = input("")
    return response.lower()
def stageQuestion():
    print("What's the name of the stage?")
    response = ''
    while response.lower() ==  "":
        response = input("")
    return response.lower()
def stageQuestion():
    print("What's the name of the stage?")
    response = ''
    while response.lower() == "":
        response = input("")
    return response.lower()
def songQuestion():
    print("What's the name of the song?")
    response = ''
    while response == "":
        response = input("")
    return response
def scrollSpeedQuestion():
    response = ''
    while response ==  "":
        try:
            response = float(input("Set the scroll speed: "))
        except ValueError:
            print("This is not a number, try again.")
    return response
def bpmQuestion():
    response = ''
    while response ==  "":
        try:
            response = int(input("Set the BPM (Beats Per Minute): "))
        except ValueError:
            print("This is not a number, try again.")
    return response
def needsVoicesQuestion():
    print("Does the song need voices?")
    response = ''
    while response not in {"true", "false", "yes", "no", True, False}:
        response = input("Please enter yes or no: ")
        if response == "yes" or response == "true":
            response =  True
        elif response == "no" or response == "false":
            response = False
    return response
def saveFileQuestion():
    print("Your empty chart is done! Save it now?")
    response = ''
    while response.lower() not in {"yes", "no"}:
        response = input("Please enter yes or no: ")
    return response.lower()


def noteRGBQuestion():
    print("Do you wanna disable the Note RGB Shader?")
    response = ''
    while response not in {"true", "false", "yes", "no", True, False}:
        response = input("Please enter yes or no: ")
        if response == "yes" or response == "true":
            response =  True
        elif response == "no" or response == "false":
            response = False
    return response


songName = songQuestion()
exportSongName = songName.lower()


    chart = {
    "song": {
        "player2": playerTwoQuestion(),
        "player1": playerOneQuestion(),
        "gfVersion": gfVersionQuestion(),
        "stage": stageQuestion(),
        "speed": scrollSpeedQuestion(),
        "needsVoices": needsVoicesQuestion(),
        "sectionLengths": [],
        "song": songName,
        "notes": [],
        "bpm": bpmQuestion(),
        "sections": 0,
        "validScore": True,
        "disableNoteRGB": noteRGBQustion()
        }
    }
if saveFileQuestion() == "yes":
    with open(f'{exportSongName}.json', 'w') as outfile:
        json.dump(chart, outfile)

