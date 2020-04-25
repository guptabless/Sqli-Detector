import urllib.request
import bcolors

print("-----------------------------------------------")
print("sqlInjection")
print("Code By : NG")
print("Usage: python sqlinjection.py and then follow the instructions")

print("-----------------------------------------------")
input_url = input(bcolors.BLUE + "please enter the endpoint where we have to check sql injection")
print("URL should have to start with http and https")
print(bcolors.BITALIC)

sql_url = input_url + "'"

resp = urllib.request.urlopen(sql_url)
body = resp.read()

fullbody = body.decode('utf-8')
if "You have an error in your SQL syntax" in fullbody:
    print(bcolors.ERRMSG + "vulnerable to sql injection")
else:
    print(bcolors.OKMSG + "Not vulnerable to sql injection")

