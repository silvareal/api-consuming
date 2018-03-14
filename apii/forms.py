from django import forms
from django.conf import settings
import requests

class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data["word"]
        endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id':settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code == 200: #success
            result = response.json()
            result['success'] = True
        else:
            result["success"] = False
            if response.status_code == 404: # Not found
                result['message'] = 'no result found for %s' % word
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result