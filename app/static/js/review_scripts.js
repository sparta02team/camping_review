let camping_data

function get_campingdata()
{

    $.ajax({
            url: '/review/load_data',
            type: 'POST',
            data: '',
            success: function (response)
            {
                if (response['result'] == 'success')
                {
                    camping_data = response['data']
                    console.log(camping_data)
                    $('#review_tag').append(camping_data['tag'])
                    $('#review_camping_site').append(camping_data['camping_site'])
                    $('#review_tel').append(camping_data['phone'])
                    $('#review_description').append(camping_data['description'])
                    $('#review_category').append(camping_data['category'])
                    $('#review_road_address').append(camping_data['road_address'])
                    $('#review_link').attr('href', (camping_data['link']))
                    $('#review_phone').append(camping_data['phone'])
                    // $('#review_img').attr("src", camping_data['img'])
                    // print('img:', camping_data['img'])
                    let mapX = camping_data['mapx']
                    let mapY = camping_data['mapy']


                    var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
                    var options = { //지도를 생성할 때 필요한 기본 옵션
                        center: new kakao.maps.LatLng(mapX, mapY), //지도의 중심좌표.
                        level: 3 //지도의 레벨(확대, 축소 정도)
                    };

                    var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

                    // 마커가 표시될 위치입니다
                    var markerPosition = new kakao.maps.LatLng(mapX, mapY);

                    // 마커를 생성합니다
                    var marker = new kakao.maps.Marker({
                        position: markerPosition,
                    });

                    // 마커가 지도 위에 표시되도록 설정합니다
                    marker.setMap(map);


                }
            }
        }
    )

}

/*
    makeReview() 함수
    - 캠핑데이터(camping_data(dict)),사용자 아이디, 리뷰내용등을 리뷰 db에등록
*/
function makeReview()
{
    console.log($('#text').val())
    let review_text = $('#text').val()
    let user_id = 'test_id'
    $.ajax({
            type: 'POST',
            url: '/review/make_review',
            data: {'review_text': review_text},
            success: function (response)
            {
                console.log('test')
                upload_img()
                if (response['result'] == 'success')
                {
                    alert('리뷰 등록을 성공했습니다.')
                } else
                {
                    alert('실패')
                }
            }

        }
    )
}

function upload_img()
{
    let image_form = new FormData()
    image_form.append("file", $("#image_file")[0].files[0]);
    console.log(image_form)

    $.ajax({
        enctype: 'multipart/form-data',
        contentType: false,
        processData: false,
        type: 'POST',
        url: '/review/upload_img',
        data: image_form,
        success: function (response)
        {
            if (response['result'] == 'success')
                console.log('이미지 업로드 성공')
        }
    })
}


function to_index()
{
    $.ajax({
        type: 'GET',
        url: '',
        success: function (response)
        {
            window.location.href = '/'
        }
    })
}
