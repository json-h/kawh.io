function toggleFields () {
    
    var fields = document.getElementsByName("priv");

    if(document.getElementById("chk").checked){
        for(i=0; i<2; i++){
            fields[i].style.display = "block";
        }
    }else{
        for(i=0; i<2; i++){
            fields[i].style.display = "none";
        }
    }
    

}