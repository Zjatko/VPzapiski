<?php
	include 'config.php';
	session_start();

	if(isset($_POST['username']) && isset($_POST['password'])) {

		$sql = "SELECT * FROM users WHERE username = '" . $_POST['username'] . "' AND password = '" . $_POST['password'] . "'";
		$result = $conn->query($sql);
		if($result->num_rows > 0) {
			$row = $result->fetch_assoc();
			$_SESSION['username'] = $row['username'];
			header('Location: admin.php');
		}
		else {
			$error = 'Invalid username or password';
		}
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<title>VarProg Login</title>
	</head>
	<body>
		<form method="post">
			<input type="text" name="username" placeholder="Username" required>
			<input type="password" name="password" placeholder="Password" required>
			<input type="submit" value="Login">
		</form>
		<?php if(isset($error)) {
			echo '<p>' . $error . '</p>';
		} ?>
	</body>
</html>
