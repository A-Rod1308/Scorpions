import http.client
import re
import json

def movieSearch(searchString):
    conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d"
        }

    conn.request("GET", "/?page=1&r=json&s="+searchString, headers=headers)

    res = conn.getresponse()
    data = res.read()
    dataDecoded = json.loads(data)
    
    theResponse = addDetails(dataDecoded)

    return theResponse

def addDetails(baseDict):
    length = len(baseDict['Search'])
    for index in range(length):
        baseDict['Search'][index]['details'] = idSearch(baseDict['Search'][index]['imdbID'])
    return baseDict


def idSearch(id):
    conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d"
        }

    conn.request("GET", "/?i="+id+"&r=json", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data)

def formatSearch(searchS):
    import re
    searchS = re.sub('[^0-9a-zA-Z]+', ' ', searchS)
    searchS.replace(" ", "%20", -1)
    return searchS

#
def leagueGameSearch(searchString):
    conn = http.client.HTTPSConnection("api-pandascore.p.rapidapi.com")

    headers = {
    'x-rapidapi-host': "api-pandascore.p.rapidapi.com",
    'x-rapidapi-key': "0a56ecd8a4msh557dc3387a3c8b2p18a8a5jsnda85dc032912"
    }

    conn.request("GET", "/tournaments/%7Bid%7D.json", headers=headers)

    res = conn.getresponse()
    data = res.read()

    dataDecoded = json.loads(data)
    
    theResponse = addDetails(dataDecoded)

    return theResponse

