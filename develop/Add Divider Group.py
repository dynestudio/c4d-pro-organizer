"""
Pro Organizer Scripts Package
Thanks for purchasing - for commercial and all uses.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Organize your everyday objects workflow with a better way in your projects.
Hold Shift or ALT or CTRL/CMD while execute the script to put the dividers up or down or child of the objects. (works only with dividers and group dividers)
Version: 1.0
Date: 22/05/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

"""

import c4d
from c4d import gui
 
#Global Variables

LBL_INFO = 1000
D_NAME = 10001
GROUP_OPTIONS = 20000
BTN_OK = 20001
BTN_CANCEL = 20002
color_divider=c4d.Vector(1,1,1) # Layer Color
 
# Dialog for renaming objects
class OptionsDialog(gui.GeDialog):
  def CreateLayout(self):
    self.SetTitle('Add Divider Group')
    self.AddStaticText(LBL_INFO, c4d.BFH_LEFT, name='Group Name:') 
    self.AddEditText(D_NAME, c4d.BFH_SCALEFIT)
    self.SetString(D_NAME, 'Write Divider Group Name')  # Default 'find' string.
    # Buttons - an Ok and Cancel button:
    self.GroupBegin(GROUP_OPTIONS, c4d.BFH_CENTER, 2, 1)
    self.AddButton(BTN_OK, c4d.BFH_SCALE, name='OK')
    self.AddButton(BTN_CANCEL, c4d.BFH_SCALE, name='Cancel')
    self.GroupEnd()
    self.ok = False
    return True
 
  # React to user's input:
  def Command(self, id, msg):
    if id==BTN_CANCEL:
      self.Close()
    elif id==BTN_OK:
      self.ok = True
      self.option_find_string = self.GetString(D_NAME)
      self.Close()
    return True
 
def add_divider(name, color):

         # Open the options dialogue to let users choose their options.
       dlg = OptionsDialog()
       dlg.Open(c4d.DLG_TYPE_MODAL, defaultw=300, defaulth=50)
       if not dlg.ok:
          return

       root = doc.GetLayerObjectRoot()
       LayersList = root.GetChildren() 

       names=[]    
       layers=[]
       for l in LayersList:
           n=l.GetName()
           names.append(n)
           layers.append((n,l))


       if not name in names:


           layer = c4d.documents.LayerObject() #New Layer
           layer.SetName(name)  
           layer[c4d.ID_LAYER_COLOR] =color
           layer_settings = {'solo': False, 'view': False, 'render': False, 'manager': True, 'locked': False, 'generators': False, 'deformers': False, 'expressions': False, 'animation': False}
           layer.SetLayerData(doc, layer_settings)
           layer.InsertUnder(root)

       else:
           for n, l in layers:
               if n ==name:
                   layer=l
                   break 

       null = c4d.BaseObject(c4d.Onull)
       null[c4d.ID_BASELIST_NAME] = "______________________________"+dlg.option_find_string #Name of null
       null[c4d.ID_LAYER_LINK] = layer
       null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(null)
       
       c4d.EventAdd()
       
def insert_up():
      activeDocument = c4d.documents.GetActiveDocument()
      objectsList = doc.GetObjects()
      firstObject = doc.GetFirstObject()
      if firstObject == None: return
      activeObject = doc.GetActiveObject()
      if activeObject == None: return
      firstObject.InsertAfter(activeObject)

def insert_down():
      activeDocument = c4d.documents.GetActiveDocument()
      objectsList = doc.GetObjects()
      firstObject = doc.GetFirstObject()
      if firstObject == None: return
      activeObject = doc.GetActiveObject()
      if activeObject == None: return
      firstObject.InsertBefore(activeObject)

def insert_child():
      activeDocument = c4d.documents.GetActiveDocument()
      objectsList = doc.GetObjects()
      firstObject = doc.GetFirstObject()
      if firstObject == None: return
      activeObject = doc.GetActiveObject()
      if activeObject == None: return
      firstObject.InsertUnder(activeObject)

def d_shorcuts_functions():

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
    d_shorcuts_functions()