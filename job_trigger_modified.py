import cx_Oracle 
import config

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
            cursor.callproc(proc_name, params)
            params[0] = cursor.var(cx_Oracle.NUMBER)
            params[1] = cursor.var(cx_Oracle.STRING)
            params[2] = cursor.var(cx_Oracle.STRING)
            params[3] = cursor.var(cx_Oracle.STRING)
            # new_var = cursor.getimplicitresults()
            # print(new_var)
            for i in range(len(params)):
                print(params[i].getvalue())
            
          
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