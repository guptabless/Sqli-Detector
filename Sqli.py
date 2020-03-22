import urllib.request

input_url = input("please enter url where we have to check sql injection")
print(input_url)

sql_url = input_url + "12'" + "&submit=Search"
print(sql_url)

resp = urllib.request.urlopen(sql_url)
body = resp.read()

fullbody = body.decode('utf-8')

if "You have an error in your SQL syntax" in fullbody:
    print("vulnerable to sql injection")
else:
    print("not vulnerable to sql injection")
