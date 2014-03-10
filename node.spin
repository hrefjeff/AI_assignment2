'' =========================================================================== 
''
''  Author:     Jeffrey Allen 
''
''  Comments: This "object" is a container for the node matrix format. It includes
''  both local data for the fields of each element in the record as well as accessor
''  method to get and set the data in the record.
''
'' ===========================================================================

CON

  MAX_NODE_BUFFER = 1

VAR

  byte Xcoordinate
  byte Ycoordinate

CON
' -----------------------------------------------------------------------------
' GETTER METHODS FIRST, convention will be to prefix "read" methods with "_"   
' -----------------------------------------------------------------------------

PUB _xPos
  return ( Xcoordinate )

PUB _yPos
  return ( Ycoordinate )

CON
' -----------------------------------------------------------------------------
' SETTER METHODS NEXT, convention will be to suffix "write" methods with "_"   
' -----------------------------------------------------------------------------

PUB xPos_( vertPos )
  Xcoordinate := vertPos
 
PUB yPos_( horPos )
  Ycoordinate := horPos

 