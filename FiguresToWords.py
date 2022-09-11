dic={
    '00':'Zero',
    '01':'One',
    '02':'Two',
    '03':'Three',
    '04':'Four',
    '05':'Five',
    '06':'Six',
    '07':'Seven',
    '08':'Eight',
    '09':'Nine',
    0:'Zero',
    1:'One',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10:'Ten',
    11:'Eleven',
    12:'Twelve',
    13:'Thirteen',
    14:'Fourteen',
    15:'Fifteen',
    16:'Sixiteen',
    17:'Seventeen',
    18:'Eighteen',
    19:'Nineteen',
    20:'Twenty',
    30:'Thirty',
    40:'Fourty',
    50:'Fifty',
    60:'Sixty',
    70:'Seventy',
    80:'Eighty',
    90:'Ninety',
    100:'Hundred',
    1000:'Thousand',
    100000:'Lakh',
    1000000:'Million',
    1000000000:'Billion',
}
def helperFunc(s):
    if s[0]!='0':
        number=int(s)
    elif s[0]=='0' and s[1]!='0':
        return dic[int(s[1])]
    elif s[0]=='0' and s[1]=='0':
        return ""
    if len(str(number))==2:
        string=str(number)
        if number<20 and number>=10:
            return dic[number]
        elif number==20:
            return dic[20]
        elif number>20 and number<30:
            return dic[20]+" "+dic[int(string[1])]
        elif number==30:
            return dic[30]
        elif number>30 and number<40:
            return dic[30]+" "+dic[int(string[1])]
        elif number==40:
            return dic[40]
        elif number>40 and number<50:
            return dic[40]+" "+dic[int(string[1])]
        elif number==50:
            return dic[50]
        elif number>50 and number<60:
            return dic[50]+" "+dic[int(string[1])]
        elif number==60:
            return dic[60]
        elif number>60 and number<70:
            return dic[60]+" "+dic[int(string[1])]
        elif number==70:
            return dic[70]
        elif number>70 and number<80:
            return dic[70]+" "+dic[int(string[1])]
        elif number==80:
            return dic[80]
        elif number>80 and number<90:
            return dic[80]+" "+dic[int(string[1])]
        elif number==90:
            return dic[90]
        elif number>90 and number<100:
            return dic[90]+" "+dic[int(string[1])]
        
def FTW(number):
    print("The roman number representation of the above number is: ")
    string=str(number)
    length=len(string)
    if number<(10**12) and length<13:
        if length==1:
            return dic[number]
        elif length==2:
            if number>=10 and number<20:
                return dic[number]
            elif number>20:
                return helperFunc(string)
        elif length==3:
            return dic[int(string[0])]+" "+dic[100]+" "+helperFunc(string[1]+string[2])
        elif length==4 and number>=1000 and number<10000:
            if string[1]=='0':
                return dic[int(string[0])]+" "+dic[1000]+" "+helperFunc(string[2]+string[3])
            else:    
                return dic[int(string[0])]+" "+dic[1000]+" "+dic[int(string[1])]+" "+dic[100]+" "+helperFunc(string[2]+string[3])
        elif length==5 and number>=10000 and number<100000:
            if string[2]=='0':
                return helperFunc(string[0]+string[1])+" "+dic[1000]+" "+helperFunc(string[3]+string[4])
            else:
                return helperFunc(string[0]+string[1])+" "+dic[1000]+" "+dic[int(string[2])]+" "+dic[100]+" "+helperFunc(string[3]+string[4])
        elif length==6 and number>=100000 and number<1000000:
            # We can use hindi version of it by using lakh. (There is lot to implement it but for now i am focusing on roman version numbering)
            # if string[3]=='0':
            #     if string[1]=='0' and string[2]=='0':
            #         return dic[int(string[0])]+" "+dic[100000]+" "+helperFunc(string[4]+string[5])
            #     else:
            #         return dic[int(string[0])]+" "+dic[100000]+" "+helperFunc(string[1]+string[2])+" "+dic[1000]+" "+helperFunc(string[4]+string[5])
            # else:
            #     return dic[int(string[0])]+" "+dic[100000]+" "+helperFunc(string[1]+string[2])+" "+dic[1000]+" "+dic[int(string[3])]+" "+dic[100]+" "+helperFunc(string[4]+string[5])
            if string[3]=='0':
                if string[1]=='0' and string[2]=='0':
                    return dic[int(string[0])]+" "+dic[100]+" "+dic[1000]+" "+helperFunc(string[4]+string[5])
                else:
                    return dic[int(string[0])]+" "+dic[100]+" "+helperFunc(string[1]+string[2])+" "+dic[1000]+" "+helperFunc(string[4]+string[5])
            else:
                if string[1]=='0' and string[2]=='0':
                    return dic[int(string[0])]+" "+dic[100]+" "+dic[1000]+" "+dic[int(string[3])]+" "+dic[100]+" "+helperFunc(string[4]+string[5])
                else:
                    return dic[int(string[0])]+" "+dic[100]+" "+helperFunc(string[1]+string[2])+" "+dic[1000]+" "+dic[int(string[3])]+" "+dic[100]+" "+helperFunc(string[4]+string[5])
print("Type any number that you wanna convert into the roman number representation: ")
num=int(input())
print(FTW(num))