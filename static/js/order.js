let ArrOldValue = [];
let course_old_length;
window.onload = function () {
    course_old_length = document.getElementsByName("course_info").length;
    let arr = [];
    arr[0] = document.getElementsByName("student_info");
    arr[1] = document.getElementsByName("grade");
    arr[2] = document.getElementsByName("class_info");
    arr[3] = document.getElementsByName("teacher_info");
    arr[4] = document.getElementsByName("course_info");
    arr[5] = document.getElementsByName("course_info_info");
    for (let n = 0; n < arr.length; n++) {
        for (let i = 0; i < arr[n].length; i++) {
            if (arr[n][i].type === "number" || arr[n][i].type === "date" || arr[n][i].type === "text") {
                ArrOldValue[ArrOldValue.length] = [arr[n][i].id, arr[n][i].value];
            }
        }
    }
};

function info(uid, table) {
    let post_data = null;

    if (table === "table_student")
        post_data = {"sno": uid, "status": "search",};
    else if (table === "table_class")
        post_data = {"classname": uid, "status": "search",};
    else if (table === "table_teacher")
        post_data = {"tno": uid, "status": "search",};
    else
        post_data = {"cno": uid, "status": "search",};


    let form = document.createElement("form");
    form.action = "";
    form.method = "POST";

    let input;
    for (let key in post_data) {
        input = document.createElement("input");
        input.type = "hidden";
        input.name = key;
        input.value = post_data[key];

        form.appendChild(input);
    }

    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

function delete_info(uid, table) {
    let post_data = null;

    if (table === "table_student")
        post_data = {"sno": uid, "status": "delete",};
    else if (table === "table_class")
        post_data = {"classname": uid, "status": "delete",};
    else if (table === "table_teacher")
        post_data = {"tno": uid, "status": "delete",};
    else if (table === "table_course")
        post_data = {"cno": uid, "status": "delete",};
    else
        post_data = {"id": uid, "status": "delete",};


    let form = document.createElement("form");
    form.action = "";
    form.method = "POST";

    let input;
    for (let key in post_data) {
        input = document.createElement("input");
        input.type = "hidden";
        input.name = key;
        input.value = post_data[key];

        form.appendChild(input);
    }

    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

function modify_info(table, modify_table, no) {
    let data = null;

    if (table === "table_student") {
        let modify_info = [];
        if (modify_table === "student") {
            for (let i = 0; i < ArrOldValue.length; i++) {
                let obj = document.getElementById(ArrOldValue[i][0]);
                if (obj.type === "text" || obj.type === "date") {
                    if (obj.value !== ArrOldValue[i][1]) {
                        modify_info.push({
                            "sno": no,
                            "sex": document.getElementById("sex").value,
                            "sbirthday": document.getElementById("sbirthday").value,
                            "phone": document.getElementById("phone").value,
                            "classname": document.getElementById("classname").value,
                            "place": document.getElementById("place").value,
                            "description": document.getElementById("description").value,
                        });

                        break;
                    }
                }
            }
        }
        else {
            for (let i = 0; i < ArrOldValue.length; i++) {
                let obj = document.getElementById(ArrOldValue[i][0]);
                if (obj.type === "number") {
                    if (obj.value !== ArrOldValue[i][1]) {
                        modify_info.push({
                            "cname": ArrOldValue[i][0],
                            "sno": no,
                            "old_grade": ArrOldValue[i][1],
                            "new_grade": obj.value
                        });
                    }
                }
            }
        }

        if (modify_info.length === 0) {
            alert("不存在修改内容");
            return;
        }

        data = JSON.stringify({"modify_table": modify_table, "modify_info": modify_info, "status": "modify",})
    }
    else if (table === "table_class") {
        let modify_info = [];
        if (modify_table === "class") {
            for (let i = 0; i < ArrOldValue.length; i++) {
                let obj = document.getElementById(ArrOldValue[i][0]);
                if (obj.type === "text") {
                    if (obj.value !== ArrOldValue[i][1]) {
                        modify_info.push({
                            "classname": no,
                            "teacher_name": document.getElementById("teacher_name").value,
                            "honor": document.getElementById("honor").value,
                            "slogan": document.getElementById("slogan").value,
                            "remark": document.getElementById("remark").value,
                        });

                        break;
                    }
                }
            }
        }

        if (modify_info.length === 0) {
            alert("不存在修改内容");
            return;
        }

        data = JSON.stringify({"modify_table": modify_table, "modify_info": modify_info, "status": "modify",})
    }
    else if (table === "table_teacher") {
        let modify_info = [];
        if (modify_table === "teacher") {
            for (let i = 0; i < ArrOldValue.length; i++) {
                let obj = document.getElementById(ArrOldValue[i][0]);
                if (obj.type === "text" || obj.type === "date") {
                    if (obj.value !== ArrOldValue[i][1]) {
                        modify_info.push({
                            "tno": no,
                            "sex": document.getElementById("sex").value,
                            "tbirthday": document.getElementById("tbirthday").value,
                            "phone": document.getElementById("phone").value,
                            "place": document.getElementById("place").value,
                            "position": document.getElementById("position").value,
                        });

                        break;
                    }
                }
            }
        }

        if (modify_info.length === 0) {
            alert("不存在修改内容");
            return;
        }

        data = JSON.stringify({"modify_table": modify_table, "modify_info": modify_info, "status": "modify",})
    }
    else {
        let modify_info = [];
        for (let i = 0; i < ArrOldValue.length; i++) {
            let obj = document.getElementById(ArrOldValue[i][0]);
            if (obj.type === "text") {
                if (obj.value !== ArrOldValue[i][1]) {
                    modify_info.push({
                        "cno": no,
                        "course_type": document.getElementById("course_type").value,
                        "credit": document.getElementById("credit").value,
                        "course_time": document.getElementById("course_time").value,
                        "remark": document.getElementById("remark").value,
                    });

                    break;
                }
            }
        }

        if (modify_info.length === 0) {
            alert("不存在修改内容");
            return;
        }

        data = JSON.stringify({"modify_table": modify_table, "modify_info": modify_info, "status": "modify",})
    }

    $.ajax({
        url: "",
        type: "POST",
        dataType: 'json',
        data: data,
        contentType: "application/json",  //缺失会出现URL编码，无法转成json对象
        success: function (result) {
            alert("修改成功");
        },
        error: function (result) {
            alert("修改失败");
        }
    });
}

function display_add_info() {
    document.getElementById('light').style.display = 'block';
    document.getElementById('fade').style.display = 'block';
}

function add_info(table) {
    let post_data = null;
    let judge_null = 0;

    if (table === "学生表") {
        let sname = document.getElementById("sname").value;
        let sno = document.getElementById("sno").value;
        let sex = document.getElementById("sex").value;
        let sbirthday = document.getElementById("sbirthday").value;
        let phone = document.getElementById("phone").value;
        let classname = document.getElementById("classname").value;

        if (sname === "" || sno === "" || classname === "")
            judge_null++;
        if (judge_null !== 0) {
            alert("*内容不能为空");
            return;
        }
        post_data = {
            "sname": sname, "sno": sno, "sex": sex, "sbirthday": sbirthday,
            "phone": phone, "classname": classname, "status": "add",
        };
    }
    else if (table === "班级表") {
        let classname = document.getElementById("classname").value;
        let teacher_name = document.getElementById("teacher_name").value;
        let honor = document.getElementById("honor").value;
        let slogan = document.getElementById("slogan").value;

        if (classname === "" || teacher_name === "")
            judge_null++;
        if (judge_null !== 0) {
            alert("*内容不能为空");
            return;
        }

        post_data = {
            "classname": classname, "teacher_name": teacher_name, "honor": honor,
            "slogan": slogan, "status": "add",
        };
    }
    else if (table === "教师表") {
        let tname = document.getElementById("tname").value;
        let tno = document.getElementById("tno").value;
        let sex = document.getElementById("sex").value;
        let tbirthday = document.getElementById("tbirthday").value;
        let phone = document.getElementById("phone").value;
        let place = document.getElementById("place").value;
        let position = document.getElementById("position").value;

        if (tname === "" || tno === "")
            judge_null++;
        if (judge_null !== 0) {
            alert("*内容不能为空");
            return;
        }

        post_data = {
            "tname": tname, "tno": tno, "sex": sex, "tbirthday": tbirthday,
            "phone": phone, "place": place, "position": position, "status": "add",
        };
    }
    else if (table === "课程表") {
        let cname = document.getElementById("cname").value;
        let cno = document.getElementById("cno").value;
        let credit = document.getElementById("credit").value;
        let course_time = document.getElementById("course_time").value;
        let course_teacher = document.getElementById("teacher_no").value;

        if (cname === "" || cno === "" || credit === "" || course_time === "" || course_teacher === "")
            judge_null++;
        if (judge_null !== 0) {
            alert("*内容不能为空");
            return;
        }

        post_data = {
            "cname": cname, "cno": cno, "credit": credit, "course_time": course_time,
            "course_teacher": course_teacher, "status": "add",
        };
    }
    else {
        let sno = document.getElementById("student_no").value;
        let cno = document.getElementById("course_no").value;
        let sc_grade = document.getElementById("sc_grade").value;

        if (sno === "" || cno === "" || sc_grade === "")
            judge_null++;
        if (judge_null !== 0) {
            alert("*内容不能为空");
            return;
        }

        post_data = {"sno": sno, "cno": cno, "sc_grade": sc_grade, "status": "add",};
    }

    let form = document.createElement("form");
    form.action = "";
    form.method = "POST";

    let input;
    for (let key in post_data) {
        input = document.createElement("input");
        input.type = "hidden";
        input.name = key;
        input.value = post_data[key];

        form.appendChild(input);
    }

    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}