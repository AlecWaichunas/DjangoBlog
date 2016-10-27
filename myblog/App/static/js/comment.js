window.fbAsyncInit = function() {
  FB.init({
    appId      : '1764321817163236',
    xfbml      : true,
    version    : 'v2.6'
  });
};

(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "//connect.facebook.net/en_US/sdk.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));


statusChangeCallback = function(response){
    if(response.status == "connected"){
        FB.api('/me', function(response){
            name = response.name;
            console.log(response.name)
            $("#comment_author").innerHTML = name;
            $("#comment_author").val(name);
        })
        $("#submit_button").click()
    }
}

checkLoginState = function(){
    FB.getLoginStatus(function(response){
        statusChangeCallback(response)
        console.log('logging in - posting')
    })
}
