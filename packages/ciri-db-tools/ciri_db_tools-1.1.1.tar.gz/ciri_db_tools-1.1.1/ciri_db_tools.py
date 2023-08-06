import pandas as pd
from sqlite3 import Error
import os
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
import psycopg2;
import base64
import json
import requests
import subprocess
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolSetCursor
import datetime

def csvCreatePg(csv_loc_input, pg_conn_input):
    '''
    Writes CSV/EXCEL file(s) data to a Postgres database.
               Parameters:
                    csv_loc_input (String): Path to directory containg the csv/xlsx(s) file
                    pg_conn_input (String): The postgres database connection URI
    '''

    PG_CONN = pg_conn_input
    path = csv_loc_input

    table_list = []
    table_name_list = []
    try:
        print("Initializing and constructing list of dataframes...")
        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                fullpath = path + "/" + filename
                pdCsv = pd.read_csv(fullpath, encoding="ISO-8859-1")
                table_list.append(pdCsv)
                table_name_list.append(filename.split(".")[0])
            if filename.endswith(".xlsx"):
                fullpath = path + "/" + filename
                pdExcel = pd.read_excel(fullpath)
                table_list.append(pdExcel)
                table_name_list.append(filename.split(".")[0])
        connection = create_engine(PG_CONN)

    except Error as e:
        print(e)
    finally:
        print("Dataframe list complete. Reading dataframes to target PG database...")
    try:
        table_index = 0
        for table in table_list:
            table_list[table_index].to_sql(table_name_list[table_index], connection, index=False)
            table_index+=1
    except Error as e:
        print(e)
    finally:
        print("Dataframes read to target PG database complete.")

def csvCreateSqlite(csv_loc_input, out_input):
    path = csv_loc_input
    table_list = []
    table_name_list = []
    try:
        print("Start [1]: Initializing and constructing list of dataframes")
        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                fullpath = path + "/" + filename
                pdCsv = pd.read_csv(fullpath, encoding="ISO-8859-1")
                table_list.append(pdCsv)
                table_name_list.append(filename.split(".")[0])
            if filename.endswith(".xlsx"):
                fullpath = path + "/" + filename
                pdExcel = pd.read_excel(fullpath)
                table_list.append(pdExcel)
                table_name_list.append(filename.split(".")[0])
    except Error as e:
        print(e)
    finally:
        print("Done [1]: Dataframe list complete")
        print("Start [2]: Reading dataframes to test SQLite database")
    try:
        table_index = 0
        for table in table_list:
            dbname = "test"
            tbname = table_name_list[table_index]
            if '-' in table_name_list[table_index]:
                dbname = table_name_list[table_index].split('-')[0]
                tbname = table_name_list[table_index].split('-')[1]
            sqlite_output_location = out_input
            connection = sqlite3.connect(sqlite_output_location + dbname + ".db")
            sqliteCursor = connection.cursor()
            table_list[table_index].to_sql(tbname, connection, index=False)
            table_index+=1
    except Error as e:
        print(e)
    finally:
        print("Done [2]: Done reading dataframes to test SQLite database.")

def scrambleData(conn_loc_str, output_dest):
    '''
    Scrambles int, float, and certain sring data in a SQLite database.
               Parameters:
                    conn_loc_str (String): SQLite connection string/path \n
                    output_dest (String): 'example.db' for relative/same dir or 'C://absolutepath/to/example.db for other dir'

            Returns:
                    A new scrambled database at output_dest
    '''
    input_conn = sqlite3.connect(conn_loc_str)
    output_conn = create_engine('sqlite:///' + output_dest)
    i_cursor = input_conn.cursor()
    i_cursor.execute('SELECT name from sqlite_master where type= "table"')
    tables = i_cursor.fetchall()
    i = 0
    pdTblList = []
    redacted_prov_full = ["Newfoundland", "Labrador", "Nova Scotia", "Prince Edward Island", "New Brunswick",
    "Quebec", "Ontario", "Manitoba", "Saskatchewan", "Alberta",
    "British Columbia", "Yukon Territory", "Northwest Territories", "Nunavut"]
    censor_prov_full = ["Maine", "New Hampshire", "Vermont", "New York",
    "Pennysylvania", "Ohio", "Michigan", "Minnesota", "North Dakota",
    "Montana", "Idaho", "Washington", "Alaska", "Mexico"]
    redacted_prov_abbr = ["NL", "NF", "LB", "NS", "PEI", "NB", "QC", "ONT", "MB", "SK", "AB", "BC", "YT", "NWT", "NV"] #15
    censor_prov_abbr = ["LA", "MNE", "NH", "VM", "NY", "PEN", "OH", "MCH", "MIN", "ND", "MON", "ID", "WSH", "AL", "MX"]
    for table in tables:
        tables[i] = table[0]
        pdTblList.append(pd.read_sql('SELECT * FROM ' + table[0], input_conn))
        i+=1
    h = 0
    for df in pdTblList:
        k = 0
        while k < len(redacted_prov_full):
            df.replace(redacted_prov_full[k], censor_prov_full[k], True)
            df.replace(redacted_prov_abbr[k], censor_prov_abbr[k], True)
            k+=1
            
        df_colTypes = list(df.dtypes)
        df_colNames = list(df.columns)
        i = 0
        while i < len(df_colNames):
            offset = ''
            if df_colTypes[i] == "int64":
                offset = 1
            if df_colTypes[i] == "float64":
                # offset = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
                offset = 0.06       
            j = 0
            while j < len(df.index)-1:
                df.at[j, df_colNames[i]] = df.at[j, df_colNames[i]] + offset
                if df_colTypes[i] == "object":
                    print(df.at[j, df_colNames[i]])
                    line = str(df.at[j, df_colNames[i]])
                    b = 0
                    while b < len(redacted_prov_abbr):
                        line = line.replace(redacted_prov_abbr[b], censor_prov_abbr[b])
                        b+=1
                    print(line)
                    df.at[j, df_colNames[i]] = line
                j+=1
            i+=1
        df.to_sql(tables[h], output_conn, index=False)
        h+=1

