import pyshorteners

def Shortener(link):
    #creating projects
    short = pyshorteners.Shortener()
    short_link = short.tinyurl.short(link)
    return short_link

url = input("Enter url : ")
final = Shortener(url)
print(f"Shortened LInk is : {final}")

