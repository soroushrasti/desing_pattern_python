from enum import Enum, auto


class Token:
    def __init__(self, token, text ):
        self.token = token
        self.text = text

    def __str__(self):
       return f"`{self.text}`"

    class Type(Enum):
        DIGIT=auto()
        PLUS=auto()
        MINUS=auto()
        LPARANT=auto()
        RPARANT=auto()

def lexing(input:str):
    results=[]
    i=0
    while(i<len(input)):
        if input[i]=="(":
            results.append(Token(Token.Type.LPARANT,"("))
        elif input[i]==")":
            results.append(Token(Token.Type.RPARANT,")"))
        elif input[i]=="+":
            results.append(Token(Token.Type.PLUS,"+"))
        elif input[i]=="-":
            results.append(Token(Token.Type.MINUS,"-"))
        elif input[i].isdigit():
            digits=[input[i]]
            for j in range(i+1,len(input)):
               if input[j].isdigit():
                   digits.append(input[j])
                   i+=1
               else:
                   break

            results.append(Token(Token.Type.DIGIT,"".join(digits)))

        i+=1
    return results

class BinaryExpression:
    class Type(Enum):
        ADDITION=auto()
        SUBTRACTION=auto()

    def __init__(self):
       self.type=None
       self.left=None
       self.right=None

    @property
    def value(self):
        # print(self.left,self.right)
        print(self.right.value)
        print(self.left.value)
        if self.type==BinaryExpression.Type.ADDITION:
            return self.left.value + self.right.value
        if self.type == BinaryExpression.Type.SUBTRACTION:
            return self.left.value - self.right.value


class Integer:
    def __init__(self, value):
        self.value = value


def parsing(tokens:[Token]):
    result=BinaryExpression()
    LFHS=False
    i=0
    while (i< len((tokens))):
        if tokens[i].token == Token.Type.DIGIT:
            integer=Integer(int(tokens[i].text))
            if not LFHS:
                result.left=integer
                LFHS = True
            else:
                result.right=integer


        elif tokens[i].token == Token.Type.PLUS:
            result.type=BinaryExpression.Type.ADDITION
        elif tokens[i].token == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif tokens[i].token == Token.Type.LPARANT:
           j=i
           while(j < len(tokens)):
               if tokens[j].token==Token.Type.RPARANT:
                   break
               j+=1

           subexpression=tokens[i+1:j]
           eleemnt= parsing(subexpression)

           if not LFHS:
               result.left=eleemnt
               LFHS=True
           else:
               result.right=eleemnt

           i=j


        i+=1

    return result

if __name__ == '__main__':
    text ="(12+1)-(3+9)"
    tokens= lexing(text)
    print("  ".join(map(lambda l: str(l),tokens)))
    print(parsing(tokens).value)