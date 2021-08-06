'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from ..models import Contact, Product, Favorite


def product_search(search_request):
    product_search = Product.objects.filter(
        name__icontains=search_request)
    return product_search


def substitute_search(search_request):
    product_search = Product.objects.filter(
        name__icontains=search_request)
    my_product = product_search[0]
    my_product_nutriscore = my_product.nutriscore_grade
    if my_product_nutriscore == 'e':
        list_score = ["d", "c", "b", "a"]
        substitute_search = Product.objects.filter(
            category_id=my_product.category_id).filter(
            nutriscore_grade__in=list_score).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'd':
        list_score = ["c", "b", "a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'c':
        list_score = ["c", "b", "a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'b':
        list_score = ["b", "a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    else:
        list_score = ["a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    return substitute_search