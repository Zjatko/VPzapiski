<?php
	$dbhost = 'mysql';
	$dbuser = 'varprog';
	$dbpass = 'varprog';
	$dbname = 'varprog';

	$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
	if($conn->connect_error) {
		die('Connection failed: ' . $conn->connect_error);
	}

	$sql = "SELECT 1 FROM information_schema.tables WHERE table_schema = 'varprog' AND table_name = 'users'";
	$result = $conn->query($sql);
	if($result->num_rows == 0) {
		$sql = "CREATE TABLE users (
			id INT AUTO_INCREMENT PRIMARY KEY,
			username VARCHAR(50) NOT NULL,
			password VARCHAR(255) NOT NULL
		)";
		if($conn->query($sql) === FALSE) {
			echo "Error creating table: " . $conn->error;
		}

		$characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < 32; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
		}

		$sql = "INSERT INTO users (username, password) VALUES ('admin', '" . $randomString . "')";
		if($conn->query($sql) === FALSE) {
			echo "Error creating user: " . $conn->error;
		}
	}
?>
