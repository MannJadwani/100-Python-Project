import psycopg2
connect = psycopg2.connect(dbname = 'postgres',user = 'postgres',password = '973015',host = 'localhost',port='5432')
print('Connected')
# page 144