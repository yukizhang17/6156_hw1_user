<!DOCTYPE html>
<html>

<head>
  <title>Our Company</title>
</head>

<body>

  You can add your address right here
<form action="/users/{{userID}}/address" method="post" name="address">
 <ul>
  You id is {{userID}}
  <li>
    <label for="street_name1">street_name1:</label>
    <input type="text" id="street_name1" name="street_name1">
  </li>
  <li>
    <label for="first_name">First Name:</label>
    <input type="text" id="first_name" name="fisrt_name">
  </li>
  <li>
    <label for="contact_number">Phone Number:</label>
    <input type="text" id="phone_number" name="phone_number">
  </li>
      <li>
    <label for="email">Email:</label>
    <input type="text" id="email" name="email">
  </li>
  <li class="button">
  <button type="submit">update</button>
</li>
 </ul>

</form>

IF YOU WANT TO DELETE YOUR ACCOUNT, PRESS HERE!
<form action="/users/{{userID}}" method="post" name="delete">
   <input type="hidden" id="custId" name="custId" value="3487">
   <button method="post">DELETE</button>
</form>

</body>
</html>