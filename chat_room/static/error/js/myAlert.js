function myAlert(type) {
    let option;
    if(type === "repeat")
        option = {title: "Error", message: "Sorry, you are already in the chat room!"};
    else if(type === "invalid")
        option = {title: "Error", message: "Invalid name(3 to 12 characters)"};
    else if(type === "close")
        option = {title: "Error", message: "Sorry, you have been disconnected from the server"};
    else if (type === "null")
        option = {title: "Error", message: "Message to be sent can't be null"};

    let top = $(window).height() * 0.3;
    $('body').append('<div class="myModa"><div class="myAlertBox"  style="margin-top:' + top + 'px"><h6>' + option.title + '</h6><p>' + option.message + '</p><div class="btnn sure">OK</div></div></div>');

    $('.btnn.sure').click(function () {
        $('.myModa').remove();
    })
}