import requests

GITHUB_API = 'https://api.github.com'
REPO_SEARCH = GITHUB_API + '/search/repositories'


def search_repositories(query):
    search_params = {
        'q': query
    }
    search_response = requests.get(REPO_SEARCH, params=search_params)
    return search_response.json()

def get_response(query):
    response = ''
    if query is 'Natalie':
        response = 'She is the biggest brat in the world!'
    elif query is 'Olivia':
        response = 'She is such a sweetheart!'
    elif query is 'Sarah':
        response = 'I plead the fifth.'
    elif query is 'Ryan':
        response = 'He is the best dad and husband ever!'
    else:
        response = "I'm sorry I don't know them, I couldn't say."
    return response