def dbCreateCsv(pg_bool, sqlite_bool, out_input, tables_input, sqlite_loc, pg_conn_input):
    '''
    Writes the contents of a SQLITE or PG database to a CSV file.
               Parameters:
                    pg_bool (bool): Set to true if a Postgres database will be accessed.
                    sqlite_bool (bool): Set to true if a SQLite database will be accessed.
                    out_input (string): Specify the relative output path './path/to/example.csv'
                    tables_input (list of strings): List of (string) tables to be accessed.
                    sqlite_loc (string): Directory of the sqlite database, if applicable.
                    pg_conn_input (string): Postgres connection URI, if applicable.
                Returns:
                    A csv file containg the specified database contents.
    '''
    # Set to either SQLite or PG database
    PG2CSV = pg_bool
    SQLITE2CSV = sqlite_bool

    TARGET_TABLES = tables_input 

    # Where you want the CSV files to generate.
    out_input = out_input + "/"
    RESULTPATH = out_input.replace("//", "/") 
    try:
        print("START")
        if SQLITE2CSV == True:
            print("SQLITE2CSV-START")
            SQLITE_LOCATION = sqlite_loc 
            for file in os.listdir(SQLITE_LOCATION):
                if file.endswith(".db"):
                    fullpath = sqlite_loc + "/" + file
                    fullpath.replace("//", "/")
                    conn = sqlite3.connect(fullpath)
                    filename = file.split(".")[0]
                    for table in TARGET_TABLES:
                        sqliteDF = pd.read_sql("SELECT * FROM " + table, conn)
                        sqliteDF.to_csv(RESULTPATH + filename + "-" + table + ".csv", mode='w', index=False)
            print("SQLITE2CSV-END")

        if PG2CSV == True:
            print("PG2CSV-START")
            PG_CONN = pg_conn_input 
            schema_conn = psycopg2.connect(PG_CONN)
            cursor = schema_conn.cursor()
            conn = create_engine(PG_CONN)
            for table in TARGET_TABLES:
                cursor.execute("SELECT table_schema FROM information_schema.tables WHERE table_name=%(tbl)s;", {"tbl": table})
                results = cursor.fetchall()
                for result in results:
                    pgDF = pd.read_sql("SELECT * FROM \"" + result[0] + "\".\"" + table + "\"", conn)
                    pgDF.to_csv(RESULTPATH + result[0] + "-" + table + ".csv", mode='w', index=False)
            print("PG2CSV-END")
    except Error as e:
        print(e)

    finally:
        print("END")

def github_copy(json_file_input, out_input):
    '''
    Copies a JSON file to a specified location from the CIRI_INFO github repo.
               Parameters:
                    json_file_input (String): Name of the specified json file in the ciri_info github repo.
                    out_input (String): Path to where the new file is '/path/to/example.json'.
                Returns:
                    A JSON file at the specified location.
                
    '''
    CIRI_INFO = "https://api.github.com/repos/cat-cfs/ciri_info"
    CONTENTS = "/contents"
    JSON = json_file_input 
    REPO_URL = CIRI_INFO + CONTENTS + JSON
    TOKEN = "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" #EXPIRES DEC. 17, 2022

    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v4+raw"
    }

    response = requests.get(REPO_URL, headers=headers)

    if response and response.status_code == 200:
        binary_content = base64.b64decode(response.json()["content"])
        content = binary_content.decode("utf-8")
        json_loads = json.loads(content)
        json_dumps = json.dumps(json_loads, indent=4)

        output_location = out_input
        with open(output_location, "w") as outfile:
            outfile.write(json_dumps)
        
    else:
        print(response)

