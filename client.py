from googlesearch import search
import requests
from lxml.html import fromstring
import unicodecsv as csv

phrases = ["auto", "butu nuoma"]
csv_output = []
header = ["query", "url", "title", "metadata"];


def query_phrases(phrases_to_query):
    try:
        for phrase in phrases_to_query:
            print ("Querying phrase {0}".format(phrase))
            for item in query(phrase):
                    print("Result: {0}".format(item))
                    csv_output.append(create_an_output_from_request(phrase, item))
    except Exception as error:
        print("I cant query the item")
        print(error)


def query(phrase):
    for item in search(phrase, tld="lt", num=10, stop=10, pause=2):
        yield(item)


def create_an_output_from_request(phrase, url):
    r = requests.get(url)
    tree = fromstring(r.content.decode('utf-8'))
    return phrase, url, tree.findtext('.//title'), r.headers


def write_to_csv(rows):
    with open('output_file.csv', 'wb') as out:
        try:
                csv_out = csv.writer(out)
                csv_out.writerow(header)
                csv_out.writerows(rows)
        except Exception as error:
            print("Unable to write to the file")
            print(error)


if __name__ == "__main__":
    query_phrases(phrases)
    write_to_csv(csv_output)
    print(csv_output)





