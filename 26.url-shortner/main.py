import pyshorteners

# this is a supermini project but could be a useful feature for automation

s = pyshorteners.Shortener()

url=input('Enter the url that you want to shortern: ')

print(s.tinyurl.short(url))

# you can use multiple url shortners to shortern your url 

# checkout the documentation here : https://pyshorteners.readthedocs.io/en/latest/