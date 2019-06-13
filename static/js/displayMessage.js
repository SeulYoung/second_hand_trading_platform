function dislayMessageNotification() {
    let state = document.getElementById('displayMe').style.display;
    if (state === "none") {
        document.getElementById('displayMe').style.display = "block";

        $.ajax({
            url: "/NewMessage/",
            dataType: 'json',
            success: function (data) {
                let message_list = data['message_list'];
                let messagenNum = message_list.length;
                document.getElementById("newMessage").innerHTML = "";
                for (let m = 0; m < messagenNum; m++) {
                    let websocketId = message_list[m]["websocket_id"];
                    let fromUser = message_list[m]["from_user"];
                    let toUser = message_list[m]["to_user"];
                    let content = message_list[m]["content"];
                    let time = message_list[m]["created_at"];
                    let contents = content.split("\n");
                    let contentsNum = contents.length;
                    let trueTimes = time.split("T");


                    let new_li = document.createElement("li");
                    new_li.setAttribute("class", "media");
                    let new_div1 = document.createElement("div");
                    new_div1.setAttribute("class", "media-left");
                    let new_div2 = document.createElement("div");
                    new_div2.setAttribute("class", "media-body");
                    let new_img = document.createElement("img");
                    new_img.setAttribute("class", "img-circle img-sm");
                    new_img.setAttribute("src", "/static/images/head/placeholder.jpg");
                    let new_span = document.createElement("span");
                    new_span.setAttribute("class", "badge bg-danger-400 media-badge");
                    new_span.innerHTML = contentsNum.toString();
                    new_div1.appendChild(new_img);
                    new_div1.appendChild(new_span);
                    let new_a = document.createElement("a");
                    new_a.setAttribute("class", "media-heading");
                    new_a.setAttribute("href", "#");
                    let new_span1 = document.createElement("span");
                    new_span1.setAttribute("class", "text-semibold messageNmae");
                    new_span1.innerHTML = fromUser;
                    let new_span2 = document.createElement("span");
                    new_span2.setAttribute("class", "media-annotation pull-right");
                    new_span2.innerHTML = trueTimes[0] + " "+ trueTimes[1].substring(0,8);
                    new_a.appendChild(new_span1);
                    new_a.appendChild(new_span2);
                    let new_span3 = document.createElement("span");
                    new_span3.setAttribute("class", "text-muted");
                    new_span3.innerHTML = contents[0];
                    new_div2.appendChild(new_a);
                    new_div2.appendChild(new_span3);
                    new_li.appendChild(new_div1);
                    new_li.appendChild(new_div2);
                    let the_newMessage = document.getElementById("newMessage");
                    the_newMessage.appendChild(new_li);
                }
            },
            error: function (data) {
                console.log("error");
            }
        });
    }
    else
        document.getElementById('displayMe').style.display = "none";
}