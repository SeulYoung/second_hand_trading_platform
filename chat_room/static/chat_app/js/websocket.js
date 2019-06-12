// let roomName = document.getElementById("name").innerHTML;
let roomName = "yyy";
let judgeUser = document.getElementById("myname").innerHTML;
// var chatSocket = new WebSocket('ws://' + window.location.host);
// var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');
var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/yyy/');

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log(data);

    // let type = data['type'];
    // let to_user = data['to_user'];
    let from_user = data['from_user'];
    let message = data['message'];

    add_new_message(from_user, message);
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

    let t = new Date();
    let hour = t.getHours();
    let minute = t.getMinutes();
    let sendTime = hour + ((minute < 10) ? ":0" : ":") + minute + " " + ((hour > 12) ? "PM" : "AM");
    // let to_user="wkz";
    chatSocket.send(JSON.stringify({
        'message': message,
        'from_user': judgeUser,
        // 'to_user': to_user,
        'time': sendTime,
    }));

    messageInputDom.value = '';
    document.getElementById("chat-message-input1").innerHTML = "";
};

function add_new_message(user, message) {
    let chatBox = document.getElementById("chat_box");

    // let judgeUser;
    // if (message === 'yyy')
    //     judgeUser = 'yyy';
    // else
    //     judgeUser = 'yxy';
    // let judgeUser = document.getElementById("myname").innerHTML;
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

    appendUnicode(new_message, message);

    // document.getElementById("preview").innerHTML = message;
    new_div_message.appendChild(new_message);
    new_div.appendChild(new_div_message);
    chatBox.appendChild(new_div);
    chatBox.scrollTop = chatBox.scrollHeight;


    // let t = new Date();
    // let hour = t.getHours();
    // let minute = t.getMinutes();
    // document.getElementById("time").innerHTML = hour + ((minute < 10) ? ":0" : ":") + minute + " " + ((hour > 12) ? "PM" : "AM");
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