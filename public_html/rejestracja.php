<h1>Rejestracja</h1>
<p>Przesłane dane</p>
<?php
  print_r($_POST);
  print_r($_GET);
?>


    <form name="formularz" id="formularz" method="POST" action=".">
      <table class="table">
        <tr>
          <td>
            <label for="imie">Imię</label>
          </td>
        </tr>
        <tr>
          <td>
            <input type="text" name="imie" value="" placeholder="Imię">
          </td>
        </tr>
        <br>
        <tr>
          <td>
            <label for="nazwisko">Nazwisko</label>
          </td>
        </tr>
        <tr>
          <td>
            <input type="text" name="nazwisko" value="" placeholder="Nazwisko">
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <input type="password" name="haslo" value="">
          </td>
        </tr>
      </table>

          <br>
          <label for="gender">Wybierz płeć:</label>
          <input type="radio" name="gender" value="male" checked> Male<br>
          <input type="radio" name="gender" value="female"> Female<br>
          <input type="radio" name="gender" value="other"> Other
          <input type="radio" name="redneg" value="rehto"> rehtO

          <br>
            <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
            <input type="checkbox" name="vehicle2" value="Car"> I have a car

          <br>
          <select name="cars">
            <option value="1">Autobus</option>
            <option value="2">Saab</option>
            <option value="3">Fiat</option>
            <option value="4">Audi</option>
          </select>

          <textarea name="komentarz" rows="4" cols="80"></textarea>

          <br>
      <input type="submit" name="zapisz" value="Zapisz">
      <input type="reset" name="reset" value="Reset">

    </form>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
  </body>
</html>
