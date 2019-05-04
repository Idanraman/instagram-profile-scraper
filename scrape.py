import grequests
import urllib.request

holdusers = []
holdpages = []
holdurls = []
filename = 'file.txt'
with open(filename,'r', encoding="utf8") as fh:
	for idx,line in enumerate(fh):
		if idx == 0 : 
			holdusers.append(str(line)[:-1][1:])
		else:
			holdusers.append(str(line)[:-1])

for idx,username in enumerate(holdusers):
	page = 'https://www.instagram.com/' + username
	holdpages.append(page)

print(holdpages)
rs = (grequests.get(u) for u in holdpages)
ans = grequests.map(rs)

print(ans)
for page in ans:
	print(page.status_code)
	try:
		if page.status_code == 200:
			x = page.text.find('og:image')
			y = page.text.find('"', x+10)
			z = page.text.find('"', y+1)
			url = page.text[y+1:z]
			holdurls.append(url)
	except:
		pass

print('STARTING!!!')
thefile = open('test.txt', 'w')
for idx,item in enumerate(holdurls):
  thefile.write("%s\n" % item)
  urllib.request.urlretrieve(item, "profiles/"+str(holdusers[idx])+".jpg")
print(holdurls)
