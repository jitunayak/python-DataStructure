from stack import stack

def is_match(p1,p2):
    if p1=='{' and p2=='}':
        return True
    if p1=='(' and p2==')':
        return True
    if p1=='[' and p2==']':
        return True 
    else:
        return False  
def check_para(paren_string):
    s = stack()
    is_balanced =True;
    index = 0
    if(paren_string==''):
        is_balanced=False
        return 'Empty'
    else:
        while len(paren_string)>index and is_balanced:
            paren = paren_string[index]
            if paren in "{([ ":
                if s.push(paren):
                    s.push(paren)
                else:
                    is_balanced=False    

            else:
                if(s.isEmpty):
                    is_balanced=True
                if not is_match(s.peek(),paren):
                    is_balanced=False
                s.pop()    
            index +=1


        if is_balanced and s.isEmpty():
            return "Balanced"
        else:
            return "Not Balanced"



def __main__():
    print(check_para(' '))

__main__()