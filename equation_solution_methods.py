import numpy as np
import sympy as sp

class invalid_parameters(Exception):
    pass

class shape_of_matrix_mismatch(Exception):
   print

#Give variables in the form of list of the variables  with comma in between
class system_of_equation:
    def __init__(self,variables, *equations):
        self.variables=sp.symbols(variables)
        self.equations = [sp.Eq(sp.sympify(eq.split("=")[0]), sp.sympify(eq.split("=")[1])) for eq in equations]


    def eq_to_matrix(self,which="both"):
        coeff_matrix,constants_matrix=sp.linear_eq_to_matrix(self.equations,self.variables)
        try:
         if(which=="left"):
            return  coeff_matrix
         elif(which=="right"):
            return constants_matrix
         elif(which=="both"):
            return coeff_matrix,constants_matrix
         else:
            raise invalid_parameters
        except:
           print("Invalid input is given in the which parameter")
           
           
    def row_reduced_eche(self):
        coeff_matrix,constants_matrix=self.eq_to_matrix("both")
        coeff_matrix_shape,constant_matrix_shape=coeff_matrix.shape,constants_matrix.shape
        try:
         if(coeff_matrix_shape[0]!=constant_matrix_shape[0] or constant_matrix_shape[1]!=1 ):
            raise shape_of_matrix_mismatch
        except:
           print("The shape of matrix is not in invalid shape, it should be in form (x,y),(x,1) but your left matrix shape is {} and right matrix shape is {}".format(coeff_matrix_shape,constant_matrix_shape))
        
        aug_matrix=np.empty((coeff_matrix_shape[0],coeff_matrix_shape[1]+constant_matrix_shape[1]))
        print(aug_matrix.shape)
        print(constant_matrix_shape)
        print(aug_matrix[:,-1])
        aug_matrix[:,-1]=constants_matrix
        
      #   aug_matrix[:,coeff_matrix_shape-1]=coeff_matrix
        
        
      #   print(aug_matrix[:][-1].shape)
      #   print(aug_matrix[:][:(coeff_matrix_shape[1]-1)].shape)
           
           
           






variables=["x", "y" ,"z"]
a=system_of_equation(variables,'4*x+5*y+6*z=9',"3*x+6*y+1*z=56")
# print(a.variables)
# print(a.equations)

# print(a.eq_to_matrix())
# print(a.left_matrix())
print(a.row_reduced_eche())


        


