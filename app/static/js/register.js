
function register() {
    let id_give = $('#userid').val()
    if (id_give.trim() == '') {
        alert('아이디를 제대로 입력해주세요')
    }

    let pw_give = $('#userpw').val()
    if (pw_give.trim() == '') {
        alert('비밀번호를 제대로 입력해주세요')
    }

    let nickname_give = $('#username').val()
    if (nickname_give.trim() == '') {
        alert('닉네임을 제대로 입력해주세요')
    }

    let email_give = $('#email').val()
    if (email_give.trim() == '') {
        alert('이메일을 제대로 입력해주세요')

    } else {
        $.ajax({
            type: "POST",
            url: "/api/register",
            data: {
                id_give: id_give,
                pw_give: pw_give,
                nickname_give: nickname_give,
                email_give: email_give
            },

            success: function (response) {
                if (response['result'] == 'success') {
                    alert('회원가입이 완료되었습니다.')
                    window.location.href = '/login'
                } else {
                    alert(response['msg'])
                }
            }
        })
    }
}