def result_tables_json(db_input, us_input, pw_input, hs_input, pt_input, sch_input, out_input):
    '''
    Writes a results table and classifiers JSON file using data from a postgres database with a metadata schema containing a table_metadata.
               Parameters:
                    db_input, us_input, hs_input, pt_input, sch_input (String): Postgres DB credentials (Database, username, password, host, port, schema)
                    out_input (String): Path/to/file.json of result tables.
                Returns:
                    A classifiers.json file and a result_tables.json file.
    '''
    database = db_input 
    user = us_input 
    password = pw_input 
    host = hs_input 
    port = pt_input 
    pgConnection = 'postgresql://' + user + ':' + \
        password + '@' + host + ':' + port + '/' + database
    TABLE_SCHEMA = sch_input 
    OUTPUT_LOCATION = out_input 
    try:
        print("START")
        alchemyEngine = create_engine(pgConnection)
        dbConnection = alchemyEngine.connect()
        pgConn = psycopg2.connect(pgConnection)
        pgCursor = pgConn.cursor()

        basicIndicators = pd.read_csv(
        './indicators/basic_indicators.csv')

        pgCursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = %(t_schema)s;",
            {"t_schema": TABLE_SCHEMA})
        tables = pgCursor.fetchall()
        col_list = []
        result_tables = []
        classifiers = []

        for table in tables:
            t_identifier = ""
            description = ""
            table_aliases = []
            default_indicators = []
            default_classifiers = []
            user_defined_classifiers = []
            table_name = table[0]
            pgCursor.execute(
                "SELECT table_description FROM metadata.table_metadata WHERE table_name = %(t_name)s;", 
                {"t_name": table_name}
            )
            table_desc_results = pgCursor.fetchall()
            if len(table_desc_results) > 0:
                description = table_desc_results[0][0]
            table_aliases.append(table_name)
            pgCursor.execute(
                "SELECT \"DB_Filename\", \"CBM_project\", \"NIR_project\", \"NIR_year\", \"PT_Name\", \"ProjectID\", \"CanFI_ID\" FROM \"" +
                TABLE_SCHEMA + "\".\"" + table_name + "\";"
            )
            helper_results = pgCursor.fetchall()
            helper = helper_results[0]
            helper_cols = {
                "DB_Filename": helper[0],
                "CBM_project": helper[1],
                "NIR_project": helper[2],
                "NIR_year": helper[3],
                "PT_Name": helper[4],
                "ProjectID": helper[5],
                "CanFI_ID": helper[6],
            }
            pgCursor.execute(
                "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %(t_name)s AND table_schema = %(t_schema)s;",
                {"t_name": table_name, "t_schema": TABLE_SCHEMA}
            )
            columns = pgCursor.fetchall()
            for column in columns:
                column_name = column[0]
                col_list.append(column_name)
    
            index = 0
            for defaultIndicator in basicIndicators["Table"]:
                if defaultIndicator == table_name:
                    default_indicators.append(basicIndicators["Indicator"][index])
                index += 1

            t_dictObj = [
                {
                    "identifier": t_identifier,
                    "description": description,
                    "table_aliases": table_aliases,
                    "default_indicators": default_indicators,
                    "default_classifiers": default_classifiers,
                    "user_defined_classifiers": user_defined_classifiers,
                    "helper_columns": helper_cols
                }
            ]
            result_tables.append(t_dictObj[0])

        for col in col_list:
            pgCursor.execute(
                "SELECT classifier_name, classifier_type, classifier_description FROM metadata.classifier_metadata WHERE classifier_name = %(col)s;",
                {"col": col}
            )
            col_info = pgCursor.fetchall()
            tcol = []
            pgCursor.execute(
                "SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE column_name = %(col)s AND table_schema = %(schema)s;",
                {"col": col, "schema": TABLE_SCHEMA}
            )
            table_names = pgCursor.fetchall()
            for tn in table_names:
                tcol.append(tn[0])

            c_identifier = col
            classifier_type = ""
            aliases = []
            table_list = tcol
            description = ""
            resources = {}
            transformation_type = ""
            transformation_alias_name = ""
            transformation_action = ""
            transformations = {
                "type": transformation_type,
                "alias_name": transformation_alias_name,
                "action": transformation_action
            }

            if len(col_info) > 0:
                c_identifier = col_info[0][0]
                description = col_info[0][2]

            if len(tcol) == 1:
                classifier_type = "tertiary"
            if len(tcol) > 1 & len(tcol) < 6:
                classifier_type = "secondary"
            if len(tcol) > 5:
                classifier_type = "primary"

            for result_table in result_tables:
                result_table_name = result_table["table_aliases"][0]
                result_classifiers = result_table["default_classifiers"]
                result_indicators = result_table["default_indicators"]
                if result_table_name in table_list and c_identifier not in result_classifiers and c_identifier not in result_indicators and c_identifier not in helper_cols:
                    result_classifiers.append(c_identifier)

            c_dictObj = [
                {
                    "identifier": c_identifier,
                    "class": classifier_type,
                    "aliases": aliases,
                    "table_list": table_list,
                    "description": description,
                    "resources": resources,
                    "transformations": transformations
                }
            ]

            basicIndicators_List = []

            for basicIndicator in basicIndicators["Indicator"]:
                basicIndicators_List.append(basicIndicator)

            dictObjID = c_dictObj[0]["identifier"]
            if c_dictObj[0] not in classifiers:
                if dictObjID not in basicIndicators_List and dictObjID not in helper_cols:
                    classifiers.append(c_dictObj[0])

        query = 'SELECT "UserDefdClassID", "ClassDesc" FROM "' + TABLE_SCHEMA + '"."tblUserDefdClasses";'
        df = pd.read_sql(query, dbConnection)
        class_list = list(df["ClassDesc"])
        query = 'SELECT "UserDefdClassSetID", "Name" FROM "' + TABLE_SCHEMA + '"."tblUserDefdClassSets";'
        df = pd.read_sql(query, dbConnection)
        df[class_list] = df["Name"].str.split(pat=",", expand=True)
        df_classes = df.copy()
        
        for result_table in result_tables:
            table_name = result_table["table_aliases"][0]
            result_classifiers = result_table["default_classifiers"]
            result_indicators = result_table["default_indicators"]        
            user_defined_classifiers = result_table["user_defined_classifiers"]

            if "UserDefdClassSetID" in result_classifiers and table_name != "tblUserDefdClassSets":
                query = 'SELECT * FROM "' + TABLE_SCHEMA + '"."' + table_name + '";'
                df = pd.read_sql(query, dbConnection)
                df = df.merge(df_classes, how='left', on='UserDefdClassSetID')
                for col in df.columns:
                    if col not in result_classifiers and col not in result_indicators and col in class_list:
                        user_defined_classifiers.append(col)
        
        tableDictObj = {
            "result_tables": result_tables
        }
        classifierDictObj = {
            "classifiers": classifiers
        }

        json_classifiers = json.dumps(classifierDictObj, indent=4)
        json_result_tables = json.dumps(tableDictObj, indent=4)
        with open(OUTPUT_LOCATION + "classifiers.json", "w") as outfile:
            outfile.write(json_classifiers)
        with open(OUTPUT_LOCATION + "result_tables.json", "w") as outfile:
            outfile.write(json_result_tables)
        pgConn.close()
    except Error as e:
        print(e)

    finally:
        print("FINISH")

