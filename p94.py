first_three = "abc"
result = "+".join(first_three)
print(result)


words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words)
print(one)

##
s = "   The   "
s = s.strip()
print(s)

##p96 replace
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

##index
print("animals".index("m"))
#96 index
try:
    "animals".index("z")
except:
    print("Not found.")
	

#in 
print("Cat" in "Cat in the house.")
print("Bat" in "Cat in the house.")
print("Potter" not in "Harry")

#
print("She says \"That is right.\" ")
print("She says 'That is right.' ")


#p99 \nline
print("line1\nlin2\nline3")


#slice
fict = ["torusutoi", "Kamyu", "Owal", "Hakusutory", "Ostin"]
print(fict[0:3])


