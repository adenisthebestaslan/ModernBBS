import xml.etree.ElementTree as ET
from hostsetup.hostsetup import login
#import items
def ChatinfoBBS(configfile,BulietenName):
    # Function to fetch recent items from a specified page in the database
    tree = ET.parse(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
    # Parse the XML configuration file
    configfile = tree.getroot()
    #get the root of the xml file and use that to login
    conn = login(configfile)

    
    print(conn)
    #print our database fata
    cur = conn.cursor()
    #connect 
    
    cur.execute(f"SELECT COUNT(*) FROM {BulietenName};")
    #select amount from page 
    row_count = cur.fetchone()[0]
    # get row number
    if row_count < 10:
        # if row number is less than ten
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
    
# Fetch results
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

    #grab the 10 messages from the database
    #grab the chatroom info from postgres.
# dbname,user,password,host,port,TableMessagesName

# Close the cursor and connection
