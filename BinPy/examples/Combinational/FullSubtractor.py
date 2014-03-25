from __future__ import print_function
from BinPy.Combinational.combinational import *
""" Examples for FullSubtractor class """
print ("\n---Initializing the FullSubtractor class--- ")
print ("\n---Input is of the form [Bit1, Bit2, Borrow]")
print ("fs = FullSubtractor(0, 1, 0)")
fs = FullSubtractor(0, 1, 0)
print ("\n---Output of FullSubtractor")
print ("fs.output()")
print (fs.output())
print("Output is of the form [Difference, Borrow")
print ("\n---Input changes---")
print ("fs.setInput(1, 0) #Input at index 1 is changed to 0")
fs.setInput(1, 0)
print ("\n---New Output of the FullSubtractor---")
print (fs.output())
print ("\n---Changing the number of inputs---")
print ("No need to set the number, just change the inputs")
print ("Input length must be three")
print ("fs.setInputs(1, 0, 1)")
fs.setInputs(1, 0, 1)
print ("\n---To get the input states---")
print ("fs.getInputStates()")
print (fs.getInputStates())
print ("\n---New output of FullSubtractor---")
print (fs.output())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output of Full Subtractor to Connector conn---")
print ("fs.setOutput(0, conn) # sets the conn at index 0 ")
fs.setOutput(0, conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = AND(conn, 0)")
gate1 = AND(conn, 0)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
