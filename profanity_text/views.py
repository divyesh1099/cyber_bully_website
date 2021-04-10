from django.shortcuts import render
from .models import Cusslist
import datetime
# Our Main Logic
def convert_cuss_word_to_stars(a_word):
	final_starred_word ="*"*len(a_word)
	return final_starred_word

def check_special_character(a_string, a_list):
    list_of_words_from_string = a_string.split()
    for a_word in list_of_words_from_string:
        # If the word is alpha numeric
        if a_word.isalnum():
            if a_word in cuss_words_list:
                list_of_words_from_string[list_of_words_from_string.index(a_word)] = convert_cuss_word_to_stars(a_word)
            else:
                pass
        #if the word has some special characters.
        else:
            streak = 0
            some_word = ""
            for a_character in a_word:
                if a_character.isalpha():
                    some_word += a_character
                    streak += 1
                else:
                    streak = 0
                if streak >1:
                    if some_word in cuss_words_list:
                        list_of_words_from_string[list_of_words_from_string.index(a_word)] = convert_cuss_word_to_stars(a_word)
                    else:
                        pass
                else:
                    pass
    return ' '.join(list_of_words_from_string)


cuss_words_list=list(Cusslist.objects.all().values_list('cussword', flat=True))

# Create your views here.
def index(request):
    result = "Show Result Here"
    context ={
        "result":result
    }
    return render(request, 'profanity_text/index.html', context)

