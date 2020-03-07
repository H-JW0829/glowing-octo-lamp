import random
def createRandomString(len):
    raw = ""
    range1 = range(58, 65) # between 0~9 and A~Z
    range2 = range(91, 97) # between A~Z and a~z

    i = 0
    while i < len:
        seed = random.randint(48, 122)
        if ((seed in range1) or (seed in range2)):
            continue;
        raw += chr(seed);
        i += 1
    return raw

def dobule_to_dict(v):
    result = {}
    for key in v.__mapper__.c.keys():
        if getattr(v, key) is not None:
            result[key] = str(getattr(v, key))
        else:
            result[key] = getattr(v, key)
    return result


def to_json(all_vendors):
    v = [ dobule_to_dict(ven) for ven in all_vendors ]
    return v

def sortBlogsByTime(blogs):
    times = []
    for blog in blogs:
        times.append(blog['create_time'])
    sorted_time = sorted(times, key=str.lower,reverse=True)
    sorted_blogs = []
    for time in sorted_time:
        for blog in blogs:
            if time == blog['create_time']:
                sorted_blogs.append(blog)
    print(sorted_blogs)
    return sorted_blogs
