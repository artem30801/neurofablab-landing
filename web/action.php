<?php
 $name=$_POST['name'];
 $tel=$_POST['phone'];
 $rs =  mail('avtolet969@gmail.com', 'NCognoLab', 'Имя: '.$name.'Телефон : '.$tel, 'From: info@ncognolab.com');
 if ($rs) {
  $result="Успешно!Мы перезвоним в ближайшее время!";
 }
 else{
  $result = $rs;
 }
    echo json_encode(array(
        'result' => $result
    ));

?>