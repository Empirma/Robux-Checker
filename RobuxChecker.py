import requests
import time

# Getting cookies
cookiesFile = open("cookies.txt", "r")
lnumber = 1

# Calculating Robux amount
robuxAmount = 0

# Going through cookies one by one
for cookie in cookiesFile:
    # Setting cookie
    r = requests.Session()
    r.cookies[".ROBLOSECURITY"] = cookie.rstrip("\n")

    # Checking if cookie is valid
    getUserInfo = r.get("https://users.roblox.com/v1/users/authenticated")
    if getUserInfo.status_code == 401:
        print("Invalid cookie in line number:", lnumber)
        lnumber += 1
    else:
        lnumber += 1
        # Getting userid
        userName, userID = getUserInfo.json()['name'], getUserInfo.json()['id']
        print("Username:", userName, "User ID:", userID); print("")
        # Getting Robux Amount
        getRobuxInfo = r.get(f"https://economy.roblox.com/v1/users/{userID}/currency")
        print(f"Robux Amount: {getRobuxInfo.json()['robux']}"); print("")
        robuxAmount += getRobuxInfo.json()['robux']

print(f"Robux amount in total: {robuxAmount}")