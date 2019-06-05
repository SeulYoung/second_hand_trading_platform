function dislayMessageNotification() {
    let state=document.getElementById('displayMe').style.display;
    if(state==="none")
        document.getElementById('displayMe').style.display = "block";
    else
        document.getElementById('displayMe').style.display = "none";
}