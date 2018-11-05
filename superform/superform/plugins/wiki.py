import json
import requests

# liens utiles :

# à propos de python et des requêtes http :
# http://dridk.me/python-requests.html
# http://docs.python-requests.org/en/master/api/ --> API de requests

# à propos de l'authentification sur pmwiki
# https://www.pmwiki.org/wiki/PmWikiFr/AuthUser

# éditer une page sur wiki :
# https://www.pmwiki.org/wiki/PmWiki/BasicEditing


FIELDS_UNAVAILABLE = []
CONFIG_FIELDS = ["username","password"]


def makeText(publishing):
    titre = "!! " + publishing.title + "\n"
    author = publishing.get_author()
    date_from = publishing.date_from

    suite = "Par " + author + " Publie le " + "\n"

    corps = str(publishing.description) + "\n"

    text = titre + "-----" + suite + corps
    return text

def run(publishing,channel_config):
    json_data = json.loads(channel_config)
    pageName = "Main.test"
    text = makeText(publishing)

    data = {"n": pageName, "text": text, "action": "edit", "post": "1"}
    # r2 = requests.post("http://localhost/pmwiki-2.2.109/pmwiki.php?n=Main.Essai_nono&action=edit&text=Hello%20World&post=1", data)

    r2 = requests.post("http://localhost/pmwiki-2.2.109/pmwiki.php", data)


    #TODO completer

    #api = twitter.Api(consumer_key = json_data['consumer_key'],
     #                 consumer_secret = json_data['consumer_secret'],
      #                access_token_key = json_data['access_token_key'],
       #               access_token_secret = json_data['access_token_secret'])
    #tweet = publishing.description
    #if is_valid_tweet(tweet): # For the moment, we avoid the tweet if it's not valid
     #   api.PostUpdate(publishing.description)

