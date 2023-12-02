-- Запит 1. Вивести кількість годин прослуховування на день та рівень депресії
select hours_per_day, depression 
from person 
join mental_illness on person.averagescore = mental_illness.averagescore
order by hours_per_day;

-- Запит 2. Вивести улюблені жанри тих, у кого рівень тривоги менше 5
select fav_genre, ocd
from person
join mental_illness on person.averageScore = mental_illness.averageScore
join music on person.music_id = music.music_id
where mental_illness.ocd < 5;

--Запит 3. Вивести жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан
select fav_genre, bpm
from person 
join mental_illness on person.averagescore = mental_illness.averagescore
join music on person.music_id = music.music_id
where person.averagescore > 5 and music.effects = 'Improve'
