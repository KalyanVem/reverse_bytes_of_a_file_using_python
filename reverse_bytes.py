print("**The reversed binary must be in the same directory as this script**")
file_name=raw_input("Enter File Name: ")
with open(file_name, 'rb') as infile:
	a = (infile.read().encode('hex'))
b=a[::-1]
with open("fin",'wb') as final:
	final.write(b)
with open('fin') as inp, open('reversed.png', 'wb') as out:
        out.write(
            inp.read().decode('hex')
        )