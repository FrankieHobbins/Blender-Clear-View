import bpy

class ClearView(bpy.types.Operator):
    bl_idname = "object.clear_view"
    bl_label = "Object Clear View"

    my_string = bpy.props.StringProperty(name="String to isolate")
    bool1 = bpy.props.BoolProperty(name="Keep Body")
    bool2 = bpy.props.BoolProperty(name="Move")
    bool3 = bpy.props.BoolProperty(name="Keep others visible")

    def execute(self, context):
        s = self.my_string        
        i = 0

        for sl in bpy.context.scene.layers:
            bpy.context.scene.layers[i] = False
            i += 1

        for o in bpy.context.scene.objects:
            if self.bool3 == False:
                o.hide = True
            if (s in o.name or self.bool1 == True and "body" in o.name):
                o.hide = False
                i = 0
                for l in o.layers:
                    if (l == True):
                        bpy.context.scene.layers[i] = True
                    i += 1
                    
        if self.bool1 == True:
            print ("keeping body")
            
        if self.bool2 == True:
            print ("moving all visible objects in 1m increments to the right on x")
            
            i = 0
            for o in bpy.context.scene.objects:
                if o.hide == False:
                    o.location[0] = i
                    i += 1
                    for m in o.modifiers:
                        if m.type == "ARMATURE":
                            m.show_viewport = False
                                    
                    if self.bool3 == True:
                        print ("keeping other objects visible")            
                        
            
        
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(ClearView)

# test call
bpy.ops.object.clear_view('INVOKE_DEFAULT')