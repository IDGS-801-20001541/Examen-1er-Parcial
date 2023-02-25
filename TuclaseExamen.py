

class TuclaseExamen():
    
    
    '''
    define propiedades de clase 
    para utilizarlas en el metodo principal
    '''
    def operaciones (n1,n2,operacion):
        if (type(n1) != 'int' & type(n2) != 'int'):
            print("Error: Numbers must only contain digits.")
        elif(len(n1) >  4 or len>4):
            print("Error: Numbers cannot be more than four digits.")
        elif (operacion != "+"):
            print("Error: Operator must be '+' or '-'")
        elif(operacion != "-"):
            print("Error: Operator must be '+' or '-'")
        
    def arithmetic_arranger(problemas,displayMode=True):
            start = True
            side_space = "    "
            line1 = line2 = line3 = line4 = ""
            # Demaciadas operaciones
            try:
                if len(problemas) > 5:
                    raise BaseException
            except:
                return "Error: Too many problems."
            for prob in problemas:
            
                separated_problem = prob.split()
            
                number1 = separated_problem[0]
            
                operator = separated_problem[1]
                
                number2 = separated_problem[2]
                exp = operaciones (number1, number2, operator)
                if exp != "":
                    return exp
                no1 = int(number1)
                no2 = int(number2)
                
                space = max(len(number1), len(number2))
            
                if start == True:
                    line1 += number1.rjust(space + 2)
                    line2 += operator + ' ' + number2.rjust(space)
                    line3 += '-' * (space + 2)
                    if displayMode == True:
                        if operator == '+':
                            line4 += str(no1 + no2).rjust(space + 2)
                        else:
                            line4 += str(no1 - no2).rjust(space + 2)
                    start = False
            
                else:
                    line1 += number1.rjust(space + 6)
                    line2 += operator.rjust(5) + ' ' + number2.rjust(space)
                    line3 += side_space + '-' * (space + 2)
                    if displayMode == True:
                        if operator == '+':
                            line4 += side_space + str(no1 + no2).rjust(space + 2)
                        else:
                            line4 += side_space + str(no1 - no2).rjust(space + 2)
                return operator