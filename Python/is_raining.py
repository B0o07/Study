import time
out = "Go outside!"

while True:
    rain = input("Is raining? ").lower().strip()

    if rain == "yes" or rain == "no":
        break
    
    else:
        print("Answer with Yes or No. ")
        time.sleep(1)

if(rain == "yes"):
    umbrella = input("Do you have an umbrella? ")

    if umbrella.lower() == "yes":
            print(out)
            
    elif umbrella.lower() == "no":
        print("Wait the rain to pass.")

        while rain.lower() != "no":
            rain = input("Is it still raining? ")
            time.sleep(1)
            
        print(out)
else:
    print(out)