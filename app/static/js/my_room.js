$(document).ready(function(){
    // 获取后台数据
    get_room_list("1");

    // 进入房间
});

// 获取房间列表
function get_room_list(page){
    $.ajax({
        url: urlPath + '/my_rooms',
        type: "GET",
        success: function(data){
            if(data == undefined){
                $(".room-list").append("暂无数据");
            }else{
                add_html_data(data)
            }
        },
        error: function(xhr){
            alert("获取数据失败")
        }

    });
}

// 添加数据到网页
function add_html_data(data){
    var content = ""
    $(data.data).each(function(index, rooms){
        var describe = rooms.describe.length < 30 ? rooms.describe : rooms.describe.substring(0, 30)+"..."
        var status = rooms.room_status?'开':'关' 
        content +=  '<a href="'+ urlPath + '/room/'+ rooms.union_id +'?start=True'+ '">' +
                        '<div class="panel panel-default" room_id='+ rooms.union_id +'>' +
                            '<div class="panel-body">' +
                                '<img src="static/img/封面.jpg" alt="">' +
                            '</div>' +
                            '<div class="panel-footer">' +
                                 describe +
                            '</div>' +
                            '<div class="room-master">' +
                                '<img class="icon" src="static/img/车.png" alt="">' + rooms.user.username + ":&nbsp" + rooms.room_name + ":&nbsp" + status +
                            '</div>' +
                        '</div>'
                    '</a>'
    });
    // 添加到页面
    $(".room-list").append(content);
}