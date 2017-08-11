import bpy

bl_info = {
    "name": "Object Clear View",
    "author": "Frankie",
    "version": (0, 2),
    "blender": (2, 79, 0),
    #"location": "View3D > Add > Mesh > New Object",
    "description": "shows objects with name containing string clearly, assign bpy.ops.object.clear_view('INVOKE_DEFAULT') to a key",
    "warning": "",
    "wiki_url": "",
    "category": "3D view",
    }

class ClearView(bpy.types.Operator):
    bl_idname = "object.clear_view"
    bl_label = "Object Clear View"

    my_string = bpy.props.StringProperty(name="String to isolate")
    bool1 = bpy.props.BoolProperty(name="Keep body group", default = True)
    bool5 = bpy.props.BoolProperty(name="Keep rig", default = True)
    bool2 = bpy.props.BoolProperty(name="Move", default = True)
    bool3 = bpy.props.BoolProperty(name="Keep others visible")
    bool4 = bpy.props.BoolProperty(name="Ignore world", default = True)

    def execute(self, context):
        s = self.my_string.lower()
        i = 0
        bodyobjects = []

        for sl in bpy.context.scene.layers:
            bpy.context.scene.layers[i] = False
            i += 1

        #finding objects
        for o in bpy.context.scene.objects:
            if self.bool3 == False:
                o.hide = True
            if (s in o.name.lower()):
                if self.bool4 == True and "world" in o.name.lower():
                    print ("continune")
                    continue
                o.hide = False
                i = 0
                for l in o.layers:
                    if (l == True):
                        bpy.context.scene.layers[i] = True
                    i += 1

        #Keep body visible
        if self.bool1 == True:
            for o in bpy.context.scene.objects:
                for g in bpy.data.groups:
                    if g.name.lower() == "body":
                        for go in g.objects:
                            if go.name == o.name:
                                o.hide = False
                                bodyobjects.append(o)
                                i = 0
                                for l in o.layers:
                                    if (l == True):
                                        bpy.context.scene.layers[i] = True
                                    i += 1

        #Keep rig visible
        if self.bool5 == True:
            for o in bpy.context.scene.objects:
                if o.type == 'ARMATURE':
                    bodyobjects.append(o)
                    o.hide = False
                    i = 0
                    for l in o.layers:
                        if (l == True):
                            bpy.context.scene.layers[i] = True
                        i += 1

        #Move objects +1 on x
        if self.bool2 == True:
            i = 0
            for o in bpy.context.scene.objects:
                if "hit_" in o.name.lower():
                    continue
                if o.hide == False:
                    if o not in bodyobjects:
                        o.location[0] = i
                        i += 1
                        for m in o.modifiers:
                            if m.type == "ARMATURE":
                                m.show_viewport = False

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(ClearView)

def unregister():
    bpy.utils.unregister_class(ClearView)

if __name__ == '__main__':
    register()

# test call
# bpy.ops.object.clear_view('INVOKE_DEFAULT')