def pg2sqlite_copy(pgconn_input, loc_input):
    '''
    Copy the database contents of a Postgres database to a SQLite database.
               Parameters:
                    pgconn_input (String): Postgres connection URI of source database
                    loc_input (String): Path/to/sqlite.db of destination database
                Returns:
                    A SQLite database at the specified destination
    '''
    SQLITE_LOCATION = loc_input
    connectionString = pgconn_input
    try:
        #   Establish pg and sqlite3 db connections, get all table names from pg db
        pgConnection = psycopg2.connect(connectionString)
        pgCursor = pgConnection.cursor()
        pgCursor.execute(
            "SELECT schema_name FROM information_schema.schemata;"
        )
        schema_list_unfiltered = pgCursor.fetchall()
        schema_list = []
        IGNORE_SCHEMA = ['pg_toast', 'public', 'pg_catalog', 'information_schema']
        for item in schema_list_unfiltered:
            schema_list.append(item[0])
        for ign_sch in IGNORE_SCHEMA:
            schema_list.remove(ign_sch)

        for schema in schema_list:
            pgCursor.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = %(schema)s;", {"schema": schema})
            tables = pgCursor.fetchall()
            alchemyEngine = create_engine(connectionString)
            connection = sqlite3.connect(SQLITE_LOCATION + schema + ".db")
            
            # Convert pg db contents to pandas df, then write df to sqlite3 db
            for table in tables:
                dbConnection = alchemyEngine.connect()
                dbQuery = 'SELECT * from "' + schema + '"."' + table[0] + '";'
                dataFrame = pd.read_sql(dbQuery, dbConnection)
                pd.set_option('display.expand_frame_repr', False)
                dbConnection.close()
                try:
                    dataFrame.to_sql(table[0], connection,
                                    if_exists='replace', index=False)

                    #   For columns with datatypes not supported by sqlite (like TEXT[], change them to type TEXT)
                except Error as e:
                    invalidParameterIndex = int(
                        ''.join(filter(str.isdigit, str(e))))
                    err_col = dataFrame.head(0).columns[invalidParameterIndex]
                    dataFrame[err_col] = dataFrame[err_col].astype(str)
                    dataFrame.to_sql(table[0], connection,
                                    if_exists='replace', index=False)
            if connection:
                connection.close()
        #   Close connection and finish script execution.
    except Error as e:
        print(e)
    finally:
        print("POSTGRES TO SQLITE CONVERSION COMPLETE")

