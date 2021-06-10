function login() {
    let id_give = $('#userid').val()
    let pw_give = $('#userpw').val()

    if (id_give.trim() == '') {
        alert('아이디를 제대로 입력해주세요')
    }

    if (pw_give.trim() == '') {
        alert('비밀번호를 제대로 입력해주세요')

    } else {
        $.ajax({
            type: "POST",
            url: "/api/login",
            data: {
                id_give: id_give,
                pw_give: pw_give
            },

            success: function (response) {
                if (response['result'] == 'success') {
                    $.cookie('loginToken', response['token']);

                    alert('로그인에 성공하였습니다!')
                    window.location.href = '/'
                } else {
                    alert(response['msg'])
                }
            }
        })
    }
}