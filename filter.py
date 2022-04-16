import psycopg2


def get_by_region(region, cursor):
    query = f"{region}"
    cursor.execute(query)


def get_by_pos(position, cursor):
    query = f"{position}"
    cursor.execute(query)


def get_by_voter_filter(filter, cursor):
    query = f"{filter}"
    cursor.execute(query)


if __name__ == "__main__":
    connection = psycopg2.connect(
        database="postgres", user='testuser', password='password')
    cursor = connection.cursor()
