<?php
require 'vendor/autoload.php';
 $name=$_POST['name'];
 $tel=$_POST['phone'];
 $to = "zaizevt00@yandex.ru"; // Update with email.
 $subject = "NCogno";
 
 // Create new fields here for each field in your form.
 // Ideally you would want some validation here too.

 $headers = "From: ncogno_forms@ncognolab.com\n";

 $message = "Name : $name\nPhone: $tel";

 $result= "Form Sent";
 mail($to, $subject, $message, $headers);
} else {
 $result= "Form failed to send. Please contact us directly.";
}
    echo json_encode(array(
        'result' => $result
    ));

?>