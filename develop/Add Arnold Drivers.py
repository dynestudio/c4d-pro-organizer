"""
Pro Organizer - Scripts Package v0.9.6
Thanks for download - for commercial and personal uses.
The Pro Organizer v1.0 granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Improve your scene organization and your projects workflow with a better way.
Hold Shift or ALT or CTRL/CMD while execute the script to put the dividers up or down or child of the objects. (works only with dividers and group dividers)
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

Pro Organizer - Scripts Package v0.9 belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
 
#global ids
color_ArnoldDrivers=c4d.Vector(0.8,0.2,0.4) # layer Color

def add_ArnoldDrivers(name, color):

   #layers ops
   root = doc.GetLayerObjectRoot()
   layersList = root.GetChildren() 

   names=[]    
   layers=[]
   
   #start undo action
   doc.StartUndo()

   for l in layersList:
       n=l.GetName()
       names.append(n)
       layers.append((n,l))

   if not name in names:

       layer = c4d.documents.LayerObject() #new Layer
       layer.SetName(name)  
       layer[c4d.ID_LAYER_COLOR] = color
       layer_settings = {'solo': False, 'view': False, 'render': True, 'manager': True, 'locked': False, 'generators': False, 'deformers': False, 'expressions': False, 'animation': False}
       layer.SetLayerData(doc, layer_settings)
       layer.InsertUnder(root)

   else:
       for n, l in layers:
           if n == name:
               layer=l
               break 

   #prevent copies in obj manager
   null = doc.SearchObject(name)
   if not null:
     #divider ops
     null = c4d.BaseObject(5140)
     null[c4d.ID_BASELIST_NAME] = name #name of null
     null[c4d.ID_LAYER_LINK] = layer
     null[c4d.NULLOBJECT_DISPLAY] = 14
     doc.InsertObject(null)
   else:
        None

   #put the divider last in the obj manager
   objectsList = doc.GetObjects()
   firstObj = doc.GetFirstObject()
   lastObj = objectsList[-1]
   firstObj.InsertAfter(lastObj)

   doc.AddUndo(c4d.UNDOTYPE_NEW, null)

   #end undo action
   doc.EndUndo()
   
   #update scene
   c4d.EventAdd()

if __name__=='__main__':
  add_ArnoldDrivers("_Arnold Drivers_",color_ArnoldDrivers)