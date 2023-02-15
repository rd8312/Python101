def get_description():
    """Return random weather, just like the pros"""
    # from random import choice
    # possibilities = ["rain", "snow", "sleet", "fog", "sun", "who knows"]
    # return choice(possibilities)

    # more safe
    import random
    possibilities = ["rain", "snow", "sleet", "fog", "sun", "who knows"]
    return random.choice(possibilities)