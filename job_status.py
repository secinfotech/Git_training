import cx_Oracle 
import config

try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\CHAKRARM\OneDrive - Novartis Pharma AG\ODY_DEV_test\instantclient_21_9")
    conn = cx_Oracle.connect(user=config.username, password=config.password,
                               dsn=config.dsn,
                               encoding=config.encoding)
    # schema = config.schema_name
    # table = config.table
 
except cx_Oracle.Error as error:
    print(error)
else:
    try:
        cursor = conn.cursor()
        cursor.execute('''select * from (select * from SDZ_CAS_BATCH.SDZ_PROCESS_LOG
        where interface like '%PRODUCT%' and start_time = (select max(start_time) from SDZ_CAS_BATCH.SDZ_PROCESS_LOG
        where interface like '%PRODUCT%')) a where a.record_id=(select max(record_id) from (select * from SDZ_CAS_BATCH.SDZ_PROCESS_LOG
        where interface like '%PRODUCT%' and start_time = (select max(start_time) from SDZ_CAS_BATCH.SDZ_PROCESS_LOG
        where interface like '%PRODUCT%')))''')
        response = cursor.fetchall()
        for row in response:
            print(row)
        job_id = response[0][1]
        print(job_id)
        
    except cx_Oracle.Error as error:
        print(error)
    finally:
        cursor.close()
finally:
    conn.close()

        
