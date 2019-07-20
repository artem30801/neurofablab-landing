<?php
 $name=$_POST['name'];
 $tel=$_POST['phone'];
 #$rs =  mail('avtolet969@gmail.com', 'NCognoLab', 'Имя: '.$name.'Телефон : '.$tel, 'From: fewfinfo@ncognolab.ru');
 $rs= mail('zaizevt00@yandex.ru', 'My Subject', 'ХУЙ');
 if ($rs) {
  $result="Успешно!Мы перезвоним в ближайшее время!";
 }
 else{
  $result = '...';
 }
    echo json_encode(array(
        'result' => $result
    ));

?>