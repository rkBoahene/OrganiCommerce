from .cart import Cart

""" 
A context processor is a function that receives the request object
as a parameter and returns a dictionary of objects that will be 
available to all templates rendered using RequestContext. 

"""


def cart(request):
    # instantiate cart using the request object and make it available
    # to all templates as a variable called cart
    return {'cart': Cart(request)}
