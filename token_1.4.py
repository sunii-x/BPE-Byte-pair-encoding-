import os
os.system('cls')


with open("corpus.txt","r",encoding='utf-8') as file:
    corpus = file.read()


class Tokenizaton:
    encode =[]

    textVocab = {chr(i): i for i in range(256)}
  
    numVocab = {}

    def bitBreak(self,corpus):
        bitToken = list(corpus.encode("utf-8"))
        return bitToken
    
    def grping(self,corpus):
        grpfreq = {}
        for i in range(len(corpus)):
          
            if i != len(corpus)-1:
                t = corpus[i],corpus[i+1]
                if t in grpfreq:
                    grpfreq[t] +=1
                else:
                    grpfreq[t] = 1 
                
        
        # for x, y in grpfreq.items():
        #     print(x," : ",y)
        return grpfreq
    
    def pairfinder(self,corpus):

        frequent_pair = () 
        count = list(corpus.values())
        freqent_count = count[0]         
        for key,value in corpus.items():
            if freqent_count <= value :
                freqent_count =  value
            if value == freqent_count :
                frequent_pair = key

        Tokenizaton.textVocab[frequent_pair] = len(Tokenizaton.textVocab)
        Tokenizaton.encode.append(frequent_pair)

        # print(frequent_pair)

        return frequent_pair
    

    def crtToken(self,corpus,bitToken):

        # print(bitToken,len(bitToken))
        x = self.pairfinder(corpus)
       
        i = 0
        tempbi = []
        while len(bitToken)  != i:
            if len(bitToken)-1 != i :
               
                if x[0] == bitToken[i] and x[1] == bitToken[i+1]:
                    tempbi.append((len(Tokenizaton.textVocab)))
                    i += 2
                    continue
                else:
                    tempbi.append(bitToken[i])
                    i +=1
            else:
                tempbi.append(bitToken[i])
                i += 1

        # print(tempbi,len(tempbi))

        for key, value in Tokenizaton.textVocab.items():
            Tokenizaton.numVocab[value] = key

        
        return tempbi
    

    def run_bpe(self,corpus):
        self.corpus = corpus

        d1 = self.bitBreak(corpus)
        for i in range(50):
            d2 = self.grping(d1)
            d1 = self.crtToken(d2,d1)

        # for x, y in Tokenizaton.textVocab.items():
        #     print(x," : ",y)
      
        
        

class encodeco(Tokenizaton):

    def encoder(self,corpus):
        tokens = self.bitBreak(corpus)
        # print(tokens,"input")
        # print(Tokenizaton.encode , "encode")

       
        for i in Tokenizaton.encode:
            tip = []
            j = 0
            while len(tokens) != j:
                
                if len(tokens) -1 != j:
                    if i[0] == tokens[j] and i[1] == tokens[j+1]:
                        t =( i[0] , i[1])
                        tip.append(Tokenizaton.textVocab.get(t))
                        j +=2
                    else:
                        tip.append(tokens[j])
                        j +=1

                else:
                    tip.append(tokens[j])
                    j +=1
                
            tokens = tip
        print("encode input : ",tokens)
    
        return tokens
    
    def expand(self,token):
        t = Tokenizaton.numVocab.get(token)
        lit = []
        for i in t:
            if i < 255:
                lit.append(i)
            else:
                self.expand(i)
        return lit

    
    def decoder(self,tokens):
        # print(tokens)
        bty = []


        for i in tokens:
            if i <= 255:
                bty.append(i)
            else:
                t = self.expand(i)
                for k in t:
                    bty.append(k)
    
        txt = bytes(bty).decode("utf-8")
        print("result : " ,txt)

            

t1 = Tokenizaton()

t1.run_bpe(corpus)

t2 = encodeco()
data = "“I know how to enter the Chakravyuha,” Abhimanyu said, his voice steady as a drawn bowstring. “Though I do not know the path to exit, I will fight my way through.”"
d1 = t2.encoder(data)
t2.decoder(d1)
# for i,j in Tokenizaton.textVocab.items() :
#     print(i ," : " , j)
