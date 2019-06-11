let ArrOldValue = [];
window.onload = function () {
    let arr = document.getElementsByName("info");
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].type === "text" || arr[i].type === "date") {
            ArrOldValue[ArrOldValue.length] = [arr[i].id, arr[i].value];
        }
    }
};

function display_add_info() {
    document.getElementById('light').style.display = 'block';
    document.getElementById('fade').style.display = 'block';
    document.getElementById('editinfo').style.display = 'block';

}

function upload() {
    let data = null;

    let modify_info = [];
    modify_info.push({
                    "commodity_name": document.getElementById("commodity_name").value,
                    "type": document.getElementById("type").value,
                    "price": document.getElementById("price").value,
                    "num": document.getElementById("num").value,
                    "desc": document.getElementById("desc").value,
                    "pic": document.getElementById("pic").value,
                });

    if (modify_info.length === 0) {
        alert("无上传内容");
        return;
    }

    data = JSON.stringify({"commodity_info": modify_info, "status": "modify_me",})

    $.ajax({
        url: "/upload/",
        type: "POST",
        dataType: 'json',
        data: data,
        beforeSend:function(xhr,settings){
            xhr.setRequestHeader("X-CSRFToken", "{{csrf_token}}");
        },
        contentType: "application/json",  //缺失会出现URL编码，无法转成json对象
        success: function (result) {
            alert("上传成功");
            document.getElementById('light').style.display = 'none';
            document.getElementById('fade').style.display = 'none';
            document.getElementById('editinfo').style.display = 'none';
            window.location.reload();
        },
        error: function (result) {
            alert("上传失败");
        }
    });
}

