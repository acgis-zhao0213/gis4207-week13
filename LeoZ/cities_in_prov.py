import sys


prov_codes = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 
              'PE', 'NS', 'NL', 'YT', 'NT', 'NU']

def main():
    fc   = sys.argv[1]
    # in_field = sys.argv[2]
    # out_ws  = sys.argv[3]
    prov = sys.argv[2].upper()
    if prov not in prov_codes:
        print (f'Invalid prov.  Must be one of {", ".join(prov_codes)}')
        exit()

    import arcpy

    ws = r'..\..\..\..\data\Canada\Canada.gdb'
    arcpy.env.workspace = ws
    prov_field = arcpy.AddFieldDelimiters(ws, 'Prov')
    wc =  f"{prov_field}='{prov}'"
  
    arcpy.AddMessage('Name,Prov,Longitude,Latitude')
    with arcpy.da.SearchCursor(fc, 
                               ['PROV','Name', 'SHAPE@XY'], 
                               where_clause=wc) as cursor:
        count = 0
        for row in cursor:
            count += 1
            name = row[1]
            prov = row[0]
            longitude = row[2][0]
            latitude = row[2][1]
            arcpy.AddMessage (f'{name},{prov},{longitude},{latitude}')
        arcpy.AddMessage(f'There are {count} cities in the above list')


if __name__ == '__main__':
    main()