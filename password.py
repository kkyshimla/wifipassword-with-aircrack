a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','`','~','!','@','#','$','%','^','&','*','?','_','-',':',';','/','+','*']
pwd=4
word=[]
b=[i for i in a]
while 0<=pwd<127:
    for i in a:
       for j in a:
            word=i+j+i+j
            print(word)
            f= len(word)
            while pwd>=f>=2:
                word=word+i
                print(word)
                f+=1
    pwd+=1
