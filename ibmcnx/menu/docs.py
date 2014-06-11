######
#  Menu for Community Scripts
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-04
#
#  License:       Apache 2.0
#
#  History:       Changed by Jan Alderlieste

import sys
import os
import ibmcnx.functions
import ibmcnx.menu.MenuClass
import java
from java.lang import String
from java.util import HashSet
from java.util import HashMap

#  Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile( "ibmcnx/loadCnxApps.py" )

global globdict
globdict = globals()

def docDocumentation():
    filename = raw_input( 'Path and Filename to Documentation file: ' )

    if (os.path.isfile( filename )):
        answer = raw_input( "File exists, Overwrite, Append or Abort? (O|A|X)" ).lower()
        if answer == "o":
            sys.stdout = open( filename, "w")
        elif answer == "a":
            sys.stdout = open( filename, "a")
        else:
            print "Exit"
            sys.exit()
    execfile( 'ibmcnx/doc/Documentation.py', globdict )
    
global globdict
globdict = globals()

doc = ibmcnx.menu.MenuClass.cnxMenu()
doc.AddItem( 'Show JVM Heap Sizes (ibmcnx/doc/JVMHeap.py)', ibmcnx.functions.docJVMHeap )
doc.AddItem( 'Show JVM Settings (ibmcnx/doc/JVMSettings.py)', ibmcnx.functions.docJVMSettings )
doc.AddItem( 'Show SystemOut/Err Log Sizes (ibmcnx/doc/LogFiles.py)', ibmcnx.functions.docLogFiles )
doc.AddItem( 'Show all used ports (ibmcnx/doc/Ports.py)', ibmcnx.functions.docPorts )
doc.AddItem( 'Show all used variables (ibmcnx/doc/Variables.py)', ibmcnx.functions.docVariables )
doc.AddItem( 'Create a file with all documentation (ibmcnx/doc/Documentation.py)', docDocumentation )
doc.AddItem( 'Back to Main Menu (cnxmenu_comcomm.py)', ibmcnx.functions.cnxBackToMainMenu )
doc.AddItem( "Exit", ibmcnx.functions.bye )

state_doc = 'True'

while state_doc == 'True':
    count = len( doc.menuitems )
    doc.Show()

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_doc = 0
    while not is_valid_doc :
        try :
                inputstring = 'Enter your choice [1-' + str( count ) + ']: '
                n = int ( raw_input( inputstring ) )

                if n <= count and n > 0:
                    is_valid_doc = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option." ) % n
        except ValueError, e :
                print ( "'%s' is not a valid integer." % e.args[0].split( ": " )[1] )
   #  n = input( "your choice> " )
    doc.Do( n - 1 )
