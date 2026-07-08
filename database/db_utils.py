import sqlite3


class DatabaseUtils:

    @staticmethod
    def get_product_price(product_name):

        conn = sqlite3.connect("database/test.db")

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT price
            FROM products
            WHERE product_name = ?
            """,
            (product_name,)
        )

        result = cursor.fetchone()

        conn.close()

        return result[0]