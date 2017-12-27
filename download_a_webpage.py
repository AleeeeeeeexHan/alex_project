from urllib.request import FancyURLopener

url  = "https://www.chinahighlights.com/travelguide/chinese-food/eight-chinese-dishes.htm"

def get_webpage(url):

    class AppURLopener(FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open(url)

    data = response.read()
    text = data.decode("utf-8")
    return text



text = get_webpage(url)

with open('html_text.txt', 'w') as f:
    f.write(text)