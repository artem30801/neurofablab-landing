<?php
 $name=$_POST['name'];
 $tel=$_POST['phone'];
 #$rs =  mail('avtolet969@gmail.com', 'NCognoLab', 'Имя: '.$name.'Телефон : '.$tel, 'From: fewfinfo@ncognolab.ru');
 $txt='XUI';
 $txt = str_replace("\n.", "\n..", $txt);
 $rs= mail('avtolet969@gmail.com', 'My Subject', $txt);
 if ($rs) {
  $result="Успешно!Мы перезвоним в  ближайшее время!";
 }
 else{
  $result = 'no';
 }
    echo json_encode(array(
        'result' => $result
    ));

?>