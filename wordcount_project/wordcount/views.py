from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    word_dictionary = {}
    word_count = 0
    for word in word_list:
        lower_cased = word.lower().strip(",-.;:?!")
        if len(lower_cased) == 0:
            continue
        word_count += 1
        if lower_cased in word_dictionary:
            word_dictionary[lower_cased] += 1
        else:
            word_dictionary[lower_cased] = 1

    sorted_by_word = sorted(word_dictionary.items(), key=operator.itemgetter(0))
    sorted_words_by_count = sorted(sorted_by_word, key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': full_text, 'count': word_count, 
                           'sortedwords': sorted_words_by_count})

def about(request):
    return render(request, 'about.html')
    