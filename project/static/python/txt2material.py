path = 'templates/'

bookNameDict = {
    'ICor': 'I Corinthians',
    'IICor': 'II Corinthians'
}

reverseBookNameDict = dict((v, k) for k, v in bookNameDict.items())

versePattern = r"([0-9]{1,2}):([0-9]{1,2})([A-z,':;()?.\n ]+)"

verseSymbols = [',',':',';','(',')','?','.']

import re
import json

materialview = {
    'ICor': {
        1: {
            1: ''
        },
        2: {
            1: ''
        }
    },
    'IICor': {
        1: {
            1: ''
        },
        2: {
            1: ''
        }
    }
}

material = dict()

words = list()

def getMaterial():
    for file in bookNameDict:
        material[file] = {} # Create section for book
        book = material[file]
        with open("QuizSite0.3/project/static/txt/" + file + ".txt", 'r') as file:
            text = file.read().replace('\n',' ')

        for verse in re.finditer(versePattern, text):
            if int(verse.group(2)) == 1:
                book[verse.group(1)] = [verse.group(3).strip()]
            elif verse.group(3).strip() != '':
                book[verse.group(1)].append(verse.group(3).strip())

            for word in verse.group(3).split(" "):
                # Remove punctuation
                # ,:;()?.
                for char in [',',':',';','(',')','?','.']:
                    word = word.replace(char, '')

                words.append(word.casefold())
    return book

getMaterial()

once =  ([word for word in words if words.count(word) == 1])
twice = ([word for word in words if words.count(word) == 2])


with open("QuizSite0.3/project/static/json/quotes.json") as json_file:
    quotes = json.load(json_file)




def keywordify(word: str) -> str:

    compareWord = str(word).casefold()
    for char in verseSymbols:
        compareWord = compareWord.replace(char, '')
    if word == '': return ''
    if word[-1] in verseSymbols:
        end = word[-1]
        word = word[:-1]
    else: end = ''

    if word[0] in verseSymbols:
        start = word[0]
        word = word[1:]
    else:
        start = ''

    if compareWord in once: return f'{start}<dt><u1>{word}</u1></dt>{end} '
    elif compareWord in twice: return f'{start}<dt><u2>{word}</u2></dt>{end} '
    else: return f'{start}<dt>{word}</dt>{end} '

# <h3 id="ICor12">
#        I Corinthians 12
#        <table>
#             <tr>
#                 <td class="number">1</td>
#                 <td><h4>    <dt>Now</dt> <dt>concerning</dt> <dt>spiritual</dt> <dt>gifts</dt>  <dt>brethren</dt>  <dt>I</dt> <dt>would</dt> <dt>not</dt> <dt>have</dt> <dt>you</dt> <dt>ignorant</dt>         </h4></td>
#             </tr>
#             <tr>
#                 <td class="number">2</td>
#                 <td><h4>    <dt>Ye</dt> <dt>know</dt> <dt>that</dt> <dt>ye</dt> <dt>were</dt> <dt>Gentiles</dt>  <dt><u1>carried</u1></dt> <dt>away</dt> <dt>unto</dt> <dt>these</dt> <dt><u1>dumb</u1></dt> <dt>idols</dt>  <dt>even</dt> <dt>as</dt> <dt>ye</dt> <dt>were</dt> <dt><u1>led</u1></dt>           </h4></td>
#             </tr>
#             ...
#         </table>

space = '  '


html = '''{{ style|safe }} 
<h1>Material</h1>
<form>
    <table style="margin: auto">
        <tr>
            <td>
                <button type="submit" type="button" name="words" value="true">Show Words</button>
                <button type="submit" type="button" name="words" value="flase">Show Letters</button>
            </td>
        </tr>
    </table>
</form>
'''

def verseNum(book: str, chapter: str, number: str) -> str:
    if int(number) in quotes[book][chapter]:
        return f"<em>{number}</em>"
    return number

for book in material:
    bookName = book
    html = html + f"<h2>{bookNameDict[bookName]}"
    book = material[book]
    for chapter in book:
        html = html + f"""
  <h3 id="{bookName}{chapter}">{bookNameDict[bookName]} {str(chapter)}
    <table>"""
        ch_str = str(chapter)
        chapter = book[chapter]
        for verse in chapter:

            

            html = html + f"""
      <tr>
        <td>{verseNum(bookName, ch_str, chapter.index(verse)+1)}</td>
        <td>
          <h4>
            """
            for word in verse.split(" "):
                html = html + keywordify(word)
            html = html + f"""
          </h4>
        </td>
      </tr>"""
        html = html + f"""
    </table>
  </h3>
"""


    html = html + '</h2>\n'

html = """
{% extends 'base.html' %}
{% block title %} Material {% endblock %}
{% block content %}

""" + html + """

{% endblock %}
"""

with open('QuizSite0.3/project/templates/material.html', 'w') as file:
        file.write(html)
        print("HTML written!")

# with open("project/static/json/material.json", 'w') as outfile:
#     json.dump(material, outfile)