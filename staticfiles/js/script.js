
function InlineSearch(query) {
    console.log(query)
    let data = JSON.stringify(query)
    if (window.XMLHttpRequest) {
        var xhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        var xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            console.log(data)
            let elem = ``
            let list = document.getElementById('result-list')
            for (let i = 0; i < data.object_list.length; i++) {

                obj = data.object_list[i]
                let panel = ` <a href="/post/${obj.slug}" class="panel-block is-active">
                <h5>
                <i class="fas fa-tag has-text-info mx-1"></i>
                ${obj.name}
                </h5>
                </a>`
                elem += panel
            }
            for (let i = 0; i < data.obj_list.length; i++) {

                obj = data.obj_list[i]
                let panel = ` <a href="/post/${obj.slug}" class="panel-block is-active">
                                    <h5>
                                    <i class="fas fa-tag has-text-info mx-1"></i>
                                    ${obj.description.slice(0, 100)}
                                    </h5>
                                </a>`
                elem += panel
            }
            elem += ``
            list.innerHTML = elem
        }
    }
    var url = "/search/"
    xhttp.open("GET", url + `?data=${data}`, true);
    xhttp.send();
}
window.onload = function () {
    if (window.history.replaceState) {
        window.history.replaceState(null, null, window.location.href);
    }
};
