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
 
def all_organizer(name, color, objname):


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
       Null[c4d.ID_BASELIST_NAME] = objname
       Null[c4d.ID_LAYER_LINK] = layer
       Null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(Null)
       
       c4d.EventAdd()

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
       Null[c4d.ID_BASELIST_NAME] = "_______________________________________________________" #Name of null
       Null[c4d.ID_LAYER_LINK] = layer
       Null[c4d.NULLOBJECT_DISPLAY] = 14
       doc.InsertObject(Null)
       
       c4d.EventAdd()


color_divider=c4d.Vector(1,1,1) # Layer divider
color_lights=c4d.Vector(0.898,0.875,0.235) # Layer Lights
color_cams=c4d.Vector(0.235,0.388,0.898) # Layer Cams
color_geo=c4d.Vector(0.263,0.286,0.329) # Layer Geometry

if __name__=='__main__':
  add_divider("_dividers_",color_divider)
  all_organizer("_cameras_",color_cams, "_cameras_")
  add_divider("_dividers_",color_divider)
  all_organizer("_lights_",color_lights, "_lights_")
  add_divider("_dividers_",color_divider)
  all_organizer("_geometry_",color_geo, "_geo_")
  add_divider("_dividers_",color_divider)