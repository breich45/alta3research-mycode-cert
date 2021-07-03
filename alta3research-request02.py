#!/usr/bin/python3

import requests
import json

apiurl = "http://10.0.168.242:2224"

def main():
         # enter a loop condition with menu prompting
    while True:
        # initialize answer
        answer = ""
        while answer == "":
            print("""\n**** Welcome to Brent's Taproom ****
            1) See whats currently available on tap
            2) See what's in queue to go on next when a tap becomes available
            3) See what's in the suggestion box
            4) Make a suggestion!
            99) Exit""")

            answer = input("> ") # collect an answer for testing

        # testing the answer
        if answer in ["1", "2", "3", "4"]:
            if answer == "1":
                resp = requests.get(f"{apiurl}/ontap")
                for i in resp.json():
                    print(f"Tap Position: {i['Tap_position']}")
                    print(f"Name: {i['Name']}")
                    print(f"Description: {i['Description']}")
                    print()
                input("Press Enter to continue...")
            elif answer == "2":
                resp = requests.get(f"{apiurl}/comingsoon")
                for i in resp.json():
                    print(f"Name: {i['Name']}")
                    print(f"Description: {i['Description']}")
                    print()
                input("Press Enter to continue...")
            elif answer == "3":
                resp = requests.get(f"{apiurl}/suggestionbox")
                for i in resp.json():
                    print(f"Name: {i['Name']}")
                    print(f"suggestion: {i['suggestion']}")
                    print()
                input("Press Enter to continue...")
            elif answer == "4":
                myname = input("What's your name?: ")
                mysuggestion = input("What's your suggestion?: ")
                res = requests.post(f"{apiurl}/makesuggestion", json={"Name": myname, "suggestion" : mysuggestion})
            else:
                print("you didn't pick a valid number.")

        # user wants to exit
        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()
