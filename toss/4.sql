/*
  아래 SQL문을 통해 데이터를 조회할 수 있습니다.
  
  SELECT * FROM `user`;
  SELECT * FROM `character`;
*/

-- SELECT user.id , CONCAT(character.title,character.job," ",character.name) from `user` and `character`  ;


SELECT

u.id
,
CONCAT(IFNULL(c.title,""),c.job," ",u.name)

FROM

`user` AS u

RIGHT JOIN

`character` AS c

ON

u.id = c.user_id

ORDER BY u.id DESC

;