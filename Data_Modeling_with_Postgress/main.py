from create_tables import main as create_tables_main
from etl import main as etl_main

def main():
    '''
    Description: Provides a simplified method for creating
    the database, and tables, and doing the ETL.
        - create the database and tables
        - process the data files into the database tables
    
    Arguments:
        none
    Returns:
        none
    '''
    create_tables_main()
    etl_main()


if __name__ == "__main__":
    main()