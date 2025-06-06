# Setting up a Configfile
first, create a file called "Configfile.xml."
set it up like this:

## Examples
<config>
   <dbname></dbname>
   <user></user>
   <password</password>
   <host></host>
   <port></port>
   <tablename></tablename>
</config>

here's what each one does:

## table

| Tag's         | use
| ------------- | ------------- |
| dbname |  Name of your database: used to connect to a message server.  |
| user  | name of the user: used to authenticate |
|password| used to connect: is authentiction|
|host| ip adress of server|
|port| where our database is listing for connections.|


# making a table

Open Hostingsetup.py,
before running this in the python file:
createchat(configfile_path, table_messages_name):

heres what each thing does

## table for argument use


| arguments| use
| ------------- | ------------- |
| configfile_path |  the file path to the config file.|
| table_messages_name  | used to access the table graphics. |

now that you know how to use it, lets see how it works.


## How Hostingsetup.PY WORKS:

###login(configfile)
 first, it attempts to try to find each peice of data from the config file [look at this here.](#Setting-up-a-Configfile)

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

then it connects.

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

   ### Createchat():
   first, it gets the config file before using login [look at this here.](###login(configfile))
   it makes a table with id, username, and message, with the name you specified in table_messages_name
              
              create_table_sql = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL,
            username VARCHAR(100) NOT NULL
        );


# grabbing the messages 

ChatinfoBBS(configfile,BulietenName):
this function is used in the Assembler



## table

| Tag's         | use
| ------------- | ------------- |
| Configfile |  uses this to access your credentials|
| BulietenName  |used to access the table|

## how it works
parse the tree and   [login.](###login(configfile))


    def ChatinfoBBS(configfile,BulietenName):
       # Function to fetch recent items from a specified page in the database
       tree = ET.parse(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
       # Parse the XML configuration file
       configfile = tree.getroot()
       #get the root of the xml file and use that to login
       conn = login(configfile)

after wards, get the number of rows.

    cur.execute(f"SELECT COUNT(*) FROM {BulietenName};")
    #select amount from page 
    row_count = cur.fetchone()[0]
    # get row number
afterwards, if you have lesss than 10 messages, it shows all the messages by ascending order.

if it is more than 10, it shows the last 10.
else, it shows the last 10.

    if row_count < 10:
         print(f"Table '{BulietenName}' contains less than 10 rows: {row_count}")

        cur.execute(f"""
        SELECT * FROM {BulietenName}
        ORDER BY username ASC
        LIMIT {row_count}
        """)
        #order by username and ascending order, limit by row count
        print(f"Table '{BulietenName}' contains less than 10 rows: {row_count}")
    elif row_count >= 10:
        print(f"Table '{BulietenName}' contains 10 or more rows: {row_count}")
        cur.execute(f"""
        SELECT * FROM {BulietenName}
        ORDER BY username ASC
        LIMIT 10;
        """)
        #order by username and ascending order, limit by 10
    #order by username and limit to 10    
    else:
        print(f"Table '{BulietenName}' contains no rows.")
        return []


it makes a list of items to be shown in the gui:

    recent_items = cur.fetchall()
    print(f"Recent items: {recent_items}")
    #print recent items
    messages = []
    # Print results
    numbermessages = 0
    print(f"Number of messages:{numbermessages}")
    for item in recent_items:
        print(item)
        print(numbermessages)
        messages.append(item)
        #append item to messages
        numbermessages += 1
    print(messages)
    

    cur.close()
    conn.close()

    return messages


# Submitmessage.py
## Submitchatroom()
Submitchatroom(username, message, Configfile, ChatroomName)

### arguments and uses


| Tag's         | use
| ------------- | ------------- |
| username |  the username of the person submitting the message.|
| message  |what the user has entered|
|configfile| grabs the config file|
|ChatroomName| the name of the chatroom|

### how it works.

first, it parses the config file and then logs in 

    print("Submitting chatroom message...")
    import xml.etree.ElementTree as ET
    from hostsetup.hostsetup import login
    tree = ET.parse(Configfile)
    configfile_root = tree.getroot()
    conn = login(configfile_root)

afterwards, it inserts the data

    conn = login(configfile_root)
    try:
        with conn.cursor() as cur:
            # Use SQL identifier placeholder for table name if supported, else validate ChatroomName
            insert = f"INSERT INTO \"{ChatroomName}\" (message, username) VALUES (%s, %s);"
            values = (message, username)
            cur.execute(insert, values)
        conn.commit()
    finally:
        conn.close()
