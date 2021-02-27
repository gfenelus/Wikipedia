import xml.etree.ElementTree as et
import wikitextparser as wtp
import re

file = 'wikiTest.xml'

ns = '{http://www.mediawiki.org/xml/export-0.10/}'

actorCounter = 0
pageCounter = 0

root = et.iterparse(file)
print('parsed.')

for ev, el in root:
    if el.tag == ns + 'title':
        title = el.text
        pageCounter += 1
    # if el.tag == ns + 'text' and 'Actor' in el.text:
    if el.tag == ns + 'text' and re.search(r'occupation \s* = \s*(?:\{{2})?(?:[\w*\|\s?])*(?:\*)?Actor', el.text):
        actorCounter += 1
        name = re.search(r'(?:\|?)name \s*=\s*(.*)', el.text)

        # print(el.text)
        parsedText = wtp.parse(el.text)
        templates = parsedText.templates
        for template in templates:
            if 'Infobox person' in template:
                # print(template)
                #                 TODO: use regex to pull out data needed for each actor
                name = re.findall(r'(?:\|?)name \s*=\s*(.*)', el.text)
                bdate_raw = re.findall(r'(?:\|?)birth_date \s*=.*\|(\d{4})\|(\d{1,2})\|(\d{1,2})', el.text)
                bdate = f"{bdate_raw[0][0]}/{bdate_raw[0][1]}/{bdate_raw[0][2]}"



        print("name: ", name[0])
        print("birthdate: ", bdate)

print("Actors found: ", actorCounter)
print("pages found: ", pageCounter)
