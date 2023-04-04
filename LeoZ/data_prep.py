import os
import sys

arcpy = None

def main():
    global arcpy
    print('Usage:  data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>')
    

    in_gdbs_base_folder = sys.argv[1]
    out_gdb = sys.argv[2]
    out_feature_dataset = sys.argv[3]

    if not os.path.exists(in_gdbs_base_folder):
        print(f'{in_gdbs_base_folder} does not exist.')
        sys.exit(0)

    import arcpy
    arcpy.env.overwriteOutput = True
    
    arcpy.env.workspace = in_gdbs_base_folder
    ws_list = arcpy.ListWorkspaces()
    arcpy.env.workspace = ws_list[0]
    first_fc = arcpy.ListFeatureClasses()[0]
    sr = arcpy.da.Describe(first_fc)['spatialReference']
    arcpy.management.CreateFileGDB(out_folder_path=os.path.dirname(out_gdb),
                                   out_name=os.path.basename(out_gdb))
    arcpy.management.CreateFeatureDataset(out_dataset_path=out_gdb,
                                          out_name=out_feature_dataset,
                                          spatial_reference=sr)
    out_path = os.path.join(out_gdb, out_feature_dataset)
    for ws in ws_list:
        arcpy.env.workspace = ws
        fc_list = arcpy.ListFeatureClasses()
        for fc in fc_list:
            print(f'Copying {fc} ...')
            arcpy.FeatureClassToFeatureClass_conversion(fc,
                                                        out_path,
                                                        out_name=fc)
    arcpy.env.workspace = out_path
    print('Checking output ...')
    for fc in arcpy.ListFeatureClasses():
        print('  ', fc)
    print('Done')


if __name__ == '__main__':
    main()
