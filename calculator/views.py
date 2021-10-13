from django.shortcuts import render
from django.conf import settings


def recipe_view(request, name):

    DATA = settings.DATA
    servings = request.GET.get('servings', None)

    if servings:
        servings
    else:
        servings = 1

    result = DATA.get(name)

    context = {'recipe':{}}
    if result:
        for ingredient, amount in result.items():
            context['recipe'][ingredient] = amount*int(servings)

    return render(request, 'calculator/index.html', context)

