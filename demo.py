import FreeSimpleGUI as sg

def calc_snoopy(a,v):
    
    print("Calculating snoopy with a =", a, "and v =", v)
    return a + v
sg.askcolor()


print(calc_snoopy(5, 10))