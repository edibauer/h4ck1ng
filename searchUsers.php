<?php

$server = "localhost";
$username = "edibauer";
$password = "edibauer123";
$database = "h4ckforyou";

$conn = new mysqli($server, $username, $password, $database); // connection

$id = $_GET['id'];
echo $id;






?>