
# how to train 
>>> lda_model=train(read_sample())


# how to test
>>> from src.models.test import *
>>> model = load_model()
>>> test = test(model, 'Best SPA, attention 10/10. Amazing food and experience!! 100% recommended. Massages are great, rooms are clean and location is great. Definitely going to come back! If you want to have the whole Antigua experience don’t hesitate to choose this hotel.')