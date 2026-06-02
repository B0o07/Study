import time

rain = input("Is raining? ").lower()

if(rain == "yes"):
    umbrella = input("Do you have an umbrella? ")

    if umbrella.lower() == "yes":
        print("Go outside")
    
    elif umbrella.lower() == "no":
        print("Wait the rain to pass.")

        while rain.lower() != "no":
            rain = input("Is it still raining? ")
            time.sleep(1)
        
        print("Go outside!")
else:
    print("Go outside!")