fh=open("output4.txt",'w')
abc = [1,2,3,4,6,7,8,11] 
sum=0
i=0
while(i<len(abc)):
 sum=sum+abc[i]
 i=i+1
avg=int(sum/len(abc))
fh.write("the average is:"+str(avg)) 