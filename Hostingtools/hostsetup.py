import psycopg2
import xml.etree.ElementTree as ET

def login(configfile):
    try:
        dbname = configfile.find('dbname').text
        print(dbname)
        user = configfile.find('user').text
        print(user)
        password = configfile.find('password').text
        print(password)
        host = configfile.find('host').text
        print(host)
        port = configfile.find('port').text
    except AttributeError as e:
        raise ValueError(e) from e

    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        return conn
    except psycopg2.Error as e:
        raise ConnectionError(f"Failed to connect to the database: {e}") from e

def createchat(configfile_path, table_messages_name):
    from psycopg2 import sql
    conn = None
    try:
        tree = ET.parse(configfile_path)
        configfile = tree.getroot()
        conn = login(configfile)
        cur = conn.cursor()
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
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Error parsing XML config file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            try:
                conn.close()
            except Exception:
                pass

print("done")

createchat(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml", "messageslist")import psycopg2
