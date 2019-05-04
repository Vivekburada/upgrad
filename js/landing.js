/*
@BuradaVivek
@vivekburada97@gmail.com
@This project is built for UpGrad
Date 4th May
*/


var link="http://0.0.0.0:5000";

var item = {user:null,name:null, price:0, quantity:0, total:0,url:null}
item.user = getCookie("user")
console.log(item);
function toggle(){
$(".lightbox-blanket").toggle();
}

/*
@BuradaVivek
@This below code Logs out User
*/

    if (window.history && history.pushState) {
    addEventListener('load', function() {
        history.pushState(null, null, null); // creates new history entry with same URL
        addEventListener('popstate', function() {
            var stayOnPage = confirm("You will be logged out of current session!");
            if (!stayOnPage) {
                history.pushState(null, null, null);
                logout();
                console.log("Logging out here!");

            } else {

                  history.back()
            }
        });
    });
  }



function OpenProduct(i){

// @BuradaVivek


  var image = $('.product-image[item-data="'+i+'"] img');
  console.log(i)
  item.url=$(image).attr("src")
  var lbi = $('.lightbox-blanket .product-image img');
  console.log($(image).attr("src"));
  $(lbi).attr("src", $(image).attr("src"));

var j = $('.product-price[item-data="'+i+'"] ')
console.log(j);
item.price =  $(j).attr("price-data");
 console.log(item.price);

 var lbprice = $('.lightbox-blanket .product-info .product-price');
 if(lbprice){
   $(lbprice).html(item.price);
 }

var name = $('.product-title[item-data="'+i+'"]')
// console.log(name)
item.name = $(name).attr("data-value")
console.log(item.name);
var lbname = $('.lightbox-blanket .product-title')
console.log(lbname);
if(lbname){
  $(lbname).html(item.name)
}






  $(".lightbox-blanket").toggle();


  $("#product-quantity-input").val("0");
  CalcPrice (0);

}


function GoBack(){
  $(".lightbox-blanket").toggle();
}


function CalcPrice (qty){
  var price =  item.price.split(/(\s+)/);
console.log(price[2])
   var total = parseFloat(parseInt(price[2]) * qty).toFixed(2);
  $(".product-checkout-total-amount").text(total);
  item.total= String(total)
}


$(document).on("click", ".product-quantity-subtract", function(e){
  var value = $("#product-quantity-input").val();

  var newValue = parseInt(value) - 1;
  if(newValue < 0) newValue=0;
  $("#product-quantity-input").val(newValue);
  CalcPrice(newValue);
  item.quantity=String(newValue)
});


$(document).on("click", ".product-quantity-add", function(e){
  var value = $("#product-quantity-input").val();

  var newValue = parseInt(value) + 1;
  $("#product-quantity-input").val(newValue);
  CalcPrice(newValue);
  item.quantity= String(newValue)
});

$(document).on("blur", "#product-quantity-input", function(e){
  var value = $("#product-quantity-input").val();
  //console.log(value);
  CalcPrice(value);
  item.quantity = String(value)
});


function AddToCart(e){

  e.preventDefault();
  var qty = $("#product-quantity-input").val();
  if(qty === '0'){

    var toast = '<div class="toast toast-success">Add items to Wishlist.</div>';
    $("body").append(toast);
    setTimeout(function(){
    $(".toast").addClass("toast-transition");
      }, 100);
    setTimeout(function(){
      $(".toast").remove();
    }, 3500);

    return;}

    console.log(item)

    mail(item)

  var toast = '<div class="toast toast-success">Added '+ qty +' to Wishlist.</div>';
  $("body").append(toast);
  setTimeout(function(){
  $(".toast").addClass("toast-transition");
    }, 100);
  setTimeout(function(){
    $(".toast").remove();
  }, 3500);


}

function mail(item){

  var url=link+"/api/v1/wishlist";
  var xhttp=new XMLHttpRequest();

  xhttp.onreadystatechange=function() {
    if (this.readyState==4){
      console.log(this.status);
      if (this.status==200)
      {
        console.log("Mailing Successful");

      }else{

      console.log("Mailing failed")
    }

    }

  };
  xhttp.open("POST",url,true);
  xhttp.setRequestHeader("Content-Type","application/json");
  item = JSON.stringify(item);

  xhttp.send(item);

}



function logout(){

  setCookie("user", username, -999999);
/*
  var url=link+"/api/v1/users/logout";
  var xhttp=new XMLHttpRequest();
  xhttp.onreadystatechange=function() {
    if (this.readyState==4){
      console.log(this.status);
      if (this.status==200)
      {
        console.log("Session Ended");
      }else{
      console.log("Session Ending failed")
    }

    }
  };
  xhttp.open("GET",url,true);
  xhttp.setRequestHeader("Content-Type","application/json");
  item = JSON.stringify({});
  xhttp.send(item);
  */


}


var search = document.getElementById("searchloop");
search.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        validate(e);
    }
});

function validate(e) {
    var search = e.target.value;
    console.log(search);

    var url=link+"/api/v1/search/"+search;
		var xhttp=new XMLHttpRequest();
	    xhttp.onreadystatechange=function() {
	    	if (this.readyState==4){

		        if(this.status==200)
		        {
		        	console.log(this.status);
		        	var json = JSON.parse(xhttp.responseText);
		        	console.log(xhttp.responseText);
              console.log(json["i"])
              OpenProduct(json["i"])



					};

		    	}
		    	else if(this.status==204)
		    	{


		    	}
		    	else if(this.status==405)
		    	{

		    	}
			}


		xhttp.open("GET",url,true);
	    xhttp.setRequestHeader("Content-Type","application/json");
	    var data=JSON.stringify({"name":search});
	    //console.log(data);
	    xhttp.send(data);


}

/*
@BuradaVivek
@This handles Cookies
*/
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
