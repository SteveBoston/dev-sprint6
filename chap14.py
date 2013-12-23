# This is where chapter 14 exercises go.

import urllib
import string

# conn = urllib.urlopen('http://thinkpython.com/secret.html')

# for line in conn:
# 	print line.strip()

zipcode = raw_input("Please enter a zip code.")




conn = urllib.urlopen("http://www.uszip.com/zip/" + zipcode)


for line in conn:
	if "meta name=\"description\"" in line:
		pop = line
		a = string.split(pop,"What is the ZIP code for")
		b = a[1:]
		c = "".join(b)
		d = string.split(c, "?")
		e = d[0]
		print zipcode, "is a zip code in", e
	if "Total population" in line:
		pop = line
		f = string.split(pop,"<dd>")
		g = f[1:]
		h = "".join(g)
		i = string.split(h, "<span class=")
		j = i[0]
		print j, "people live in this zip code."






