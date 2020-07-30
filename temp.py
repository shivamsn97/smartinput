def sinput(what = "",history=None, hints=None, historyAsHint=True,autohistory= True, eof=None, whatcolor=None, color=None, hintcolor=Fore.MAGENTA):
    print((whatcolor if whatcolor else "") + what + (Style.RESET_ALL if whatcolor else "") + (color if color else ""), end='', flush=True)
    x = str(mygetch())
    rtn = ""
    mhistory = [""] + history.aslist() if history else []
    hcur = 0
    rval = 0
    suggest = ""
    while(x != '\n' and x != '\r'):
        if(ord(x)==4):
            print(Style.RESET_ALL)
            if eof:
                return eof
            raise EOFError
        if(ord(x) == 127):
            if(rtn):
                rtn = (rtn[:-rval-1] if rval else rtn[:-1]) + (rtn[-rval:] if rval else "")
                print('\b' + rtn[-rval:] +' ' + ' '*(len(suggest)) + '\b'*(rval+1+len(suggest)) if rval else " "*(len(suggest)) + '\b'*len(suggest) + "\b \b", end="", flush=True) 
        elif(x== '\t'):
            rtn+=suggest
            print(rtn[-rval-len(suggest):] if (rval+len(suggest)) else "", end="", flush=True)
            rval=0
        elif ord(x) == 27:
            x = mygetch()
            if (ord(x)==91):
            #67 = right, 68 = left, 65= up, 66= down
                x = ord(mygetch())
                if(x == 68 and rval<len(rtn)):
                    print('\b', end="", flush=True)
                    rval +=1
                if(x==67):
                    if(rval):
                        print(rtn[-rval], end="", flush=True)
                        rval-=1
                    else:
                        x = "\t"
                        continue
                if history:
                    if(x==66 and hcur>0):
                        mhistory[hcur] = rtn
                        hcur-=1
                        print('\b'*(len(rtn)-rval)  + ' '*len(rtn) + '\b'*len(rtn), end="", flush=True)
                        rtn = mhistory[hcur]
                        print(rtn, end="", flush=True)
                        rval=0
                    elif(x== 65 and hcur < len(mhistory)-1):
                        mhistory[hcur] = rtn
                        hcur+=1
                        print('\b'*(len(rtn)-rval) + ' '*len(rtn) + '\b'*len(rtn),end="", flush=True)
                        rtn = mhistory[hcur]
                        print(rtn, end="", flush=True)
                        rval=0
        else:
            rtn = (rtn[:-rval] if rval else rtn) + x + (rtn[-rval:] if rval else "")
            print(rtn[-rval-1:] + '\b'*rval if rval else x, end="", flush=True)
        tx = True
        if(not(rval)):
            print(' '*len(suggest) + '\b'*len(suggest), end='', flush=True)
        if(suggest and rtn and not(rval)):
            if(x==suggest[0]):
                suggest=suggest[1:]
                tx = False
            else:
                tx = True
                suggest=""
        if tx:
            suggest = suggestion(rtn,history if historyAsHint else None, hints)
            tx = True
        if(suggest and rtn):
            print((rtn[-rval:] if rval else "") +  hintcolor + Style.DIM + suggest + Style.RESET_ALL + (color if color else "") + "\b"*(len(suggest)+rval), end='', flush=True)
        x = mygetch()
    print(' '*len(suggest)+ '\b'*len(suggest) + Style.RESET_ALL)
    if(autohistory and history):
        history.add(rtn)
    return rtn