def geospatial_plot(us_input, pw_input, hs_input, prt_input, db_input, srid_input, shapes_input, points_input):
    '''
    Using *.shp files, create and display a geospatial dataplot using a Postgres database.
               Parameters:
                    us_input, pw_input, hs_input, prt_input, db_input (String): Postgres DB credentials (user, password, host, port, database)
                    srid_input (String): SRID for map projection, ie 'ESPG: 102001'
                    shapes_input (String): Name of the geometric shapes .shp file, ie 'sample_polygons.shp' -> 'sample_polygons'
                    points_input (String): Name of the geometric points .shp file, ie 'sample_points.shp' -> 'sample_points'
                    Reminder that *.shp will require all supporting files present in the directory as well
                Returns:
                    A matplot displaying the shape/point geospatia data provided
    '''
    # pip install geopandas

    # Heroku server credentials are commented out. 
    conn_host = hs_input
    conn_user = us_input

    # For localhost, change password to your own
    conn_pass = pw_input

    # Postgis will be the name of the new locally hosted spatial database
    conn_db = db_input
    conn_port = prt_input
    conn_uri = "postgres://" + conn_user + ":" + conn_pass + "@" + conn_host + ":" + str(conn_port) + "/" + conn_db
    srid = srid_input #'ESPG: 102001'       # SRID 102001 -> https://epsg.io/102001

    shapes = shapes_input
    points = points_input

    try:
        # Check if connecting to no DB localhost or DB present server (Heroku)
        if conn_host == "localhost":
            print("Connecting to localhost. \n")
            Postgres_Connection = psycopg2.connect(host=conn_host, user=conn_user, password=conn_pass, database="postgres",port=5432)
            Postgres_Connection.autocommit = True
            Postgres_Cursor = Postgres_Connection.cursor()
            Postgres_Cursor.execute("SELECT datname from pg_database where datname='postgis'")
            Postgres_Presence = Postgres_Cursor.fetchone()
            if Postgres_Presence is None:
                print("No database postgis found. Creating DATABASE postgis. \n")
                Postgres_Cursor.execute('CREATE DATABASE postgis;')
            Postgres_Connection.close()
        if conn_host != "localhost":
            print("Connecting to DB on non-localhost server. \n")

        # Establish Postgis database connection
        PostGIS_Connection = psycopg2.connect(
        host = conn_host,
        user = conn_user,
        password = conn_pass,
        database = conn_db,
        port = 5432
        )
        PostGIS_Cursor = PostGIS_Connection.cursor()

        # Check if database has postgis extension, add if not.
        PostGIS_Cursor.execute("SELECT extname from pg_extension WHERE extname='postgis';")
        PostGIS_Presence = PostGIS_Cursor.fetchone()
        if PostGIS_Presence is None:
            print("Postgis extension not found. Creating EXTENSION postgis.")
            PostGIS_Cursor.execute("CREATE EXTENSION postgis;")
            PostGIS_Cursor.execute("COMMIT;")
        
        # Execute shell script to store .shp files to the database. Make sure that the server does not contain these tables already.
        PostGIS_Cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name='%(sh)s';", {"sh": shapes})
        PostGIS_Polygon_Table = PostGIS_Cursor.fetchone()
        if PostGIS_Polygon_Table is None:
            print("No sample_polygons table found. Building TABLE %(sh)s.", {"sh": shapes})
            sample_polygons_cmd = 'shp2pgsql -s 4326 ' + shapes + '.shp' + shapes + ' | psql -q ' + conn_uri
            subprocess.call(sample_polygons_cmd, shell=True)
        
        PostGIS_Cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name='%(pt)s';", {"pt": points})
        PostGIS_Points_Table = PostGIS_Cursor.fetchone()
        if PostGIS_Points_Table is None:
            print("No sample_points table found. Building TABLE %(pt)s.", {"pt": points})
            sample_points_cmd = 'shp2pgsql -s 4326'+ points +'.shp' + points + ' | psql -q ' + conn_uri
            subprocess.call(sample_points_cmd, shell=True)
        
        # Query and list site_id and geom from sample points
        PostGIS_Cursor.execute('SELECT geom, site_id from %(pt)s ORDER BY site_id ASC', {"pt": points})
        geom_points_results = PostGIS_Cursor.fetchall()
        geom_points_array = []
        site_id_points_array = []
        for points_row in geom_points_results:
            geom_points_array.append(points_row[0])
            site_id_points_array.append(points_row[1])

        # Query and list site_id and geom from sample polygons
        PostGIS_Cursor.execute('SELECT geom, site_id from %(sh)s ORDER BY site_id ASC', {"sh": shapes})
        geom_polygons_results = PostGIS_Cursor.fetchall()
        geom_polygons_array = []
        site_id_polygons_array = []
        for polygons_row in geom_polygons_results:
            geom_polygons_array.append(polygons_row[0])
            site_id_polygons_array.append(polygons_row[1])
        
        # Convert geom points array into WKT points array
        points_array = []
        for geom_point in geom_points_array:
            PostGIS_Cursor.execute("SELECT ST_AsText('" + geom_point + "');")
            points_wkt_results = PostGIS_Cursor.fetchall()
            for point in points_wkt_results:
                points_array.append(point[0])
        
        # Convert geom polygons array into WKT polygons array
        polygons_array = []
        for geom_polygon in geom_polygons_array:
            PostGIS_Cursor.execute("SELECT ST_AsText('" + geom_polygon + "');")
            polygons_wkt_results = PostGIS_Cursor.fetchall()
            for polygon in polygons_wkt_results:
                polygons_array.append(polygon[0])
        
        # Convert WKT points and polygons to GeoDataFrames with the correct projection
        pt = gpd.GeoSeries.from_wkt(points_array)
        pt.to_crs = srid
        poly = gpd.GeoSeries.from_wkt(polygons_array)
        poly.to_crs = srid

        # Create a list of plots and a list of site arrays
        plots = []
        plots.append(pt)
        plots.append(poly)
        site_types = []
        site_types.append(site_id_points_array)
        site_types.append(site_id_polygons_array)

        # Plot each geodataframe object and its corresponding Site_ID text label
        site_type_index = 0
        for plot in plots:
            plot.plot()
            site_id_index = 0
            for coord in pt:
                site_id = "Site_ID: " + str(site_types[site_type_index][site_id_index])
                plt.text(coord.x, coord.y, site_id)
                site_id_index += 1
            site_type_index +=1

        # Display the two plots and close the PG connection
        plt.show()
        PostGIS_Connection.close()
    except Error as e:
        print("An error occured.")
        print(e)
    finally:
        print("Script executed.")

