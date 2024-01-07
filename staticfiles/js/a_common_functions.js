function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
async function delUser(id) {

    swal({
        title: "Ma hubtaa in aad ?",
        text: "Bixinaysid Userkaan",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/userProfile-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Graysay User", {
                        icon: "success",
                    });
                    location.reload()
                    
                }
            });

        }
    });

}

async function delQestion(id) {

    swal({
        title: "Ma hubtaa in aad ?",
        text: "Bixinaysid SU'aashaan",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/probQuestion-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Graysay Su'aasha", {
                        icon: "success",
                    });
                    location.reload()
                    
                }
            });

        }
    });

}


async function delAppointment(id) {

    swal({
        title: "Ma hubtaa in aad ?",
        text: "Cancel bookinkaan",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/doctorAppointment-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Graysay Su'aasha", {
                        icon: "success",
                    });
                    location.reload()
                    
                }
            });

        }
    });

}

async function delListeningCilajWithQurans(id) {

    swal({
        title: "Ma hubtaa in aad ?",
        text: "Bixinaysid Dhagaysiga",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/listeningCilajWithQuran-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Graysay Cilaajka", {
                        icon: "success",
                    });
                    location.reload()
                    
                }
            });

        }
    });

}
async function delProductInfo(id) {

    swal({
        title: "Ma hubtaa in aad ?",
        text: "Bixinaysid Product",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/productInfo-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Graysay Su'aasha", {
                        icon: "success",
                    });
                    location.reload()
                    
                }
            });

        }
    });

}
async function delAdkarWithTalo(id) {

    swal({
        title: "Ma hubtaa in aad ?",
        text: "Bixinaysid  Adkar ama taladan",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/adkarQuranWithTalo-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Graysay "+type, {
                        icon: "success",
                    });
                    location.reload()
                    
                }
            });

        }
    });

}
