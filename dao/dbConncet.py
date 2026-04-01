import pathlib


import mysql.connector

class DBConnect:

    _mypool = None

    def __init__(self):
        #per implementare il pattern singletone ed impedire al chiamante di creare istanza di classe.
        raise RuntimeError("Attenzione! Non devi creare un'istanza di questa classe. Usa i metodi di classe.")
    @classmethod
    def getConnection(cls):
        if cls._mypool is None:
            try:
                #cnx = mysql.connector.connect(
               #     user = "root",
                 #   password = "Golden2026!",
                  #  host = "127.0.0.1",
                   # database = "sw_gestionale")
                cls._mypool = mysql.connector.pooling.MySQLConnectionPool(
                    #user = "root",
                    #password = "",
                    #host = "127.0.0.1",
                    #database = "sw_gestionale",
                    pool_size = 3,
                    pool_name = "mypool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                return cls._mypool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None

        else:
            #allora il pool già esiste e quindi restituisco direttamente la connessione
            return cls._mypool.get_connection()
