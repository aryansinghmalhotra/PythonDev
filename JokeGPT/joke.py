import requests

def get_joke(category, flag):
    response = requests.get(f'https://v2.jokeapi.dev/joke/{category}?blacklistFlags={flag}')
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            return data['joke']
        elif data['type'] == 'twopart':
            return f"{data['setup']} - {data['delivery']}"
    else:
        return "Couldn't retrieve a joke"

#print(get_joke("Programming", "explicit"))

def search_joke(term):
    response = requests.get(f'https://v2.jokeapi.dev/joke/Any?term={term}')
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            return data['joke']
        elif data['type'] == 'twopart':
            return f"{data['setup']} - {data['delivery']}"
        else:
            return "No jokes found"
    else:
        return "Couldn't retrieve a joke"


def get_joke_by_language(category, language):
    response = requests.get(f'https://v2.jokeapi.dev/joke/{category}?lang={language}')
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            return data['joke']
        elif data['type'] == 'twopart':
            return f"{data['setup']} - {data['delivery']}"
    else:
        return "Couldn't retrieve a joke"

print(get_joke_by_language("Programming", "en"))

