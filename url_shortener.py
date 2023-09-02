from pyshorteners import *
url = input("Enter the original link : ")
print("Shortened link is : ",Shortener().tinyurl.short(url))