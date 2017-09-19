from string import ascii_letters

s='oczmz vmzor jocdi bnojv dhvod igdaz admno ' \
  'ojbzo rcvot jprvi oviyv aozmo cvooj ziejt' \
  'dojig toczr dnzno jahvi fdiyv xcdzq zoczn' \
  'zxjiy'
ns=''
for c in s:
    if c in ascii_letters:
        ns=ns+ascii_letters[(ascii_letters.index(c)+5)%len(ascii_letters)]
    else:
        continue

print(ns)