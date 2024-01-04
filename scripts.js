(function(){
    

    function changeStuff(){
        document.getElementById("change").innerHTML="Hello JavaScript!";
    }

    toggleCartBtn.addEventListener("click", function(e) {
        e.preventDefault();
        changeStuff();
      });
})();