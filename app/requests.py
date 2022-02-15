from .models import Quote
import urllib.request, json

link = 'http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    '''
    '''
    url = link
    
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    quote_details=[]

    author = data.get('author')
    text = data.get('quote')

    new_quote = Quote(author,text)
    quote_details.append(new_quote)

    return quote_details