# SmartInput
Much better implementation of the python input function, with hints and history support.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install smartinput.

__Note:__ Windows support is temporarily dropped. We are working on a fix and will update it soon.
```bash
pip install smartinput --upgrade
```

Or alternatively, you can install the latest version using git:
```bash
git clone https://github.com/shivamsn97/smartinput
cd smartinput
python setup.py install
```
## Usage

### Using Smart Input:
```python
from smartinput import sinput
mystr = sinput("Enter your name: ") #This parameter is optional
#This will work as a normal input function.

mystr2 = sinput("Enter your designation: ", hints=["teacher","student","developer","hobbyist"])
#This will show hints whenever user will input something.
```
#### You can further customize the input field:
```python
from smartinput import sinput, Fore
mystr = sinput("Name: ", hints=["Shivam", "Tushar", "Pulkit", "Imran"], color=Fore.BLUE, hintcolor=Fore.GREEN)
```
#### Input History
Yes. You heard it right. sinput supports History. Which means you can use up/down arrow keys to navigate to previously used inputs. By default, previously used history is also treated as hints, and current input is automatically added to the provided History object. 
```python
from smartinput import sinput, History, Fore
myhistory = History()
str1 = sinput(">> ", history=myhistory, color=Fore.BLUE)
str2 = sinput(">> ", history=myhistory, color=Fore.BLUE)
str3 = sinput(">> ", history=myhistory, color=Fore.BLUE)
str4 = sinput(">> ", history=myhistory, color=Fore.BLUE)
#You can use up and down arrow keys to navigate to history. Also, history will be shown as hints.

str5 = sinput(">> ", history=myhistory, historyAsHint=False, color=Fore.BLUE)
#Here, history will not be considered as hints.

str6 = sinput(">> ", history=myhistory,autohistory=False, color=Fore.BLUE)
#The input of this command will not be added to history automatically.
```

### Create a Shell 
You can create a fully interactive shell using smartinput, in just a few lines.

#### Making a callback function
To create a shell, you must have a function that accepts two positional parameters, first is the input provided by the user, and second is a instance of a class that will be used to interact with shell in runtime.
```python
def handle_query(query, shell):
    shell.out("You said: " + query) #This will output the first parameter on the shell.
    #TODO:  in future versions, you will also be able to use return in place of shell.out.
```

You can also exit from the shell using shell.exit()
```python
def handle_query(query, shell):
    if("bye" in query):
        shell.exit()  #will exit the shell when the input is bye.
    shell.out("You said: " + query) #This will output the first parameter on the shell.
```

Alert message (Something like *Please Wait...*)
It automatically disappears on next alert or output.
```python
from time import sleep

def handle_query(query, shell):
    shell.alert("Please wait. Thinking...")
    sleep(3)  #Do processing here.
    if("bye" in query):
        shell.exit()  #will exit the shell when the input is bye.
    shell.out("You said: " + query) 
```

#### Making our Shell
```python
from smartinput import Shell, Fore
myshell = Shell()
#Important:
myshell.setcallback(handle_query) #handle_query function was defined in the above section

#Optional:
myshell.setintitle("Input: ") #defaults to "> "
myshell.setouttitle("Output: ") #defaults to "< "
myshell.setinputcolor(Fore.BLUE)
myshell.setoutputcolor(Fore.GREEN)
myshell.setalertcolor(Fore.RED)  # Color for the alert messsage.
myshell.setexiton("quit") #defaults to "exit". Whenever user inputes this or press ctrl+d (EOF, linux), the shell exits.

#You can also pass all these in the Shell constructor:
#myshell = Shell(callback=handle_query, intitle="Input: ", outtitle="Output: ", inputcolor=Fore.BLUE, outputcolor=Fore.GREEN, alertcolor=Fore.RED, exiton="quit")

#Start the shell using:
myshell.start()
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
