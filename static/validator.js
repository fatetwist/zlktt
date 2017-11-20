function Ifnocontent(input,alertmsg){
    with(input){
        if(value == ""){
            alert(alertmsg);
            return false;
        }
        else{return True}
    }
}