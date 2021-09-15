<?php

    $server = "sql302.epizy.com";
    $username = "epiz_29733557";
    $password = "3id3w6BlLJg8sv":
    $dbname = "epiz_29733557_starkclient";

    $conn = mysqli_connect($server, $username, $password, $dbname);

    if(!$conn){
        die("connection Failed:".mysqli_connect_error())
    }