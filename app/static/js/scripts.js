/*!
* Start Bootstrap - Landing Page v6.0.0 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/

function showArticles() {
    $.ajax({
        type: "GET",
        url: "/camping_data",
        data: {},
        success: function (response) {
            if (response["result"] == "success") {
                let articles = response['articles']
                for (let i = 0; i < articles.length; i++) {
                    let article = articles[i]
                    let campsite_name = article['campsite_name']
                    let category = article['category']
                    let link = article['link']
                    let address = article['address']
                    let roadAddress = article['roadAddress']
                    makeCard(campsite_name, category, link, addresss, roadAddress)
                }
                alert(response["msg"]);
            }
        }
    })
}
