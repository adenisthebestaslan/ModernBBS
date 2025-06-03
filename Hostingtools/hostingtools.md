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

### login(configfile)
 first, it attempts to try to find each peice of data from the config file [look at this here.](#Setting up a Configfile)

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
      first, it gets the config file before using login [look at this here.](### login(configfile))
      it makes a table with id, username, and message, with the name you specified in table_messages_name
              
              create_table_sql = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL,
            username VARCHAR(100) NOT NULL
        );


