import requests
import sys


def add_bib(key):
    bib = requests.get("http://dblp.org/rec/bib2/%s.bib" % (key,)).text.strip()

    with open('references.bib', 'a') as o:
        o.write('\n')
        o.write(bib)
        o.write('\n')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        title = ''
        for l in sys.stdin:
            l = l.strip()
            if not l:
                break
            title += (' ' + l)
    else:
        title = ' '.join(sys.argv[1:])

    result = requests.get(
        "http://dblp.org/search/publ/api",
        params={'q': title, 'format': 'json'}
    ).json()

    try:
        hits = result['result']['hits']['hit']
    except KeyError:
        print("No hits")
        sys.exit(1)

    target = 0

    if len(hits) != 1:
        print("Multiple hits:")
        for i, hit in enumerate(hits, 1):
            print(
                "[%d] %s, %s" % (i, hit["info"]["title"], hit["info"]["url"])
            )
        print("Which would you like me to add?")
        i = int(sys.stdin.readline().strip())
        target = i - 1
    add_bib(hits[target]["info"]["key"])
