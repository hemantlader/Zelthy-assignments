"""
Input Format : Command Line Args

\> python -m module_name Word?<userinput...a word>
"""
import requests
import json
import sys

if __name__ == "__main__":
    
    if(len(sys.argv) < 2 ):
        print("Please pass argument as 'Word?<user input ...a word>")
    else:
        inp= sys.argv[1].split('?')
        if inp[0].strip() != "Word":
            print("Invalid Command \nPlease pass argument as 'Word?<user input ...a word>")
        else:
            word = inp[1].strip()
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word
            try:
                response = requests.get(url)
                # print(response.status_code)
                data = response.json()[0]
                
                if(data.keys() == 0 ):
                    print("Meaning not found")
                else:    
                    word = data["word"].capitalize()
                    meanings = data['meanings'][0]
                    pos = meanings['partOfSpeech'].capitalize()
                    definition = meanings['definitions'][0]['definition'].capitalize()
                    print(">" + word + ". " + pos + ". "+ definition +".")
            except:
                print("Error in connection")
            