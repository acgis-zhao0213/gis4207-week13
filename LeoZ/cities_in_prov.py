import sys

prov_codes = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 
              'PE', 'NS', 'NL', 'YT', 'NT', 'NU']
                    
    
def main():

    prov = sys.argv[0].upper()
    if prov not in prov_codes:
        print (f'Invalid prov.  Must be one of {", ".join(prov_codes)}')
        exit()

    import arcpy

    ws = r'..\..\..\..\data\Canada\Canada.gdb'
    arcpy.env.workspace = ws
    prov_field = arcpy.AddFieldDelimiters(ws, 'Prov')
    wc =  f"{prov_field}='{prov}'"
    fc = 'MajorCities'
    print ('Name,Prov,Longitude,Latitude')
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
            print (f'{name},{prov},{longitude},{latitude}')
        print (f'There are {count} cities in the above list')


if __name__ == '__main__':
    main()