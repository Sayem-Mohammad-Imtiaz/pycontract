from src.contracts import contract
import tensorflow as tf

from src.contracts.library import Extension
from src.contracts.syntax import ParsingTmp


class CustomClass(object):
    pass

@contract(x='tf_tensor', y='int,>0')
def f(x,y):
    pass


# f(CustomClass()) # OK

# f(42) # fails
#
# contracts.interface.ContractNotRespected: Breach for argument 'x' to f().
# Expected type 'CustomClass', got <type 'int'>.
# checking: CustomClass   for value: Instance of <type 'int'>: 42

# print(ParsingTmp.keywords,list(Extension.registrar.keys()))
my_variable = tf.Variable(tf.zeros([1, 2, 3]))
a=tf.constant([1, 2, 3, 4, 5, 6])
f(a, -1)