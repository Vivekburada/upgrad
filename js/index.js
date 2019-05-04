/*
@BuradaVivek
@vivekburada97@gmail.com
@This project is built for UpGrad
Date 4th May
*/


var link="http://0.0.0.0:5000";

function checkmail(email)
{
  if(1)
  {
    return 1;
  }
  else
  {
return 0;
  }

}
function login() {
flag=1
  var username=document.getElementById('log_username').value;
  var password=document.getElementById('log_pwd').value;
  flag=checkmail(username)
  if(!flag)
  {
    var success=document.getElementById('success-login');
    success.innerHTML='Enter Correct Email ID'
    success.style.display="block";
    return;
  }
  var url=link+"/api/v1/users/login";
  var xhttp=new XMLHttpRequest();
  xhttp.onreadystatechange=function() {
    if (this.readyState==4){
      console.log(this.status);
      if (this.status==200)
      {
       setCookie("user", username, 30);
       console.log(getCookie("user"),"--COOKIE  --");
        var success=document.getElementById('success-login');
        success.innerHTML='Login Successful : <a href="landing.html">Click here to launch Main page</a>'
        success.style.display="block";
      }else{
      var success=document.getElementById('success-login');
      success.innerHTML="Login failure";
      success.style.display="block";
    }

    }

  };
  xhttp.open("POST",url,true);
  xhttp.setRequestHeader("Content-Type","application/json");
  var data=JSON.stringify({"name":username,"pass":password});
  console.log(data);
  xhttp.send(data);
}

  function register()
  {
    var username=document.getElementById('reg_username').value;
    var password=document.getElementById('reg_pwd').value;
    var url=link+"/api/v1/users/register";
    var xhttp=new XMLHttpRequest();

    xhttp.onreadystatechange=function() {
      if (this.readyState==4){
        console.log(this.status);
        if (this.status==201)
        {
          var success=document.getElementById('success');
          success.innerHTML="User successfully created please login to continue!";

          success.style.display="block";
        }else{
        var success=document.getElementById('success');
        success.innerHTML="Operation Failure";
        success.style.display="block";
      }

      }

    };
    xhttp.open("POST",url,true);
    xhttp.setRequestHeader("Content-Type","application/json");
    var data=JSON.stringify({"name":username,"pass":password});
    console.log(data);
    xhttp.send(data);
  }
/*
@BuradaVivek
@This handles Cookies
*/
function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
