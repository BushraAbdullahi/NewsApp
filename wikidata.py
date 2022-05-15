# pip3 install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

citiesquery = """#Largest cities of the world
#defaultView:BubbleChart
SELECT DISTINCT ?cityLabel ?population ?gps
WHERE
{
  ?city wdt:P31/wdt:P279* wd:Q515 .
  ?city wdt:P1082 ?population .
  ?city wdt:P625 ?gps .
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY DESC(?population) LIMIT 10000"""


def splitGps(value):
  value = value.replace("Point(","").replace(")","")
  value = value.split()
  lng = float(value[0])
  lat = float(value[1])
  return [lat,lng]


def sparql_to_city(sparqlcity):
    # parse the coordinates
    return {
        "name" : sparqlcity["cityLabel"]["value"],
        "population" : int(sparqlcity["population"]["value"]),
        "location" : splitGps(sparqlcity["gps"]["value"])

    }

def get_cities():
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(citiesquery)
    sparql.setReturnFormat(JSON)
    #the array below is the data in sample.json
    sparqlcities = sparql.query().convert()["results"]["bindings"]
    # list comprehension. 
    cities = [sparql_to_city(sparqlcity) for sparqlcity in sparqlcities]
    #cities = cities.sort(key = lambda x: x["population"])
    return cities

