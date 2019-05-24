 <?php if(!defined('IN_GS')){die('you cannot load this page directly'); } ?>
 
  <noscript>
    Do pełnej funkcjonalności strony potrzebujesz włączonej obsługi skryptów.
    Tu znajdziesz <a href="https://www.enable-javascript.com/pl/" target="_blank">
    instrukcje, które pozwolą Ci włączyć skrypty w Twojej przeglądarce</a>.
  </noscript>

  <script>
    var $buoop = {notify:{e:-6,f:-4,o:-4,s:-2,c:-4},insecure:true,api:5};
    function $buo_f(){
      var e = document.createElement("script");
      e.src = "http://browser-update.org/update.min.js";
      document.body.appendChild(e);
    };
    try {document.addEventListener("DOMContentLoaded", $buo_f,false)}
    catch(e){window.attachEvent("onload", $buo_f)}
  </script>
