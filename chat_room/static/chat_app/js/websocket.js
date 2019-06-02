// let roomName = document.getElementById("name").innerHTML;
let roomName = "yyy";
// var chatSocket = new WebSocket('ws://' + window.location.host);
// var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');
var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/yyy/');

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log(data);

    // let type = data['type'];
    // let user = data['user'];
    let message = data['message'];

     add_new_message('message', 'yxy', message);
    // update_room_list(type);
};

chatSocket.onopen = function () {
    // update_room_list("user in");
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
    myAlert("close");
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    let messageInputDom = document.querySelector('#chat-message-input');
    let message = messageInputDom.value;

    if (message.length === 0) {
        myAlert("null");
        return;
    }

    chatSocket.send(JSON.stringify({
        'message': message
    }));

    messageInputDom.value = '';
    document.getElementById("chat-message-input1").innerHTML = "";
};

function add_new_message(type, user, message) {
    let chatBox = document.getElementById("chat_box");
    if (type !== "user out") {
        if (type === "message") {
            let judgeUser = document.getElementById("myname").innerHTML;
            let new_div = document.createElement("div");
            if (user === judgeUser)
                new_div.setAttribute("class", "chat_record me_record");
            else
                new_div.setAttribute("class", "chat_record you_record");
            let new_img = document.createElement("img");
            if (user === judgeUser)
                new_img.setAttribute("class", "portrait me_portrait");
            else
                new_img.setAttribute("class", "portrait you_portrait");
            new_img.setAttribute("src", "/static/chat_app/img/thomas.jpg");
            new_img.setAttribute("alt", "");
            new_div.appendChild(new_img);
            let new_div_message = document.createElement("div");
            if (user === judgeUser)
                new_div_message.setAttribute("class", "me_message");
            else
                new_div_message.setAttribute("class", "you_message");
            let new_span = document.createElement("span");
            if (user === judgeUser)
                new_span.setAttribute("class", "user_name you_name");
            else
                new_span.setAttribute("class", "user_name");
            new_span.innerHTML = user;
            new_div_message.appendChild(new_span);
            let new_message = document.createElement("div");
            if (user === judgeUser)
                new_message.setAttribute("class", "bubble me");
            else
                new_message.setAttribute("class", "bubble you");
            // new_message.innerHTML = message;


            appendUnicode(new_message, message);


            document.getElementById("preview").innerHTML = message;
            new_div_message.appendChild(new_message);
            new_div.appendChild(new_div_message);
            chatBox.appendChild(new_div);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        else {
            let new_member_in = document.createElement("div");
            new_member_in.setAttribute("class", "conversation-start");
            let new_user_in = document.createElement("span");
            new_user_in.innerHTML = "user " + user + " enters the chat room.";
            new_member_in.appendChild(new_user_in);
            document.getElementById("preview").innerHTML = "user " + user + " enters the chat room.";

            chatBox.appendChild(new_member_in);
            chatBox.scrollTop = chatBox.scrollHeight;

            let sideMenuContainer = document.getElementById("sideMenuContainer");
            let new_member_div = document.createElement("div");
            new_member_div.setAttribute("class", "user_list");
            new_member_div.setAttribute("id", "user_" + user);
            let new_member_portrait = document.createElement("img");
            new_member_portrait.setAttribute("class", "user_portrait");
            new_member_portrait.setAttribute("src", "/static/chat_app/img/thomas.jpg");
            new_member_portrait.setAttribute("alt", "");
            new_member_div.appendChild(new_member_portrait);
            let new_member_name = document.createElement("span");
            new_member_name.setAttribute("class", "fa");
            new_member_name.innerHTML = user;
            new_member_div.appendChild(new_member_name);
            sideMenuContainer.appendChild(new_member_div);
        }

        let t = new Date();
        let hour = t.getHours();
        let minute = t.getMinutes();
        document.getElementById("time").innerHTML = hour + ((minute < 10) ? ":0" : ":") + minute + " " + ((hour > 12) ? "PM" : "AM");
    }
    else {
        let removeElement = document.getElementById("user_" + user);
        removeElement.remove();

        let new_member_out = document.createElement("div");
        new_member_out.setAttribute("class", "conversation-start");
        let new_user_out = document.createElement("span");
        new_user_out.innerHTML = "user " + user + " left the chat room.";
        new_member_out.appendChild(new_user_out);
        document.getElementById("preview").innerHTML = "user " + user + " left the chat room.";

        chatBox.appendChild(new_member_out);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function update_room_list(type) {
    if (type !== "message") {
        $.ajax({
            url: "/HotRoomList/",
            dataType: 'json',
            success: function (data) {
                let list = data['hot_room'];
                document.getElementById("hot_room").innerHTML = "";
                for (let m = 0; m < list.length; m++) {
                    let new_a = document.createElement("a");
                    if (list[m].room_name === roomName)
                        new_a.setAttribute("onclick", "myAlert('repeat')");
                    else
                        new_a.setAttribute("href", "../" + list[m].room_name);
                    let new_li = document.createElement("li");
                    new_li.setAttribute("class", "person");
                    let new_img = document.createElement("img");
                    new_img.setAttribute("class", "roomLogo");
                    new_img.setAttribute("src", "/static/chat_app/img/" + list[m].no + ".png");
                    new_li.appendChild(new_img);
                    let new_name = document.createElement("span");
                    new_name.setAttribute("class", "name");
                    new_name.setAttribute("name", "hot_room_name");
                    new_name.innerHTML = list[m].room_name;
                    new_li.appendChild(new_name);
                    let new_num = document.createElement("span");
                    new_num.setAttribute("class", "num");
                    new_num.innerHTML = list[m].room_user_num + " people";
                    new_li.appendChild(new_num);
                    new_a.appendChild(new_li);
                    let the_hot_room = document.getElementById("hot_room");
                    the_hot_room.appendChild(new_a);
                }
            },
            error: function (data) {
                console.log("error");
            }
        });
    }

}

function appendUnicode(element, input) {
    var k, len, split_on_unicode, text, val;
    if (!input) {
        return '';
    }
    if (!Config.rx_codes) {
        Config.init_unified();
    }
    split_on_unicode = input.split(Config.rx_codes);
    for (k = 0, len = split_on_unicode.length; k < len; k++) {
        text = split_on_unicode[k];
        val = '';
        if (Config.rx_codes.test(text)) {
            val = Config.reversemap[text];
            if (val) {
                val = ':' + val + ':';
                val = $.emojiarea.createIcon($.emojiarea.icons[val]);

                element.innerHTML += val;
            }
        } else {
            // val = document.createTextNode(text);
            element.innerHTML += text;
        }
    }
    return input.replace(Config.rx_codes, function (m) {
        var $img;
        val = Config.reversemap[m];
        if (val) {
            val = ':' + val + ':';
            $img = $.emojiarea.createIcon($.emojiarea.icons[val]);
            return $img;
        } else {
            return '';
        }
    });

}