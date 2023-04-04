import os
import sys

_shp_types = ['Point', 'Polyline', 'Polygon']


def main():
    global arcpy
 
    print("Usage: list08.py <root_folder> <Point|Polyline|Polygon> <out_file_name>")
       

    root_folder = sys.argv[1]
    shp_type = sys.argv[2]
    out_filename = sys.argv[3]

    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist.")
        sys.exit(0)

    if not shp_type in _shp_types:
        print(f'{shp_type} is not valid.')
        print('Must be one of Point, Polyline, or Polygon')
        sys.exit(0)

    import arcpy

    msg = f'Writing {shp_type} feature class names '
    msg += f'under {root_folder} to {out_filename} ...'
    print(msg)
    with open(out_filename, 'w') as outfile:
        walk = arcpy.da.Walk(root_folder, datatype="FeatureClass", type=shp_type)
        for ws, _, fc_list in walk:
            for fc in fc_list:
                print(os.path.join(os.path.abspath(ws), fc))
                outfile.write(os.path.join(os.path.abspath(ws), fc) + '\n')
    print('Done')


if __name__ == '__main__':
    main()
