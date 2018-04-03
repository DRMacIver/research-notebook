import bibtexparser
import re

if __name__ == '__main__':
    with open('references.bib') as bibtex:
        db = bibtexparser.load(bibtex)

    with open('reflist.tex', 'w') as o:
        o.write('\\begin{itemize}\n')
        for entry in db.entries:
            if entry['ENTRYTYPE'] == 'proceedings':
                continue
            title = re.sub(r" +", " ", entry['title'].replace("\n", " "))
            o.write('\\item ``%s\'\'\\cite{%s}\n' % (
                title, entry['ID']
            ))
        o.write('\\end{itemize}\n')
