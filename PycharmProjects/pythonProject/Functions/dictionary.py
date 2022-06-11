def book_profile(Bookname,author, published =''):
    profile={'book':Bookname, 'author':author}
    if published:
        profile['published'] = published
    return profile
store =book_profile('Aerodynamics', 'Jhon D Anderson', published='yes')
print(store)