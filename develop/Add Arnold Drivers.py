"""
Pro Organizer Scripts Package
Thanks for purchasing - for commercial and all uses.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Organize your everyday workflow with a better way your projects.
Hold Shift or ALT or CTRL/CMD while execute the script to put the dividers up or down or child of the objects. (works only with dividers)
Version: 1.0
Date: 04/05/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

"""

import c4d
 
def add_ArnoldDrivers(name, color):


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
       Null[c4d.ID_BASELIST_NAME] = name #Name of null
       Null[c4d.ID_LAYER_LINK] = layer
       Null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(Null)
       
       c4d.EventAdd()


color_ArnoldDrivers=c4d.Vector(0.8,0.2,0.4) # Layer Color
add_ArnoldDrivers("_Arnold Drivers_",color_ArnoldDrivers)

