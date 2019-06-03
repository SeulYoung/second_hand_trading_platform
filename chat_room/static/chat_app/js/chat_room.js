document.querySelector('.chat[data-chat=person1]').classList.add('active-chat');
document.querySelector('.person[data-chat=person1]').classList.add('active');


var friends = {
  list: document.querySelector('ul.people'),
  all: document.querySelectorAll('.left .person'),
  name: '' },

chat = {
  container: document.querySelector('.container .right'),
  current: null,
  person: null,
  name: document.querySelector('.container .right .top .name') };

// friends.all.forEach(function (f) {
//   f.addEventListener('mousedown', function () {
//     f.classList.contains('active') || setAciveChat(f);
//   });
// });
//
// function setAciveChat(f) {
//   friends.list.querySelector('.active').classList.remove('active');
//   f.classList.add('active');
//   chat.current = chat.container.querySelector('.active-chat');
//   chat.person = f.getAttribute('data-chat');
//   chat.current.classList.remove('active-chat');
//   chat.container.querySelector('[data-chat="' + chat.person + '"]').classList.add('active-chat');
//   friends.name = f.querySelector('.name').innerText;
//   chat.name.innerHTML = friends.name;
// }

function GotoOtherPerson() {
    let other = document.getElementById("other_room");
    let room_name = other.value.toLowerCase().replace(" ", "_");
    if (!/^([a-z\-_]){3,12}$/.test(room_name)) {
        myAlert("invalid");
        return;
    }
    if(room_name===roomName){
        myAlert("repeat");
        return;
    }
    window.location.href='../' + room_name;
}

// function refresh() {
//     $.ajax({
//         url: "/HotRoomList/",
//         dataType: 'json',
//         success: function (data) {
//             let list = data['hot_room'];
//             document.getElementById("hot_room").innerHTML = "";
//             for(let m=0;m<list.length;m++){
//                 let new_a = document.createElement("a");
//                 if(list[m].room_name === roomName)
//                     new_a.setAttribute("onclick", "myAlert('repeat')");
//                 else
//                     new_a.setAttribute("href", "../" + list[m].room_name);
//                 let new_li = document.createElement("li");
//                 new_li.setAttribute("class", "person");
//                 let new_img = document.createElement("img");
//                 new_img.setAttribute("class", "roomLogo");
//                 new_img.setAttribute("src", "/static/chat_app/img/" + list[m].no + ".png");
//                 new_li.appendChild(new_img);
//                 let new_name = document.createElement("span");
//                 new_name.setAttribute("class", "name");
//                 new_name.setAttribute("name", "hot_room_name");
//                 new_name.innerHTML = list[m].room_name;
//                 new_li.appendChild(new_name);
//                 let new_num= document.createElement("span");
//                 new_num.setAttribute("class", "num");
//                 new_num.innerHTML = list[m].room_user_num + " people";
//                 new_li.appendChild(new_num);
//                 new_a.appendChild(new_li);
//                 let the_hot_room = document.getElementById("hot_room");
//                 the_hot_room.appendChild(new_a);
//             }
//         },
//         error: function (data) {
//             console.log("error");
//         }
//     });
// }