"""
Input Format

\> python -m module_name
>Word?<userinput...a word>
"""
import requests
import json
import sys

if __name__ == "__main__":
    
    print(">Word? ", end="")
    word = str(input()).strip()
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word
    try:
        response = requests.get(url)
        data = response.json()[0]

        word = data["word"].capitalize()
        meanings = data['meanings'][0]
        pos = meanings['partOfSpeech'].capitalize()
        definition = meanings['definitions'][0]['definition'].capitalize()
        print(">" + word + ". " + pos + ". "+ definition)
        
    except:
        print("Error in connection")