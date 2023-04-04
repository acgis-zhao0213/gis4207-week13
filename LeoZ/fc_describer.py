import sys
import arcpy

def main():
    global arcpy
    fc = sys.argv[1]



    if not arcpy.Exists(fc):
        print(fc + " does not exist")
        sys.exit()

    dsc = arcpy.da.Describe(fc)

    msg=arcpy.GetParameterAsText(0)
    arcpy.AddMessage(fc)

    fields = dsc['fields']
    for field in fields:
        print(f'{field.name:15} {field.type:15} {field.length:>3}')
if __name__ == '__main__':
    main()
