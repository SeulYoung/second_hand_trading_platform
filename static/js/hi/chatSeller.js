function chatWithSeller(seller_name) {
    let form = document.createElement("form");
    form.action = "/chatRoom/";
    form.method = "POST";

    let data = {'seller_name': seller_name};

    for (let key in data) {
        let input = document.createElement("input");
        input.type = "hidden";
        input.name = key;
        input.value = data[key];

        form.appendChild(input);
    }

    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}