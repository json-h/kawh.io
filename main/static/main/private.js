function toggleFields () {

    var fields = document.getElementsByName("priv");
    for (field in fields){
        if (fields[field].style.display === "none") {
            fields[field].style.display = "block";
        } else {
            fields[field].style.display = "none";
        }
    }

}