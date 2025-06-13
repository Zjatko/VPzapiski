<?php
	include 'config.php';
	session_start();

	if(!isset($_SESSION['username'])) {
		header('Location: index.php');
	}

	if(isset($_POST['ip'])) {
		$data = shell_exec('curl ' . $_POST['ip']);
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<title>VarProg Admin</title>
	</head>
	<body>
		<h1>Welcome <?php echo $_SESSION['username']; ?></h1>
		<form method="post">
			<input type="text" name="ip" placeholder="IP Address" required>
			<input type="submit" value="Ping">
		</form>
		<?php if(isset($data)) {
			echo '<pre>' . $data . '</pre>';
		} ?>
	</body>
</html>
