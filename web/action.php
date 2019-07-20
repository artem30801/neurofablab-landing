<?php
 $name=$_POST['name'];
 $tel=$_POST['phone'];
 $rs =  mail('avtolet969@gmail.ru', 'NCognoLab', 'Имя: '.$name.'Телефон : '.$tel, 'From: info@ncognolab.com');
 if ($rs) {
  $result="Успешно!Мы перезвоним в ближайшее время!";
 }
 else{
  $result = "Что-то пошло не так :(";
 }
    echo json_encode(array(
        'result' => $result
    ));

?>