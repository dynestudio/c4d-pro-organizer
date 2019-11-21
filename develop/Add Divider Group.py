"""
Pro Organizer Scripts Package
Thanks for purchasing - for commercial and all uses.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Organize your everyday objects workflow with a better way in your projects.
Hold Shift or ALT or CTRL/CMD while execute the script to put the dividers up or down or child of the objects. (works only with dividers and group dividers)
Version: 1.0
Date: 04/05/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

"""

import c4d
 
color_divider=c4d.Vector(1,1,1) # Layer Color
 
def add_divider(name, color):


       root = doc.GetLayerObjectRoot()
       LayersList = root.GetChildren() 

       names=[]    
       layers=[]
       for l in LayersList:
           n=l.GetName()
           names.append(n)
           layers.append((n,l))


       if not name in names:


           c4d.CallCommand(100004738) # New Layer
           LayersList = root.GetChildren() 
           layer=LayersList[-1]
           layer.SetName(name)  
 
           layer[c4d.ID_LAYER_COLOR] =color 

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       Null = c4d.BaseObject(5140)
       Null[c4d.ID_BASELIST_NAME] = "______________________________Group Name" #Name of null
       Null[c4d.ID_LAYER_LINK] = layer
       Null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(Null)
       
       c4d.EventAdd()
       
def insert_up():
      ActiveDocument = c4d.documents.GetActiveDocument()
      ObjectsList = doc.GetObjects()
      FirstObject = doc.GetFirstObject()
      if FirstObject == None: return
      ActiveObject = doc.GetActiveObject()
      if ActiveObject == None: return
      FirstObject.InsertAfter(ActiveObject)

def insert_down():
      ActiveDocument = c4d.documents.GetActiveDocument()
      ObjectsList = doc.GetObjects()
      FirstObject = doc.GetFirstObject()
      if FirstObject == None: return
      ActiveObject = doc.GetActiveObject()
      if ActiveObject == None: return
      FirstObject.InsertBefore(ActiveObject)

def insert_child():
      ActiveDocument = c4d.documents.GetActiveDocument()
      ObjectsList = doc.GetObjects()
      FirstObject = doc.GetFirstObject()
      if FirstObject == None: return
      ActiveObject = doc.GetActiveObject()
      if ActiveObject == None: return
      FirstObject.InsertUnder(ActiveObject)

def Shorcuts_Functions():

    doc = c4d.documents.GetActiveDocument()
    bc = c4d.BaseContainer()

    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
        if  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT: 
            add_divider("_dividers_",color_divider)
            insert_up()
             
        elif  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: 
            add_divider("_dividers_",color_divider)
            insert_down()
            
        elif  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QCTRL: 
            add_divider("_dividers_",color_divider)
            insert_child()
             
        else:
            add_divider("_dividers_",color_divider)

    c4d.EventAdd()

if __name__=='__main__':
    Shorcuts_Functions()