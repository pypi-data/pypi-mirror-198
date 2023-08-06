import mysql.connector

class MySQL():
    def __init__(self, host:str, user:str, password:str, database:str) -> None:
        self.myConnection = mysql.connector.connect(host = host, user = user, password = password, database = database)
        self.cursor = self.myConnection.cursor()
        
    def createDataBase(self, nameDB:str) -> None:
        """
        Crea una base de datos nueva
        """
        self.cursor.execute(f"CREATE DATABASE {nameDB};")
        self.myConnection.commit()

    def useDatabase(self, database:str) -> None:
        """
        Accede directamente a una base de datos ya creada
        """
        self.cursor(f"USE {database};")

    def createTable(self, nameTable:str, parametersOfTable:str) -> None:
        """
        Crea una tabla mientras no exista otra con el mismo nombre
        """
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {nameTable}({parametersOfTable});")
        self.myConnection.commit()
    
    def tableIsEmpity(self, database:str, table:str) -> bool:
        """
        Verifica si hay datos guardados en una tabla de una base de datos
        """
        if (self.cursor.execute(f"SELECT COUNT(*) FROM  {database}.{table};") != 0): return False
        return True
    
    def countRecordsWhere(self, database:str, table:str, parametersOfSearch:list, value:list) -> int:
        """
        Cuenta cuantos valores hay de un dato especifico con respecto a uno o varios parametros 
        las dos listas deben tener la misma longitud
        """
        query = f"SELECT COUNT(*) FROM {database}.{table} WHERE "

        if (len(parametersOfSearch) == len(value) and value != []):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{value[k]}\" AND "
                else:
                    query += f"{parametersOfSearch[k]} = \"{value[k]}\";"

            return self.cursor.execute(query)
        
        else: return None
    
    def insertRow(self, table:str, columns:str, values:tuple) -> None:
        """
        Inserta una serie de valores pasados como tuplas en las columnas indicadas de la tabla
        """
        self.cursor.execute(f"INSERT INTO {table}({columns}) VALUES{values};")
        self.myConnection.commit()
    
    def getRowsWhereAND(self, table:str, parametersOfSearch:list, values:list) -> tuple:
        """
        Retorna todas las columnas de una tabla cuando se cumplan las condiciones requerida
        la longitud de las listas de parametros y la de valores debe tener la misma longitud
        el conector logico para cuando sea mas de una condicion sera el AND
        """
        query = f"SELECT * FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} = \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\" AND "
                else:
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getRowsWhereOR(self, table:str, parametersOfSearch:list, values:list) -> tuple:
        """
        Retorna todas las columnas de una tabla cuando se cumplan las condiciones requerida
        la longitud de las listas de parametros y la de valores debe tener la misma longitud
        el conector logico para cuando sea mas de una condicion sera el OR
        """
        query = f"SELECT * FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} = \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\" OR "
                else:
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getRowsLikeOR(self, table:str, parametersOfSearch:str, values:str) -> tuple:
        """
        Al ser usado el LIKE como operador de comparacion la busqueda en la base de datos sera como un filtro \n
        Retorna todas las columnas de una tabla cuando se cumplan las condiciones requerida
        la longitud de las listas de parametros y la de valores debe tener la misma longitud
        el conector logico para cuando sea mas de una condicion sera el OR.
        """
        query = f"SELECT * FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} LIKE \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\" OR "
                else:
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getRowsLikeAND(self, table:str, parametersOfSearch:str, values:str) -> tuple:
        """
        Al ser usado el LIKE como operador de comparacion la busqueda en la base de datos sera como un filtro \n
        Retorna todas las columnas de una tabla cuando se cumplan las condiciones requerida
        la longitud de las listas de parametros y la de valores debe tener la misma longitud
        el conector logico para cuando sea mas de una condicion sera el AND.
        """
        query = f"SELECT * FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} LIKE \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\" AND "
                else:
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getColumn(self, table:str, column:str) -> tuple:
        """
        Retorna una tupla con las columnas de la tabla seleccionadas
        """
        self.cursor.execute(f"SELECT {column} FROM {table}")
        return self.cursor.fetchall()

    
    def getColumnsWhereAND(self, table:str, columns:list, parametersOfSearch:list, values:list) -> tuple:
        """
            El orden de los valores de las listas de parametros y valores deben corresponder en el orden
            Se debe tomar en cuenta que el uso de conectores en caso de ser mas de un solo parametro de busqueda
            Y valores sera un conector logico AND
        """
        query = "SELECT "
        for k in range(len(columns)):
            if (k != len(columns) - 1):
                query += columns[k] + ", "
            else:
                query += columns[k] + " "
        
        query += f"FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} = \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\" AND "
                else:
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getColumnsWhereOR(self, table:str, columns:list, parametersOfSearch:list, values:list) -> tuple:
        """
            El orden de los valores de las listas de parametros y valores deben corresponder las posiciones
            se debe tomar en cuenta que el uso de conectores en caso de ser mas de un solo parametro de busqueda
            y valores sera un conector logico OR
        """
        query = "SELECT "
        for k in range(len(columns)):
            if (k != len(columns) - 1):
                query += columns[k] + ", "
            else:
                query += columns[k] + " "
        
        query += f"FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} = \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\" OR "
                else:
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getColumnsLikeAND(self, table:str, columns:list, parametersOfSearch:list, values:list) -> tuple:
        """
            El operador de comparacion es un LIKE por lo que sera una busqueda parcial \n
            El orden de los valores de las listas de parametros y valores deben corresponder las posiciones
            se debe tomar en cuenta que el uso de conectores en caso de ser mas de un solo parametro de busqueda
            y valores sera un conector logico AND
        """
        query = "SELECT "
        for k in range(len(columns)):
            if (k != len(columns) - 1):
                query += columns[k] + ", "
            else:
                query += columns[k] + " "
        
        query += f"FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} LIKE \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\" AND "
                else:
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\";"
        else:
            return None
    
    def getColumnsLikeOR(self, table:str, columns:list, parametersOfSearch:list, values:list) -> tuple:
        """
            El operador de comparacion es un LIKE por lo que sera una busqueda parcial \n
            El orden de los valores de las listas de parametros y valores deben corresponder las posiciones
            se debe tomar en cuenta que el uso de conectores en caso de ser mas de un solo parametro de busqueda
            y valores sera un conector logico OR
        """
        query = "SELECT "
        for k in range(len(columns)):
            if (k != len(columns) - 1):
                query += columns[k] + ", "
            else:
                query += columns[k] + " "
        
        query += f"FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} LIKE \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\" OR "
                else:
                    query += f"{parametersOfSearch[k]} LIKE \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getTable(self, dataBase:str, table:str) -> tuple:
        """
            Retorna toda una tabla de la base de datos
        """
        self.cursor.execute(f"SELECT * FROM {dataBase}.{table};")
        return self.cursor.fetchall()
    
    def deleteRowWhereAND(self, table:str, parametersOfSearch:list, values:list) -> None:
        """
            Elimina filas de una tabla, la longitud de los parametros de busqueda y de los valores
            de busqueda deben ser iguales, en caso de ser mas de un parametro de busqueda y valor
            se usara el conector logico AND para las condiciones
        """
        query += f"DELETE FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} = \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\" AND "
                else:
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        self.myConnection.commit()

    def deleteRowWhereOR(self, table:str, parametersOfSearch:list, values:list) -> None:
        """
            Elimina filas de una tabla, la longitud de los parametros de busqueda y de los valores
            de busqueda deben ser iguales, en caso de ser mas de un parametro de busqueda y valor
            se usara el conector logico OR para las condiciones
        """
        query += f"DELETE FROM {table} WHERE "

        if ( 1 in [len(parametersOfSearch), len(values)]):
            query += f"{parametersOfSearch[0]} = \"{values[0]}\";"

        elif  ([len(parametersOfSearch), len(values)] > [1,1]):
            for k in range(len(parametersOfSearch)):
                if (k != len(parametersOfSearch) - 1):
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\" OR "
                else:
                    query += f"{parametersOfSearch[k]} = \"{values[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        self.myConnection.commit()
    
    def showTables(self, nameDB:str) -> tuple:
        self.cursor.execute(f"SHOW TABLES FROM {nameDB};")
        return self.cursor.fetchall()
    
    def showDataBases(self):
        self.cursor.execute("SHOW DATABASES;")
        return self.cursor.fetchall()
    
    def showSomeDataBases(self, parameter:str):
        self.cursor.execute(f"SHOW DATABASES LIKE \"{parameter}%\";")
        return self.cursor.fetchall()
    
    def deleteTable(self, nameDB:str, nameTable:str) -> None:
        self.cursor.execute(f"DROP TABLE {nameDB}.{nameTable};")
        self.myConnection.commit()
    
    def deleteDataBase(self, nameDB:str) -> None:
        self.cursor.execute(f"DROP DATABASE {nameDB};")
        self.myConnection.commit()
    
    def updateWhereAND(self, table:str, columns:list, newValue:list, columnSearch:list, valueSearch:list) -> None:
        query = f"UPDATE {table} SET "

        for k in range(len(columns)):
            if (k != len(columns) - 1):
                query += columns[k] + "=" + f"\"{newValue[k]}\"" + ", "
            else:
                query += columns[k] + "=" + f"\"{newValue[k]}\" "
        
        query += f"WHERE "

        if ( 1 in [len(columnSearch), len(valueSearch)]):
            query += f"{columnSearch[0]} = \"{valueSearch[0]}\";"

        elif  ([len(columnSearch), len(valueSearch)] > [1,1]):
            for k in range(len(columnSearch)):
                if (k != len(columnSearch) - 1):
                    query += f"{columnSearch[k]} = \"{valueSearch[k]}\" AND "
                else:
                    query += f"{columnSearch[k]} = \"{valueSearch[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        self.myConnection.commit()
    
    def updateWhereOR(self, table:str, columns:list, newValue:list, columnSearch:list, valueSearch:list) -> None:
        query = f"UPDATE {table} SET "

        for k in range(len(columns)):
            if (k != len(columns) - 1):
                query += columns[k] + "=" + f"\"{newValue[k]}\"" + ", "
            else:
                query += columns[k] + "=" + f"\"{newValue[k]}\" "
        
        query += f"WHERE "

        if ( 1 in [len(columnSearch), len(valueSearch)]):
            query += f"{columnSearch[0]} = \"{valueSearch[0]}\";"

        elif  ([len(columnSearch), len(valueSearch)] > [1,1]):
            for k in range(len(columnSearch)):
                if (k != len(columnSearch) - 1):
                    query += f"{columnSearch[k]} = \"{valueSearch[k]}\" OR "
                else:
                    query += f"{columnSearch[k]} = \"{valueSearch[k]}\";"
        else:
            return None
        
        self.cursor.execute(query)
        self.myConnection.commit()
    
    def commit(self) -> None:
        self.myConnection.commit()