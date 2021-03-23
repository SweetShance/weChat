

//  登录检测， 发消息的时候用
function login_status(){
    var username = $(".user_name").text();
    if($.trim(username) == "暂未登录"){
        alert("您还未登录,请先登录")
        return false;
    }
    return true
}

function cookie_to_json(){
    var cookie_key_value_str = document.cookie.split(";");
    var cookie_key_value = {};
    cookie_key_value_str.map(function(data, index){
        var key_value_list = data.split("=");
        cookie_key_value[key_value_list[0].replace(/^\s*/, "")] = key_value_list[1].replace(/^\s*/, "");
    })
    return cookie_key_value 
}


// 接收消息，除自己的消息外，加入到聊天界面
function receive_json(socket){
    socket.on("message", function(data){
        // var json_data = JSON.parse(data);
        var cookie_json = cookie_to_json()
        if(cookie_json){
            var user_uuid = cookie_json.user_about;
            var resp_uuid = data.user_uuid;
            //  暂时头像如果使用默认
            // 用户名那个
            var username = data.username;
            var text = data.text;
            if(user_uuid != resp_uuid){
                //  不是自己发的上频
                var content =   '<div class="other-content" style="clear: both; padding-top: 10px;">'+
                                    '<div>'+
                                        '<img src="/static/img/head-img.png"><span class="user-name">'+username+'</span>'+
                                    '</div>'+
                                    '<div class="user-content">'+
                                        text+
                                    '</div>'+
                                '</div>'
                $(".content").append(content);
            }
        }

    }, namespace="/world")
}

// 发送消息
function send_message(socket, room=null){
    var text = $(".text").val();
    var cookie_json = cookie_to_json()
    var user_about = cookie_json.user_about;
    var username = cookie_json.username;
    if(user_about){
        if($.trim(text) != ""){
            // 上频
            var content =   '<div class="oneslef-content" style="clear: both; padding-top: 10px;">'+
                                '<div style="float: right;">'+
                                    '<span class="user-name">'+username+'</span><img src="/static/img/head-img.png">'+
                                '</div>'+
                                '<br style="clear: both;">'+
                                '<div class="user-content">'+
                                    text+
                                '</div>'+
                            '</div>'
            $(".content").append(content);
            if(room){
                // 发送消息
                console.log("room"+room)
                socket.emit("room", {"room_name": room, "text": text});
            }else{
                // 发送消息
                socket.emit("message", text);
            }
            
            $(".text").val("");

        }else{
            alert("内容不能为空");
        }
    }else{
        alert("登录信息有误请重新登录");
    }
    
}