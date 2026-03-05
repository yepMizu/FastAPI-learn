
def find_post(id,my_posts):
    for p in my_posts:
        if p["id"] == id:
            return p
    return None

def find_index(id,my_posts):
    for i , p in enumerate(my_posts):
        if p["id"] == id:
            return i 

