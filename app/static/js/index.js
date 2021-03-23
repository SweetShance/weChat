
//  进入界面对登录设置
$(document).ready(function(){
    var username = $(".user_name").text();
    if($.trim(username) != "暂未登录"){
        $(".login").hide();
        $(".logout").show();
        $(".creat_room").show();
        $(".register").hide();
    }else{
        $(".login").show();
        $(".creat_room").hide();
        $(".logout").hide();
        $(".register").show();
        alert("暂未登录，登陆后才可聊天与进入房间。")
    };
    var args = window.location.search;
    var error = args.substring(7, args.length);
    // decodeURIComponent 解密
    //  encodeURIComponent 加密
    if(error != ""){
        alert(decodeURIComponent(error))
    }
})

// 点击登录
$(".login-submit").click(function(){
    var username = $(".username-login").val();
    var password = $(".password-login").val();
    if($.trim(username) == ""){
        alert("用户不能为空");
        return false;
    };
    if($.trim(password).length < 6){
        alert("密码不能少于6位");
        return false;
    }
    return true;
});

// 点击注册
$(".register-submit").click(function(){
    var username = $(".username-register").val();
    var password = $(".password-register").val();
    
    var email = $(".email").val();
    var reg = /^\w+@\w+\.[a-zA-Z]+$/;

    if($.trim(username) == ""){
        alert("用户不能为空");
        return false;
    };
    if($.trim(password).length < 6){
        alert("密码不能少于6位");
        return false;
    }
    if( !reg.test(email)){
        alert("邮箱不正确");
        return false;
    }
    return true;
});


// 点击创建房间提交
$(".create-room-submit").click(function(){
    var room_name = $(".room_name").val();
    var room_number = $(".room_number").val();
    if($.trim(room_name) == ""){
        alert("房间名不能为空");
        return false;
    }
    if($.trim(room_number) == ""){
        alert("房间编号不能为空");
        return false;
    }
    return true;

})


