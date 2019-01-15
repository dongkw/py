import psycopg2

if __name__ == '__main__':
  connection = psycopg2.connect(database="dev", user="postgres", password="dev",
                                host="172.16.10.105", port="5432")
  cursor = connection.cursor()
  for index in range(0, 500):
    sql = """update s_liu.t_test set count = count + 1 where id = 1;"""
    cursor.execute(sql)
  connection.commit();
  cursor.close()