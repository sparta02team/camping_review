/*!
* Start Bootstrap - Landing Page v6.0.0 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/

// 전역변수
let id = ''
let data


$(document).ready(function ()
{
    // user 정보
    setUserInfo()
});

/* 기능변경으로 주석처리
$(document).ajaxStart(function ()
{
    //로딩 중 마우스 커서를 변경
    alert('로딩 중입니다. 잠시만 기다려주세요');
    $('html').css("cursor", "wait");
});


$(document).ajaxStop(function ()
{
    //로딩이 끝나면 마우스 커서를 원래대로
    $('html').css("cursor", "auto");
});
*/

function setUserInfo()
{
    let userInfo = $('#user-info')
    let token = $.cookie('loginToken')
    console.log(token)

    if (token === undefined)
    {
        window.location.href = '/login'
    } else
    {
        $.ajax({
            type: "POST",
            url: "/user",
            headers: {'authorization': `Bearer ${token}`},
            data: {},
            success: function (response)
            {
                if (response['result'] === 'success')
                {
                    // id 를 전역변수 처리 하겠습니다.
                    id = response['id']
                    userInfo.append(`
                        <a class="navbar-brand" href="#">${id}</a>
                        <a class="btn btn-secondary" onclick="logOut()">Log Out</a>
                    `)
                } else
                {
                    alert('다시 로그인해주세요.')
                    window.location.href = '/login'
                }
            }
        })
    }

}


function logOut()
{
    $.removeCookie('loginToken', {path: '/'})
    alert('로그아웃 되었습니다.')
    window.location.href = '/login'
}

function showArticles()
{
    let region = $('.form-select').val()
    console.log(region)
    $("#cards-box").html("")

    $.ajax({
        type: "GET",
        url: "/camping_data",
        data: {'region_give': region},
        success: function (response)
        {
            if (response["result"] == "success")
            {

                let articles = response['articles']
                console.log(articles)
                for (let i = 0; i < articles.length; i++)
                {
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
        error: function (response)
        {
            alert('검색에 실패하였습니다.');
        }
    })
}


function makeCard(campsite_name, category, description, image, link, phone, address, road_address, tag)
{
    $.ajax({
    type: "GET",
    url: "/review/count_review",
    data: {'camping_site': campsite_name},
    success: function (response) {
        if (response["result"] == "success") {
            let count = response['articles']
            let tempHtml = `<div class="card">
                                <div class="card-header" style="background-image: url('${image}')">
                                    <div class = "card-header-is_closed" ></div>
                                </div>
                                <div class="card-body">
                                    <div class= "card-body-header">
                                        <span class= "card-category">${category}</span>
                                        <h1 class= "card-title">${campsite_name}</h1>
                                        <a href="${link}"><img class= "card-link" style= "border-style: none;"></a>
                                        <hr style="opacity: 0.4; border-color: #FF5675">
                                        <p class="card-text-hashtag">${tag}</p>
                                        <p class= "card-body-phone">${phone}</p>
                                        <p class= "card-body-address">${address}</p>
                                        <p class= "card-body-road-address">${road_address}</p>
                                        
                                    </div>
                                        <p class="card-body-description">
                                            ${description}
                                        </p>
                                    <div class="card-body-footer">
                                        <hr style="margin-bottom: 8px; opacity: 0.5; border-color: #FF5675">
                                        <i class="icon icon-comment" onclick="to_review('${campsite_name}')"></i>리뷰 작성
                                        <i class="icon icon-comments_count" title=></i>리뷰 ${count}개
                                    </div>
                                </div>
                            </div>`;
            $("#cards-box").append(tempHtml);
            }
        }
    })
}


function to_review(campsite_name)
{
    // let index = $(e).parent().parent().parent().index()
    // let camping_site =  $('h1.card-title:eq('+ index +')').text()
    let camping_site = campsite_name
    console.log(camping_site)
    console.log(id)

    $.ajax({
        type: 'POST',
        url: '/review',
        data: {
            'camping_site': camping_site,
            'user_id': id
        },
        success: function (response)
        {
            if (response['result'] == 'success')
            {
                window.location.href = '/review'
            }

        }
    })
}

function to_review_page(index)
{
    $.ajax({
        type: 'POST',
        url: '/review_page',
        data: {'index': index},
        success: function (response)
        {
            if (response['result'] == 'success')
            {
                window.location.href = '/review_page'
            }

        }


    })
}


function showReviews()
{

    $("#cards-box").html("")

    $.ajax({
        type: "POST",
        url: "/review_page/get_review",
        success: function (response)
        {
            if (response["result"] == "success")
            {

                let reviews = response['reviews']
                console.log(reviews)

                for (let i = 0; i < reviews.length; i++)
                {
                    let review = reviews[i]
                    let camping_site = review['camping_site']
                    let category = review['category']
                    let description = review['description']
                    let image = review['image']
                    let link = review['link']
                    let phone = review['phone']
                    let address = review['address']
                    let road_address = review['road_address']
                    let tag = review['tag']
                    let id = review['user_id']
                    let index = review['index']
                    makeCard2(camping_site, category, description, image, link, phone, address, road_address, tag, id, index)
                }
            }
        },
        error: function (response)
        {
            alert('검색에 실패하였습니다.');
        }
    })
}

// 작성된 리뷰글을 생성하는 함수
function makeCard2(campsite_name, category, description, image, link, phone, address, road_address, tag, id, index)
{
    let tempHtml = `<div class="card" >
                        <div class="card-header" style="background-image: url('${image}')">
                            <div class = "card-header-is_closed" ></div>
                        </div>
                        <div class="card-body">
                            <div class= "card-body-header">
                                <span class= "card-category">${category}</span>
                                <span class= "card-category">${category}</span>
                                <h1 class= "card-title">${campsite_name}</h1>
                                <a href="${link}"><img class= "card-link" style= "border-style: none;"></a>
                                <hr style="opacity: 0.4; border-color: #FF5675">
                                <p class="card-text-hashtag">${tag}</p>
                                <p class= "card-body-phone">${phone}</p>
                                <p class= "card-body-address">${address}</p>
                                <p class= "card-body-road-address">${road_address}</p>
                                
                            </div>
                                <p class="card-body-description">
                                    ${description}
                                </p>
                            <div class="card-body-footer">
                            
                            <div onclick="to_review_page(${index})" style="cursor:pointer">
                            <i class="icon icon-comment" ></i>리뷰 보기
                            </div>
                            
                               
                            </div>
                        </div>
                    </div>`;
    $("#cards-box").append(tempHtml);
}