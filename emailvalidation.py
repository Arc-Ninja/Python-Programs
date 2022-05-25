while True:
    a = str(input('Enter your email: '))
    b = 'fail'
    if a.endswith('.com') or a.endswith('.co') or a.endswith('.in'):
           if a[0]!= '1' and a[0]!='2' and a[0]!='3'and a[0]!='4'and a[0]!='5'and a[0]!='6'and a[0]!='7'and a[0]!='8' and a[0]!='9' and a[0]!='0':
               if a.count('`')==0 and a.count('~')==0 and a.count('!')==0 and a.count('#')==0 and a.count('$')==0 and a.count('%')==0 and a.count('^')==0 and a.count('&')==0 and a.count('*')==0 and a.count('(')==0 and a.count(')')==0 and a.count('-')==0 and a.count('_')==0 and a.count('+')==0 and a.count('=')==0 and a.count('[')==0 and a.count(']')==0 and a.count('{')==0 and a.count('}')==0 and a.count('|')==0 and a.count('\\')==0 and a.count('/')==0 and a.count('?')==0 and a.count(';')==0 and a.count(':')==0 and a.count('"')==0 and a.count('\'')==0 and a.count('<')==0 and a.count('>')==0 and a.count(',')==0 and a.count('@')==1 and a.count(' ')== 0:
                   b = 'pass'

    if b== 'pass':
        print('This email is valid')
    else:
        print('invalid email')