def sqlite2pg_copy(db_input, us_input, pw_input, hs_input, pt_input, dir_input):
    '''
    Copy the database contents of a SQLite database to a Postgres database.
               Parameters:
                    db_input, us_input, pw_input, hs_input, pt_input(String): Destination Postgres credentials (database, user, pass, host, port)
                    dir_input (String): Path/to/sqlite.db of source database
                Returns:
                    A Postgres database containing the SQLite data
    '''
    database = db_input
    user = us_input
    password = pw_input
    host = hs_input
    port = pt_input
    pgConnection = 'postgresql://' + user + ':' + \
        password + '@' + host + ':' + port + '/' + database
    SQLITE_DB_DIRECTORY = dir_input
    try:
        for file in os.listdir(SQLITE_DB_DIRECTORY):
            if file.endswith(".db"):
                filename = file.split(".")[0]
                #   Connect to sqlite DB, get all sqlite DB table names, and then create postgres connection
                connection = sqlite3.connect("./ciri_results_db/csvConverters/" + file) 
                sqliteCursor = connection.cursor()
                #connection.text_factory = lambda x: unicodedata(x, 'utf-8', 'ignore')
                sqliteCursor.execute('SELECT name from sqlite_master where type= "table"')
                tables = sqliteCursor.fetchall()
                alchemyEngine = create_engine(pgConnection)

                schemaQuery = "CREATE SCHEMA IF NOT EXISTS \"" + filename + "\";"
                schemataConn = psycopg2.connect(pgConnection)
                schemataCursor = schemataConn.cursor()
                schemataCursor.execute("SELECT schema_name from information_schema.schemata;")
                results = schemataCursor.fetchall()
                print(results)
                schemataCursor.execute(schemaQuery)
                schemataConn.commit()
                #   Get all data from each sqlite tbl, store it in a pandas df, connect to pg db and write the df to it
                for table in tables:
                    table_name = filename + "." + table[0]
                    dbQuery = 'SELECT * from "' + table[0] + '";'
                    dataFrame = pd.read_sql(dbQuery, connection)
                    pd.set_option('display.expand_frame_repr', False)
                    dbConnection = alchemyEngine.connect()

                    try:
                        dataFrame.to_sql(table[0], dbConnection, schema= filename,
                                        if_exists='replace', index=False)
                        dbConnection.close()

                        psycopg2Connection = psycopg2.connect(pgConnection)
                        pgCursor = psycopg2Connection.cursor()
                        #   Query the pg db for column headers with "list" in their name (ie column_list)
                        pgCursor.execute("SELECT column_name from information_schema.columns WHERE (table_name = '" +
                                        table_name + "') AND column_name SIMILAR TO '%l" + "ist%';")
                        columns = pgCursor.fetchall()

                        #   Retrieve the string value of every element under the TEXT "list" column
                        if (len(columns) > 0):
                            for column in columns:
                                tbl_name = table_name
                                col_name = column[0]
                                pgCursor.execute("SELECT " + col_name +
                                                " FROM " + tbl_name)
                                column_lists = pgCursor.fetchall()

                                #   Update all TEXT elements containing '[...]' to TEXT[] (array) friendly format '{...}'
                                for column_list in column_lists:
                                    sqr_br_list = column_list[0]
                                    cur_br_list = ""
                                    left_br_list = sqr_br_list.replace("[", '{')
                                    cur_br_list = left_br_list.replace("]", '}')
                                    pgCursor.execute("UPDATE " + tbl_name + " SET " + col_name + " = %(r0)s WHERE " +
                                                    col_name + " = (%(r1)s);", {"r0": cur_br_list, "r1": sqr_br_list})

                                #   Change the datatype of the list column from TEXT to TEXT[] and commit the changes
                                pgCursor.execute("ALTER TABLE " + tbl_name + " ALTER COLUMN " +
                                                col_name + " TYPE TEXT[] USING " + col_name + "::TEXT[];")
                                psycopg2Connection.commit()
                                psycopg2Connection.close()
                                print("SQLITE TO POSTGRES CONVERSION COMPLETE")
                    except Error as e:
                        print(e)
                        dbConnection.close()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def sqlite2pg_MetadataTbls(db_input, us_input, pw_input, hs_input, pt_input, loc_input, sqlite_name):
    '''
    Use a SQLite database to automatically create entries within a Postgres database's metadata.table_metadata
               Parameters:
                    db_input, us_input, pw_input, hs_input, pt_input(String): Destination Postgres credentials (database, user, pass, host, port)
                    loc_input (String): Path/to/sqlite.db of source database
                    sqlite_name (String): Name of the sqlite db, ie 'example' for 'example.db'
                Returns:
                    New entries in a PG database that store metadata (in metadata.table_metadata) about src's SQLite database's tables.
    '''
    database = db_input
    user = us_input
    password = pw_input
    host = hs_input
    port = pt_input
    pgConnection = 'postgresql://' + user + ':' + \
        password + '@' + host + ':' + port + '/' + database
    SQLITE_DB_LOCATION = loc_input

    tblNmDcDm = []
    try:
        print("start")
        conn = sqlite3.connect(SQLITE_DB_LOCATION)
        cursor = conn.cursor()
        cursor.execute('SELECT name from sqlite_master where type= "table"')
        tables = cursor.fetchall()
        for table in tables:
            col_list = []
            table_name = table[0]
            table_description = table_name + " description"
            database_name = sqlite_name
            cursor.execute("PRAGMA table_info('" + table_name + "')")
            columns = cursor.fetchall()
            for column in columns:
                col_list.append(column[1])
            col_string = str(col_list)
            col_string_1 = col_string.replace("[", "{")
            column_list = col_string_1.replace("]","}")
            tblNmDcDm.append({"table_name": table_name, "table_description": table_description, "database_name": database_name, "column_list": column_list})
        tblIgnoreList = []
        pgConn = psycopg2.connect(pgConnection)
        pgCursor = pgConn.cursor()
        pgCursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='metadata'")
        pgTbls = pgCursor.fetchall()
        for pgTbl in pgTbls:
            tblIgnoreList.append(pgTbl[0])

        pgCursor.execute("BEGIN TRANSACTION;")
        for item in tblNmDcDm:
            if item["table_name"] not in tblIgnoreList:
                print(item["table_name"])
                pgCursor.execute("INSERT INTO metadata.table_metadata (table_name, table_description, database_name, column_list) VALUES (%s, %s, %s, %s);",
                (item["table_name"], item["table_description"], item["database_name"], item["column_list"]))
        pgCursor.execute("COMMIT;")
        pgConn.close()
    except Error as e:
        print(e)

    finally:
        print("done")

