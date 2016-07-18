with open("combinedbig.txt") as f:
    content = f.readlines()

matchMin = 5

#remove short lines

names = [x.strip() for x in content if len(x)>matchMin]

replacements = []

def matchLength(s1,s2):
	agreement=0;
	for i in range(0,min(len(s1),len(s2))):
		if s1[i]==s2[i]:
			agreement = agreement + 1
		else:
			break;
	return agreement

def endsWith(n,ending):
	return n[len(n)-len(ending):]==ending

print "making replacements"

for n1 in names:
	for n2 in names:
		if n1==n2:
			continue
		match = matchLength(n1,n2)
		if match>matchMin:
			l1 = len(n1[match-1:])
			l2 = len(n2[match-1:])
			if (l1>2 and l2>2):
				replacements.append([n1[match-1:],n2[match-1:],n1,n2])
				replacements.append([n2[match-1:],n1[match-1:],n2,n1])

def replaceEnding(n,oldending,newending):
	return n[:len(n)-len(oldending)]+newending

generated = []

for n in names:
	for r in replacements:
		if endsWith(n,r[0]):
			newN = replaceEnding(n,r[0],r[1])
			if not newN in names and not newN in generated:
				print newN + "\t( " + n + " + " + r[2] + " -> " + r[3] + " )"
				generated.append(newN)