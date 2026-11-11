import requests
    
    
    
req = "https://api.chucknorris.io/jokes/random"
 
resp = requests.get (req) .json()
print (resp ['value'] )