n=input().split()
a,b = int(n[0]),int(n[1])
if(b==0):
	print ("%d/0=Error" %a)
elif b<0:
	print("%d/(%d)=%.2f" %(a,b,a/b))
else:
	print("%d/%d=%.2f" %(a,b,a/b))
