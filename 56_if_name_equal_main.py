# 56. if __name__ == '__main__'

        # FILE - firstModule.py
print(__name__)

print(f'First modules name {__name__}')

# before python runs any code file it first goes through and sets a few special variables which __name__ is one of those special variables 
    # and when python runs a file directly it sets __name__ = __main__ 


# whenever we import a file its code is run 
        # FILE - secondModule.py
# when we import module __name__ is set to name of module/file 
import first_module
    # whenever we import a module its code is run 
    # so OutPut in this case will be name of module, since whenever import a module containing __name__ its name is set to name of file 

print(f'__name__ in second module {__name__}')
        # OP -
            # first_module
            #  __main__ // since python is running that file directly
def main():
    pass

if __name__=='__main__':
    main()
    # thus its helps in finding if the current module is being ran directly or being imported

#-----------------------------------------------------------------------------
            # FILE - firstModule.py  
if __name__=='__main__':
    print('FirstModule Run Directly')
else:
    print('FirstModule Run from Import')

            # FILE - secondModule.py
import firstModule
print(f'running __name__ in second Module directly {__name__}')

# if block of >> if __name__=="__main__":
    # allows to execute code in that file only if run directly and helps separate code that not to run when this module is imported to other
    # main() method can also be run explictly in other module
        # firstModule.main() to run main() in other module 

#-----------------------------------------------------------------------------
            # FILE - firstModule.py
print('in firstModule this will always be run')  

def main():
    print("first module main method")

if __name__=="__main__":
    main()

            # FILE - secondModule.py
import firstModule

firstModule.main()
  # main() method can also be run explictly in other module
        # firstModule.main() to run main() in other module 
print(f'second modules name is {__name__}')