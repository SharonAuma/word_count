import requests
kittens=requests.get("http://placekitten.com/")
print kittens.text[559:1000]
