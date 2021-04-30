from django.shortcuts import render
from .models import Cusslist
import datetime

def convert_cuss_word_to_stars(a_word):
    final_starred_word = "*" * len(a_word)
    return final_starred_word

def check_for_special_character(a_word):
    for j in a_word:
        if j.isalpha()==False:
            return True


def check_if_actually_a_cussword(a_word,cuss_words_list):
    thatword=""
    for k in a_word:
        if k.isalpha()==True:
                thatword+=k
    if thatword in a_word and thatword in cuss_words_list:
        return True
    else:
        return False



def check_special_character(a_string, cuss_words_list):
    list_of_words_from_string = a_string.split()
    for a_word in list_of_words_from_string:
        if a_word.lower() in cuss_words_list:
            list_of_words_from_string[list_of_words_from_string.index(a_word)]=convert_cuss_word_to_stars(a_word)

        else:
            if check_for_special_character(a_word.lower())==True:
                if check_if_actually_a_cussword(a_word.lower(),cuss_words_list)==True:
                    list_of_words_from_string[list_of_words_from_string.index(a_word)] = convert_cuss_word_to_stars(a_word)




    return " ".join(list_of_words_from_string)



cuss_words_list=tuple(Cusslist.objects.all().values_list('cussword', flat=True))

# Create your views here.
def index(request):
    result=""
    user_input_string = ''
    if request.method=="POST":
        user_input_string = request.POST['content']
       
        result = check_special_character(user_input_string, cuss_words_list)
    context ={
           "result":result,
           "original": user_input_string
    }
    return render(request, 'profanity_text/Home.html', context)

def save_cusswords(request):
    a_string = ""
    if request.method == "POST":
        a_string = request.POST['cuss']
    list_of_cusswords = a_string.splitlines() 
    for a_word in list_of_cusswords:
        a_cussword = Cusslist.objects.create(cussword=a_word,created=datetime.datetime.now(),edited=datetime.datetime.now()) 
        a_cussword.save()  

    return render(request,"profanity_text/save_cusswords.html")