def sqliteAddHelperCols(dir_input, supp_input, out_input, merge_input):
    '''
    Create csv(s) that contain sqlite database meta in additional to new columns aiding in data source identification
               Parameters:
                    dir_input (String): Path/to/sqlite.db(s) of source database(s)
                    supp_input (String): Path/to/supplementary.json used for helper column generation
                    out_input (String): Path/to/dest_directory
                    merge_input (Bool): True to aggregate data, False to not aggregate.
                Returns:
                    Csv file(s) containing sqlite database data with additional generated metadata.
                    Resulting files may be an aggregation of multiple DBs if desired.
    '''
    MERGE_RESULTS = merge_input 
    SQLITE_DIRECTORY = dir_input 
    SUPP_JSON_LOCATION = supp_input 
    OUTPUT_LOCATION = out_input 
    try:
        print("START")
        df_results = []
        df_results_names = []
        df_file_info = []
        access_supp = open(SUPP_JSON_LOCATION)
        load_obj_supp = json.load(access_supp)
        access_supp.close()
        dumps_supp = json.dumps(load_obj_supp)
        loads_supp = json.loads(dumps_supp)
        cbm_project_code = loads_supp["supplementary_data"][0]["CBM_project code"]
        pt_code_abbrevs = loads_supp["supplementary_data"][0]["PT_Abbrevs"]
        cbm_project_name_canfi_id = loads_supp["supplementary_data"][1]["CBM_project name"]
        pt_abbrev_code = loads_supp["supplementary_data"][1]["CanFI_IDs"]
        cbm_project_name_projectid = loads_supp["supplementary_data"][2]["CBM_project name"]
        projectIDs = loads_supp["supplementary_data"][2]["ProjectIDs"]
        pt_name_prov_terr = loads_supp["supplementary_data"][3]["Province/territory name (PT_Name)"]
        pt_name_canfi_ids = loads_supp["supplementary_data"][3]["CanFI_IDs"]
        pt_name = loads_supp["supplementary_data"][4]["PT_Name"]
        pt_name_abbrevs = loads_supp["supplementary_data"][4]["PT_Abbrevs"]

        drop_tables = ["tblPreDisturbanceAge", "tblSPUGroup", "tblSPUGroupLookup",
        "tblSVL", "tblUserDefdClassSetValues", "tblUserDefdSubclasses", "tblRandomSeed"]

        for filename in os.listdir(SQLITE_DIRECTORY):
            if filename.endswith(".db") and filename != "metadata.db" and filename != "postgis.db" and filename != "site_information.db":
                sqlConn = sqlite3.connect(SQLITE_DIRECTORY + "/" + filename)
                sqlCursor = sqlConn.cursor()

                DB_Filename = filename
                NIR_year = 2023
                PT_Abbrev = filename.split("_")[0]
                CBM_project = PT_Abbrev
                NIR_project = filename.split("_")[1] + "_" + filename.split("_")[2]
                PT_Name = "placeholder"
                ProjectID = "placeholder"
                CanFI_ID = "placeholder"
                for pt_name_item in pt_name_abbrevs:
                    if pt_name_abbrevs[pt_name_item] == PT_Abbrev:
                        PT_Name = pt_name_item
                DB_Modified = datetime.datetime.now()
                for project_item in projectIDs:
                    if project_item == PT_Abbrev:
                        ProjectID = projectIDs[project_item]
                for canfi_item in pt_name_canfi_ids:
                    if canfi_item == PT_Name:
                        CanFI_ID = pt_name_canfi_ids[canfi_item]

                for drop_table in drop_tables:
                    sqlCursor.execute('DROP TABLE IF EXISTS "' + drop_table +'";') 
                sqlCursor.execute('SELECT name from sqlite_master where type= "table"')
                tables = sqlCursor.fetchall()       

                sql_df_list = []
                for table in tables:
                    query = 'SELECT * FROM "' + table[0] + '";'
                    df = pd.read_sql(query, sqlConn)
                    df["DB_Filename"] = DB_Filename
                    df["CBM_project"] = CBM_project
                    df["NIR_project"] = NIR_project
                    df["NIR_year"] = NIR_year
                    df["PT_Name"] = PT_Name
                    df["ProjectID"] = ProjectID
                    df["CanFI_ID"] = CanFI_ID
                    df.astype({"ProjectID":int, "CanFI_ID": int})
                    df["temp_tableName"] = table[0]
                    df["DB_Date_Modified"] = DB_Modified
                    df_results.append(df)
                    df_results_names.append(table[0])
                df_file_info.append({"file":filename.split(".")[0], "t_len":len(tables)})
        final_list = []
        j = 0
        i = 0
        h = 0
        if MERGE_RESULTS == True:
            final_list = []
            for df_result_name in df_results_names:
                merge_list = []
                print(df_result_name)
                for df1_result in df_results:
                    print(df1_result["temp_tableName"][0])
                    if df1_result["temp_tableName"][0] == df_result_name:
                        merge_list.append(df1_result)
                merged_df = pd.concat(merge_list)
                final_list.append(merged_df)
            for final in final_list:
                final.drop(['temp_tableName'], axis=1, inplace=True)
                final.to_csv(OUTPUT_LOCATION + 'merged-' + df_results_names[i] + '.csv', mode='w', index=False)
                i+=1

        if MERGE_RESULTS == False:
            for df_result1 in df_results:
                df_result1.drop(["temp_tableName"], axis=1, inplace=True)
                df_result1.to_csv(OUTPUT_LOCATION + df_file_info[h]["file"] + '-' + df_results_names[i + j] + '.csv', mode='w', index=False)   
                i+=1
                if i == df_file_info[h]["t_len"]:
                    j = i
                    i = 0
                    h+=1      
    except Error as e:
        print(e)

    finally:
        print("FINISH")