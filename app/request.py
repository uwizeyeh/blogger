from .models import Quote
import urllib.request,json
from app import app



base_url=app.config['QUOTE_API_BASE_URL']

def configure_request(app):
    global base_url
   

def get_quote():
    '''
    function that gets the json response to url request
    '''
    get_movies_url = base_url

    with urllib.request.urlopen(get_movies_url) as url:
        get_quote_data=url.read()
        print 
        get_quote_response=json.loads(get_quote_data)

        quote_objects= None

        if get_quote_response:
            id=get_quote_response.get('id')
            author=get_quote_response.get('author')
            quote=get_quote_response.get('quote')


        
    return quote_objects    
# def get_movies(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_movies_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_movies_url) as url:
#         get_movies_data = url.read()
#         get_movies_response = json.loads(get_movies_data)

#         movie_results = None

#         if get_movies_response['results']:
#             movie_results_list = get_movies_response['results']
#             movie_results = process_results(movie_results_list)


#     return movie_results