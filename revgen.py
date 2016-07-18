with open("combined.txt") as f:
    content = f.readlines()

matchMin = 5

#remove short lines

names = [x.strip() for x in content if len(x)>matchMin]

replacements = []

def matchLength(sa1,sa2):
	s1 = sa1[::-1]
	s2 = sa2[::-1]
	agreement=0;
	for i in range(0,min(len(s1),len(s2))):
		if s1[i]==s2[i]:
			agreement = agreement + 1
		else:
			break;
	return agreement

def startsWith(n,beginning):
	return n[:len(beginning)]==beginning

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
				replacements.append([n1[:len(n1)-match+2],n2[:len(n2)-match+2],n1,n2])
				replacements.append([n2[:len(n2)-match+2],n1[:len(n1)-match+2],n2,n1])
				#print replacements[len(replacements)-1]

def replaceBeginning(n,oldbeginning,newbeginning):
	return newbeginning + n[len(oldbeginning):]

print "generating names"

generated = []

for n in names:
	for r in replacements:
		if startsWith(n,r[0]):
			newN = replaceBeginning(n,r[0],r[1])
			if not newN in names and not newN in generated:
				print newN + "\t( " + n + " | " + r[2] + " -> " + r[3] + " )"
				generated.append(newN)