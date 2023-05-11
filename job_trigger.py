import cx_Oracle 
import config
# import job_status


def job_trigger():
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
            proc_name = 'SDZ_CAS_BATCH.SDZ_INTF_MEDICAID_PKG.SDZ_INTF_OUT_PRODUCT_PROCESS_SP'
            params = ['PN_RET_CD_OUT', 'PS_ERROR_CD_OUT', 'PS_ERROR_MSG_OUT', 'PS_PROC_STEP_OUT']
            # cursor.execute('SELECT * from SDZ_CAS_BATCH.CONT OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY')
            # response = cursor.fetchall()
            # for row in response:
            #     print(row)
            cursor.callproc(proc_name, params)
            res = cursor.var(bool)
            print(res)
        except Exception as err:
            print(err)
        else:
            print('Procedure executed')
        finally:
            cursor.close()
    finally:
        conn.close()

job_trigger()

# print(job_status.response)