import c4d
 
def add_custom(name, color):


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


color_custom=c4d.Vector(1,0.545,0.094) # Layer Color
add_custom("_custom divider_",color_custom)

