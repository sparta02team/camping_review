/*!
* Start Bootstrap - Landing Page v6.0.0 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/


$(document).ready(function () {
    // user 정보
    setUserInfo()
});


$(document).ajaxStart(function() {
    //로딩 중 마우스 커서를 변경
    alert('로딩 중입니다. 잠시만 기다려주세요');
    $('html').css("cursor", "wait");
});


$(document).ajaxStop(function() {
    //로딩이 끝나면 마우스 커서를 원래대로
    $('html').css("cursor", "auto");
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
            headers: { 'authorization': `Bearer ${token}` },
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
    $.removeCookie('loginToken', { path: '/' })
    alert('로그아웃 되었습니다.')
    window.location.href = '/login'
}


function to_review() {
    $.ajax({
        type: 'POST',
        url: '/review',
        data: {'mapx': '300492', 'mapy': '552541', 'title': '난지캠핑장', 'address': '서울특별시 마포구 한강난지로 28'},
        success: function (response) {
            window.location.href = '/review'
        }
    })
}


function showArticles() {
    let region = $('.form-select').val()
    console.log(region)

    $.ajax({
        type: "GET",
        url: "/camping_data",
        data: { 'region_give': region },
        success: function (response) {
            if (response["result"] == "success") {
                let articles = response['articles']
                for (let i = 0; i < articles.length; i++) {
                    let article = articles[i]
                    let campsite_name = article['campsite_name']
                    let category = article['category']
                    let description = article['description']
                    let image = article['image']
                    let link = article['link']
                    let phone = article['phone']
                    let address = article['address']
                    let road_address = article['road_address']
                    let tag = article['tag']
                    makeCard(campsite_name, category, description, image, link, phone, address, road_address, tag)
                }
            }
        },
            error: function (response) {
                alert('검색에 실패하였습니다.');
        }
    })
}


function makeCard(campsite_name, category, description, image, link, phone, address, road_address, tag) {
    let tempHtml = `<div class="card">
                        <div class="card-header" style="background-image: url('${image}')">
                            <div class = "card-header-is_closed" ></div>
                        </div>
                        <div class="card-body">
                            <div class="card-body-header">
                                <span class="card-header">${category}</span>
                                <h1 class="card-title">${campsite_name}</h1>
                                <a href="${link}" class="card-title">${link}</a>
                                <p class="card-text-hashtag">${tag}</p>
                                <p class = "card-body-phone">${phone}</p>
                                <p class = "card-body-address">${address}</p>
                                <p class = "card-body-address">${road_address}</p>
                            </div>
                                <p class="card-body-description">
                                    ${description}
                                </p>
                            <div class="card-body-footer">
                                <hr style="margin-bottom: 8px; opacity: 0.5; border-color: #FF5675">
                                <i class="icon icon-comment"></i>리뷰 작성
                                <i class="icon icon-comments_count"></i>리뷰 개수
                            </div>
                        </div>
                    </div>`;
    $("#cards-box").append(tempHtml);
}
