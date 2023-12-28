import psycopg2

username = 'postgres'
password = 'postgres'
database = 'db_lab3_lukianenko'
host = 'localhost'
port = '5432'

query_1 = '''
select hours_per_day, depression 
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
order by hours_per_day;
'''
query_2 = '''
select fav_genre, ocd
from person
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.ocd < 5;
'''

query_3 = '''
select fav_genre, bpm
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.averagescore > 5 and music.effects = 'Improve'
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

def output(cur):
        for row in cur:
            print(row)
        print('\n')

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    print('Вивести кількість годин прослуховування на день та рівень депресії')
    cur.execute(query_1)
    output(cur)

    print('\nВивести улюблені жанри тих, у кого рівень тривоги менше 5')
    cur.execute(query_2)
    output(cur)

    print('\nВивести жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан')
    cur.execute(query_3)
    output(cur)