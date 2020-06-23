#pip install getch
windows = False
import os
if os.name == 'nt':
    from msvcrt import getch
    windows = True
else:
    from getch import getch
#pip install colorama
from colorama import Fore, Style, Back

def mygetch():
	if windows:
		return getch().decode("utf-8")
	return getch()

class History:
    def __init__(self, default=[]):
        self._hList = default

    def add(self, string):
        self._hList.insert(0,string)

    def find(self, what):
        return [x for x in self._hList if x.startswith(what)]

    def aslist(self):
        return list(self._hList)

BaseHistory = History(["one","two","three"])

def suggestion(query, history, hints):
    if not(query):
        return ""
    slist=[]
    if(history):
        slist+=history.find(query)
    if(hints):
        slist+= [x for x in hints if x.startswith(query)]
    if len(slist)==0:
        return ""
    if len(slist)==1:
        return slist[0][len(query):]
    slist = [x[len(query):] for x in slist]
    nval = ""
    i=0
    try:
        while True:
            thischar = slist[0][i]
            for x in slist:
                if(x[i]!=thischar):
                    raise Exception
            nval += thischar
            i+=1
    except:
        return nval   
    return ""

    
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

class _exitShell(Exception):
    pass

     
class _interact:
    def __init__(self, intitle, outtitle, inputcolor, outputcolor, alertcolor):
        self.intitle=intitle
        self.outtitle=outtitle
        self.inputcolor = inputcolor
        self.outputcolor = outputcolor
        self.alertcolor = alertcolor
        self.alertmsg=None
        self.message = None

    def exit(self):
        raise _exitShell

    def getmessage():
        return str(self.message)

    def out(self, x):
        if self.alertmsg:
            print('\r'+ ' '*(len(self.alertmsg)+ len(self.outtitle)) + '\r', end="", flush=True)
            self.alertmsg = None
        print(self.outtitle + (self.outputcolor if self.outputcolor else "") + x + (Style.RESET_ALL if self.outputcolor else "") ) 

    def alert(self, x):
        print('\r' +  ' '*len(self.outtitle) + (self.alertcolor if self.alertcolor else "" ) + x + (Style.RESET_ALL if self.alertcolor else ""), end="", flush=True)
        self.alertmsg = x
        
class Shell:
    def __init__(self,callback = None, exiton = "exit", intitle="> ", outtitle="< ", inputcolor =None, outputcolor=None, alertcolor=None):
        self.intitle=intitle
        self.outtitle=outtitle
        self.history=History()
        self.instancerunning = False
        self.call = callback
        self.inputcolor = inputcolor
        self.outputcolor = outputcolor
        self.alertcolor = alertcolor
        self.exiton = exiton

    def setexiton(self, x):
        self.exiton=x

    def setintitle(self, x):
        self.intitle=x

    def setouttitle(self,x):
        self.outtitle=x

    def setinputcolor(self,x):
        self.inputcolor = x

    def setoutputcolor(self,x):
        self.outputcolor = x

    def setalertcolor(self, x):
        self.alertcolor = x

    def setcallback(self,x):
        self.call = x

    def start(self):
        if(self.instancerunning):
            raise Exception("Instance of shell is already running.")
        if not(self.call):
            raise Exception("No callback function defined. Set a callback function using Shell.setcallback(Function). Function should accept a string and a _interact object as a parameter.")
        self.instancerunning = True
        self.instance = _interact(self.intitle, self.outtitle, self.inputcolor, self.outputcolor, self.alertcolor)
        while True:
            a = sinput(what=self.intitle,hints=[self.exiton], color=self.inputcolor,history=self.history, eof=self.exiton)
            if a == self.exiton:
                break
            try:
                self.call(a, self.instance)
            except _exitShell:
                break
        self.instancerunning = False

if __name__ == "__main__":
	for i in range(10):
		print(mygetch())
