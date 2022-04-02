#solving of problem 1

def find_nth_occurrence(substring, string,num):
    try:
        x = 0
        for i in range(num):
            x = string.find(substring,x)+1
        return(x-1)
    except ValueError:print(" wrong input")
    except TypeError:print("wrong input")
    except:print('revise')
    finally:print('##############################3')


#solving of problem 2

def solve(a,b):
        for i,j in zip(a,b):
            try:
                if len(a)>=(len(a)+1):
                    return False
                elif a==b:
                    return True
                elif a=='*':
                    return True
                else:
                    x=a.find('*')
                    y=a.replace('*',f'{b[-(len(a)-x)-2:-1]}')

                    if y==b:
                        return True
                    if a.replace("*",b[x:x+len(b)-len(a)+1])==b:
                        return True
                    else:
                        return False
            except ValueError:print(" wrong input")
            except TypeError:print("wrong input")
            except:print('revise')
            finally:print('############################3')



#solving of problem 3

def solve(a,b):
        for i,j in zip(a,b):
            try:
                if len(a)>=(len(a)+1):
                    return False
                elif a==b:
                    return True
                elif a=='*':
                    return True
                else:
                    x=a.find('*')
                    y=a.replace('*',f'{b[-(len(a)-x)-2:-1]}')

                    if y==b:
                        return True
                    if a.replace("*",b[x:x+len(b)-len(a)+1])==b:
                        return True
                    else:
                        return False
            except ValueError:print(" wrong input")
            except TypeError:print("wrong input")
            except:print('revise')



