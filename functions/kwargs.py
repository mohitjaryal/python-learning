# kwargs
# it allows us to pass any number of keywords arguments
# keywords argument mean that they contain a key-value pair, like a python dictionary

# jb hme arguments ko key:value pair m bhejna h tb hm kwargs ka use krte h 
def display(**kwargs):
    
    for(key,value) in kwargs.items():
        print(key,'->',value)

display(india='delhi',srilanka='colombo')