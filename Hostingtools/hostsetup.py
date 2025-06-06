#this was the first thign i ever coded for this project: a simple way to connect to the database,

import psycopg2
#imports Psycop2 
import xml.etree.ElementTree as ET
#imports  the abilty to check a config file.
def login(configfile):
    #the function to login: this is used alot in the codebase.
    try:
        #tries to connect,
        dbname = configfile.find('dbname').text
        #it gets the dbname from the config file
        print(dbname)
        user = configfile.find('user').text
        #it finds the user  from the config file
        print(user)
        password = configfile.find('password').text
        #finds password
        print(password)
        host = configfile.find('host').text
        #finds host
        print(host)
        port = configfile.find('port').text
        #finds the port.
    except AttributeError as e:
        #if this isnt workinh, it pritns the error.
        raise ValueError(e) from e

    try:
        #it trys to connect using the data it collected durring the begining,
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        return conn
        #it sets the connection used to interact with the database, it is used when login
    except psycopg2.Error as e:
        raise ConnectionError(f"Failed to connect to the database: {e}") from e
        #except if theres  a error, then it prints out a error/
def createchat(configfile_path, table_messages_name):
    from psycopg2 import sql
    #improt sql fucntions
    conn = None
    #defaultvalue for conn
    try:
        #it parses the configfile, opening it up.
        tree = ET.parse(configfile_path)
        # it gets the root file 
        configfile = tree.getroot()
        #config file is the docum
        conn = login(configfile)
        #the connection is returned from login, using configfile as the attrubite with the same name in login.
        cur = conn.cursor()
        #creates the cursor
        create_table_sql = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} ( 
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL,
            username VARCHAR(100) NOT NULL
        );
        """).format(table=sql.Identifier(table_messages_name))
        cur.execute(create_table_sql)
        conn.commit()
        cur.close()
        conn.close()
        print("done")
        #this code first creates a table and inserts id, message, and username. afterwards, it proceeds to
        #execute this sql code before doing the finishing steps of closing the cursor and connection.
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Error parsing XML config file: {e}")
    # prints out a error if there is one
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            try:
                conn.close()
            except Exception:
                pass
           #tries to close connection
print("done")

createchat(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml", "messageslist")import psycopg2
