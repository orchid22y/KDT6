from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


try:
    html=urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked!') #정상인경우