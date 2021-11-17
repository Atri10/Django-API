# Django Simple API
<h4>This is a simple Django API which accepts details of user and retrives all the details back on GET request.
An <b>asynchronous</b> email containing user details will be sent to user.</h4>

# How to use

<h4>1. Open Postman or use https://reqbin.com/</h4>
<h4>2. Set target url to https://django-api-show.herokuapp.com/userdata</h4>
<h4>3. Put Following data in JSON formate and send <b>POST</b> request</h4>

```
{
  "name":"Test User",
  "birth":"2001-11-29",
  "email":"RandomEmail@gmail.com",
  "phone":"+91 9999999999"
}
```
<h4>4. To retrive data send <b>GET</b> request to same URL</h4>
