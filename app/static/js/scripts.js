/*!
* Start Bootstrap - Landing Page v6.0.0 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/


$(document).ready(function () {
    setUserInfo()
});


function setUserInfo() {
    let userInfo = $('#user-info')
    let token = $.cookie('loginToken')
    console.log(token)

    if (token === undefined) {
        window.location.href = '/login'
    } else {
        $.ajax({
            type: "POST",
            url: "/user",
            headers: {'authorization': `Bearer ${token}`},
            data: {},
            success: function (response) {
                if (response['result'] === 'success') {
                    let id = response['id']
                    userInfo.append(`
                        <a class="navbar-brand" href="#">${id}</a>
                        <a class="btn btn-secondary" onclick="logOut()">Log Out</a>
                    `)
                } else {
                    alert('다시 로그인해주세요.')
                    window.location.href = '/login'
                }
            }
        })
    }

}


function logOut() {
    $.removeCookie('loginToken', {path: '/'})
    alert('로그아웃 되었습니다.')
    window.location.href = '/login'
}


function showArticles() {
    let region = $('.form-select').val()
    console.log(region)

    $.ajax({
        type: "GET",
        url: "/camping_data",
        data: {'region_give': region},
        success: function (response) {
            if (response["result"] == "success") {
                let articles = response['articles']
                for (let i = 0; i < articles.length; i++) {
                    let article = articles[i]
                    let campsite_name = article['campsite_name']
                    let category = article['category']
                    let link = article['link']
                    let address = article['address']
                    let road_address = article['road_address']
                    makeCard(campsite_name, category, link, address, road_address)
                }
            } else {
                alert('검색에 실패하였습니다.');
            }
        }
    })
}

function makeCard(campsite_name, category, link, address, road_address) {
    let tempHtml = `<div class="card">
            <div class="card-body">
            <a href="${link}" target="_blank" class="card-title">${campsite_name}</a>
            <p class="card-text">${category}</p>
            <p class="card-text comment">${address}</p>
            <p class="card-text comment">${road_address}</p>
            </div>
        </div>`;
    $("#cards-box").append(tempHtml);
}