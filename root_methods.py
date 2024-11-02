import sympy as sp
import numpy as np

class wrong_val_inputs(Exception):
     pass

class Roots():
    # Constructor
    # If more than 1 variable give symbol with space between them
    def __init__(self, equation, symbol):
        self.equation = equation
        self.symbol =symbol

    def equation_val(self,val):
         return float((self.equation.subs({self.symbol:val})).evalf())
    
    def equation_lst_vals(self,vals):
        function_vals=np.emtpy(len(vals))
        for i in range(0,len(vals)):
            function_vals[i]=self.equation_val(vals[i])
        return function_vals



    
    
    def diff(self,var_of_diff):
        return sp.diff(self.equation,var_of_diff)
    
    def double_diff(self,var_of_diff):
        differentiation=self.diff(var_of_diff)
        return sp.diff(differentiation,var_of_diff)
        
    
    def diff_value(self,value,var_of_diff):
        differentiation=self.diff(var_of_diff)
        return float((differentiation.subs({var_of_diff:value})).evalf())
    
    def double_diff_val(self,val,var_of_diff):
        return float((self.double_diff(var_of_diff).subs({var_of_diff:val})).evalf())
    
    #Bisection-Method
    #Inbuilt error is set ot 0,005
    def bisection_method(self,positive_val,negative_val,error=0.005,max_iteration=1000):
          val2=self.equation.subs({self.symbol:negative_val})
          val1=self.equation.subs({self.symbol:positive_val})
          positive_vals=np.empty(max_iteration)
          negative_vals=np.empty(max_iteration)
          mids=np.empty(max_iteration)
          iteration=0
          try:
           if(val1*val2>=0):
                raise wrong_val_inputs()
          except wrong_val_inputs as e:
               print("Both inputs values are giving same sign number as output")

          while True:
               mid=(positive_val+negative_val)/2
               
               if(abs(self.equation_val(mid))<error):
                    return mid,mids[:iteration],positive_vals[:iteration],negative_vals[:iteration],iteration
               else:
                if(self.equation_val(positive_val)/abs(self.equation_val(positive_val))*self.equation_val(mid)/abs(self.equation_val(mid))<0):
                    positive_vals[iteration]=positive_val
                    negative_vals[iteration]=negative_val
                    negative_val=mid

                else:
                    positive_vals[iteration]=positive_val
                    negative_vals[iteration]=negative_val
                    positive_val=mid

                mids[iteration]=mid
                iteration+=1

    

     #Checbychev-Method
    #Inbuilt error value is set to 0.005
    def chebychev(self,val=1,error=0.005,max_iteration=1000):
        vals=np.empty(max_iteration)
        diff_vals=np.empty(max_iteration)
        second_diff_vals=np.empty(max_iteration)
        changes=np.empty(max_iteration)
        iteration=0
        while True:
         equation_val=((self.equation_val(val)))
         if(abs(equation_val)<error):
            return val,vals[:iteration],diff_vals[:iteration],second_diff_vals[:iteration],changes[:iteration],iteration
         else:
            diff_val=(self.diff_value(val,self.symbol))
            second_diff_val=(self.double_diff_val(val,self.symbol))
            change=(-1*(equation_val/diff_val))-((equation_val**2)*second_diff_val)/(2*(diff_val**3))
            vals[iteration]=val
            diff_vals[iteration]=diff_val
            second_diff_vals[iteration]=second_diff_val
            changes[iteration]=change
            val=val+change
            iteration+=1


            

    # Newton Rapison Method
    # inbulit error is set to 0.005
    def newton_rapison(self,val=0, error=0.005,max_iteration=1000):
        vals=np.empty(max_iteration)
        diff_vals=np.empty(max_iteration)
        iteration=0
        while True:
          equation_val=self.equation_val(val)
          if(abs(equation_val)<error):
            return val,vals[:iteration],diff_vals[:iteration]
          else:
            diff_val=self.diff_value(val,sp.symbols(self.symbol))
            vals[iteration]=val
            diff_vals[iteration]=diff_val
            iteration+=1
            val=val-(equation_val/diff_val)

    
    
    #Regular - Falsi Method
    #Buitin error is 0.005
    def regular_falsi(self,positive_val,negative_val,error=0.005,max_iteration=1000):
        positive_vals=np.empty(max_iteration)
        negative_vals=np.empty(max_iteration)
        function_positive_vals =np.empty(max_iteration)
        function_negative_vals=np.empty(max_iteration)
        function_vals=np.empty(max_iteration)
        iteration=0
        function_positive_val=self.equation_val(positive_val)
        function_negative_val=self.equation_val(negative_val)

        try:
            if(function_positive_val*function_negative_val>0):
                raise wrong_val_inputs
        except:
            print("Both inputs values are giving same sign number as output")
        while True:
            solution=positive_val-((function_positive_val)/(function_positive_val-function_negative_val))*(positive_val-negative_val)
            if( abs(self.equation_val(solution))<=error):
                return solution,function_vals[:iteration],positive_vals[:iteration],negative_vals[:iteration],function_positive_vals[:iteration],function_negative_vals[:iteration],iteration
                
            else:
               function_val=self.equation_val(solution)
               positive_vals[iteration]=positive_val
               negative_vals[iteration]=negative_val
               function_vals[iteration]=solution
               function_positive_vals[iteration]=function_positive_val
               function_negative_vals[iteration]=function_negative_val
               if(function_positive_val*function_val<0):
                   negative_val=solution
                   
                   
               else:
                   positive_val=solution

            iteration+=1

               
               




               



   




        



# Example usage
x,y = sp.symbols('x y')  # Define the symbol
a = Roots(x**3-9, 'x')  # Pass the equation and symbol as strings
 # Call the diff method with the symbol
# print(a.diff_value(5,x))
# on_method(0,5,0.005)


# val,vals,diff_vals,second_diff_val,changes,iteration=(a.chebychev())
# print(val)
# print(diff_vals)
# print(second_diff_val)
# print(changes)
# print(iteration)

# val,vals,diff_vals=a.newton_rapison(5)
# print(val ,"\n", vals ,"\n", diff_vals)

# mid,mids,positive_vals,negative_vals,iteration=a.bisection_method(0,5)
# print(mid, "\n",mids,"\n",positive_vals,"\n",negative_vals,"\n",iteration)

# solution,function_vals,positive_vals,negative_vals,function_positive_vals,function_negative_vals,iteration=a.regular_falsi(0,5)
# print(solution)
# print(function_vals)
# print(function_negative_vals)
# print(function_positive_vals)
# print(negative_vals)
# print(positive_vals)

