print("Welcome to the official website of CBWED(Central board of workers education and development)")
n=int(input("Kindly enter the basic salary:"))
da=5/100*n
hra=7/100*n
gr=n+da+hra
if gr<15000:
	print("Official post:clerk")
	print("Officials in this post are: Kavya chopra,Krishnendu Rai,Alam rafik,Moinuddin Ahmed")
	print("The da of the person is ",da)
	print("The hra of the person is ",hra)
	print("The gross salary of the person is ",gr)
elif gr>15000 and gr<60000:
	print("Official post:staff")
	print("Officials in this post are: Priyotosh Mitra,Arabinda Ganguly,Mainak Shil,Roshni Majhi")
	print("The da of the person is ",da, '\n', "The hra of the person is ",hra, '\n', "The gross salary of the person is ",gr)
   # print("The hra of the person is ",hra)
    #print("The gross salary of the person is ",gr)
elif gr>60000 and gr<170000:
	print("Official post:Education officer")
	print("Officials in this post are: Sabyasachi Sarkar,Sukanya banerjee,Krishna Das,Aditya Roy Choudhury")
	print("The da of the person is ",da, '\n', "The hra of the person is ",hra, '\n',"The gross salary of the person is ",gr)
    #print("The hra of the person is ",hra)
    #print("The gross salary of the person is ",gr)
elif gr>170000 and gr<210000:
	print("Official post:Regional director")
	print("Officials in this post are: Chinmoy bhattacharya")
	print("The da of the person is ",da, '\n', "The hra of the person is ",hra, '\n', "The gross salary of the person is ",gr)
    #print("The hra of the person is ",hra)
    #print("The gross salary of the person is ",gr)
else:
	print("Sorry, We have no such employee with that salary")