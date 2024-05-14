def no_lowercase(t):return not any([_.islower() for _ in t])
def no_uppercase(t):return not any([_.isupper() for _ in t])
def no_number(t):return not any([_.isnumeric() for _ in t])
def no_symbol(t):return not any([not _.isalnum() for _ in t])
def character_repetition(t):
    for i in range(len(t)-3):
        if t[i:i+4]==t[i]*4:return 1
def number_sequence(t):
    for i in range(len(t)-3):
        _=t[i:i+4]
        if _.isnumeric():
            if '01234567890'.find(_)!=-1:return 1
            if '09876543210'.find(_)!=-1:return 1
    return 0
def letter_seqence(t):
    for i in range(len(t)-3):
        _,o=t[i:i+4],'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if _.isalpha():
            if o.find(_.upper())!=-1:return 1
            if "".join(reversed(o)).find(_.upper())!=-1:return 1
    return 0
def keyboard_pattern(t):
    for i in range(len(t)-3):
        _=t[i:i+4].upper()
        if '!@#$%^&*()_+|'.find(_)!=-1 or '!@#$%^&*()_+|'.find(''.join(reversed(_)))!=-1 :return 1
        if 'QWERTYUIOP'.find(_)!=-1 or 'QWERTYUIOP'.find(''.join(reversed(_)))!=-1 :return 1
        if 'ASDFGHJKL'.find(_)!=-1 or 'ASDFGHJKL'.find(''.join(reversed(_)))!=-1 :return 1
        if 'ZXCVBNM'.find(_)!=-1 or 'ZXCVBNM'.find(''.join(reversed(_)))!=-1 :return 1
    return 0
passw,errors=input().strip(),[]
if len(passw)<8:errors.append('Less than 8 characters')
if no_lowercase(passw):errors.append('No lowercase letters')
if no_uppercase(passw):errors.append('No uppercase letters')
if no_number(passw):errors.append('No numbers')
if no_symbol(passw):errors.append('No symbols')
if character_repetition(passw):errors.append('Character repetition')
if number_sequence(passw):errors.append('Number sequence')
if letter_seqence(passw):errors.append('Letter sequence')
if keyboard_pattern(passw):errors.append('Keyboard pattern')
if len(errors)==0:errors.append('OK')
for _ in errors:print(_)