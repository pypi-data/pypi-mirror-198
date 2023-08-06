import sqlite3
import pkg_resources

class CasteHelper:
    
    def __init__(self):
        self.__database_name = pkg_resources.resource_filename(__name__, 'data/caste.db')
        self.__conn = sqlite3.connect(self.__database_name)
        self.__table_name = "castes"
    
    def _get_all_castes(self):
        query = f"SELECT * FROM {self.__table_name}"
        cursor = self.__conn.execute(query)
        return [row[1] for row in cursor.fetchall()]
    
    def _is_present(self,surname):
        if not isinstance(surname, str):
            raise TypeError("Input parameter must be a string")
        query = f"SELECT * FROM {self.__table_name} WHERE surnames = ?"
        cursor = self.__conn.execute(query, (surname.strip(),))
        return len(cursor.fetchall()) > 0
        
    def _get_random_caste(self,n=1):
        if not isinstance(n, int):
            raise TypeError("Input parameter must be a Integer.")
        query = f"SELECT * FROM {self.__table_name} ORDER BY RANDOM() LIMIT {n}"
        cursor = self.__conn.execute(query)
        return [row[1] for row in cursor.fetchall()]

    def __del__(self):
        self.__conn.close()
    

       