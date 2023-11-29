import requests

def get_movies_by_genre(genre):
    url = "https://moviesdatabase.p.rapidapi.com/titles"

    headers = {
        'X-RapidAPI-Key': "06f851cc76mshbf06dba42430d31p12f8e4jsn27c1e5a98b94",
        'X-RapidAPI-Host': "moviesdatabase.p.rapidapi.com"
    }

    params = {
        "genre": genre,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None



