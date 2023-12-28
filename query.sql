-- Запит 1. Вивести кількість годин прослуховування на день та рівень депресії
select hours_per_day, depression 
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
order by hours_per_day;

-- Запит 2. Вивести улюблені жанри тих, у кого рівень тривоги менше 5
select fav_genre, ocd
from person
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.ocd < 5;

--Запит 3. Вивести жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан
select fav_genre, bpm
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.averagescore > 5 and music.effects = 'Improve'
