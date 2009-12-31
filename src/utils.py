'''
Created on Nov 10, 2009

@author: gumuz
'''

def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size


def get_file_icon(filename):
    file_icon = {"picture.png" : ('.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tif'),
                 "music.png" : ('.mp3', '.wav', '.wma'),
                 "film.png" : ('.mp4', '.avi', '.mkv', '.wmv'),
                 "compress.png" : ('.zip', '.rar', '.7z', '.tar.gz'),
                 "application.png" : ('.exe', '.bat', '.dll', '.com'),
                 }
    
    default = "page.png"
    
    for icon, extensions in file_icon.items():
        for ext in extensions:
            if filename.lower().endswith(ext):
                return icon
            
    return default

def split_seq(seq,size):
    """ Split up seq in pieces of size """
    return [seq[i:i+size] for i in range(0, len(seq), size)]

def divide_permutate(l):
    from itertools import permutations
    
    best = divide(l)
    
    for p in permutations(l):
        parts = divide(p)
        if len(best) > len(parts):
            best = parts
            
    return best
        
def divide_greedy(l, max):
    return divide(sorted(l,cmp=lambda a,b: cmp(a['size'], b['size']), reverse=True), max)    

def divide_random(l, max):
    from random import shuffle
    l = l[:]
    best = divide(l)
    
    for i in range(50000):
        shuffle(l)
        d = divide(l, max)
        if len(d) < len(best):
            best = d
            
    return best

def divide(l, max):
    l = list(l)
    parts = []
    
    part = []
    while l:
        n = l.pop()
        if sum([p['size'] for p in part])+n['size'] < max:
            part.append(n)
        else:
            parts.append(part)
            part = [n]
    if part:
        parts.append(part)
        
    return parts