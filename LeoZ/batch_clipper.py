import os
import sys


def main():
    global arcpy
    import arcpy
    arcpy.env.overwriteOutput = True

    in_ws   = sys.argv[1]
    clip_ws = sys.argv[2]
    out_ws  = sys.argv[3]

    for ws in [in_ws, clip_ws, out_ws]:
        if not arcpy.Exists(ws):
            print( "In Workspace '%s' does not exist" % in_ws)
            sys.exit()

    arcpy.env.workspace = in_ws
    in_fc_list = arcpy.ListFeatureClasses()

    arcpy.env.workspace = clip_ws
    clip_fc_list = arcpy.ListFeatureClasses()

    for in_fc in in_fc_list:
        in_fc_path = os.path.join(in_ws, in_fc)
        in_fc_base = arcpy.Describe(in_fc_path).basename
        for clip_fc in clip_fc_list:
            clip_fc_path = os.path.join(clip_ws, clip_fc)
            clip_fc_base = arcpy.Describe(clip_fc_path).basename
            out_fc  = f'{clip_fc_base}_{in_fc_base}'
            out_fc_path = os.path.join(out_ws, out_fc)
            print( (f'{out_fc} ...'))
            arcpy.Clip_analysis(in_fc_path,
                                clip_fc_path,
                                out_fc_path)

    def usage():
        msg=arcpy.GetParameterAsText(0)
        arcpy.AddMessage(msg)
    sys.exit(0)
if __name__ == '__main__':
    main()
