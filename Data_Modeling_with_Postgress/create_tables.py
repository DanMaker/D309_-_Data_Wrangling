import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''
    Description: Initalize the Database
        - drop the database if it already exists
        - create the database with the provided template
        - create the tables
        - create the connection string
        - create the command cursor
    
    Arguments:
        none

    Returns:
        conn: the database connection string
        cur: the command cursor
    '''

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    '''
    Description: drop the tables
        - drop the tables in the 'drop_table_queries' list
    
    Arguments:
        conn: the database connection string
        cur: the command cursor
        
    Returns:
        conn: the database connection string
        cur: the command cursor
    '''

    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
            # print("Completed:", query)
        except Exception as e:
            print("Error: failed to complete:", query)
            print(e)
            return cur, conn


def create_tables(cur, conn):
    '''
    Description: create the tables
        - create the tables in the 'create_table_queries' list
    
    Arguments:
        conn: the database connection string
        cur: the command cursor
        
    Returns:
        conn: the database connection string
        cur: the command cursor
    '''

    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
            # print("Completed:", query)
        except Exception as e:
            print("Error: failed to complete:", query)
            print(e)
            return cur, conn

def main():
    '''
    Description: manage all the functions in this file
        - create the cur and conn variables and call 'create_database' with them
        - call drop_tables
        - call create_tables
        - close the database connection
    
    Arguments:
        none
        
    Returns:
        none
    '''


    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()