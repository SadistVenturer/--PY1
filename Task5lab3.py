import random
import string 
a = string.ascii_lowercase + string.ascii_uppercase + string.digits
def get_random_password(gum) -> str:
    random.sample(gum, 8)
    return' '.join(random.sample(gum, 8))
print(get_random_password(a))