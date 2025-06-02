def Submitchatroom(username, message, Configfile, ChatroomName):
    print("Submitting chatroom message...")
    import xml.etree.ElementTree as ET
    from hostsetup.hostsetup import login
    tree = ET.parse(Configfile)
    configfile_root = tree.getroot()
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




