<?php
 $name=$_POST['name'];
 $tel=$_POST['phone'];
 #$rs =  mail('avtolet969@gmail.com', 'NCognoLab', 'Имя: '.$name.'Телефон : '.$tel, 'From: fewfinfo@ncognolab.ru');
 $txt='ХУЙ';
 $txt = str_replace("\n.", "\n..", $txt);
 $rs= mail('avtolet969@gmail.com', 'My Subject', $txt);
 if ($rs) {
  $result="Успешно!Мы перезвоним в  ближайшее время!";
 }
 else{
  $result = 'avtolet969@gmail.com'.'NCognoLab'.'Имя: '.$name.'Телефон : '.$tel.'From: info@ncognolab.com';
 }
    echo json_encode(array(
        'result' => $result
    ));

?>