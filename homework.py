import psycopg2

 
db_name = 'n47'
password = '258182126'
host = 'localhost'
port = 5432
user = 'postgres'


with psycopg2.connect(dbname=db_name,
                      user=user,
                      password=password,
                      host=host,
                      port=port) as conn:
    with conn.cursor() as cur:
        def create_table():
            product_id = 1
            create_table_query = """create table if not exists Products(
                id serial PRIMARY KEY,
                name varchar(70) not null,
                image varchar(255),
                is_liked boolean,
                created_at timestamp default current_timestamp,
                updated_at timestamp default current_timestamp
            );
            """
            cur.execute(create_table_query)
            conn.commit()
            print('Table Successfully Created')

        if __name__ == "__main__":
            create_table()


        def insert_product_data(name, image, is_liked):
            insert_query = """insert into Products (name, image, is_liked)
                                      values (%s, %s, %s)"""
            cur.execute(insert_query, (name, image, is_liked))
            conn.commit()

        product_id = insert_product_data("Product 1", "image1.jpg", True)

        def select_data():
            select_query = "SELECT * FROM Products"
            cur.execute(select_query)
            products = cur.fetchall()
            for product in products:
                print(product)


        select_data()

        def update_data(product_id, name, image, is_liked):
            update_query = """update Products
                                      set name = %s, image = %s, is_liked = %s, updated_at = CURRENT_TIMESTAMP
                                      where id = %s"""
            cur.execute(update_query, (name, image, is_liked, product_id))
            conn.commit()


        update_data(product_id, "Updated Product 1", "updated_image.jpg", False)


        def delete_data(product_id):
            delete_query = "delete from Products where id = %s"
            cur.execute(delete_query, (product_id,))
            conn.commit()

        delete_data(product_id)

