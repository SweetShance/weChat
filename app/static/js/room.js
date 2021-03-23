
var room;
$(document).ready(function(){
    var socket = connect_socket();
    $(".send").click(function(){
        send_message(socket, room);
    });
    // 接受消息
    receive_json(socket);
    // 断开连接
    disconnect_socket(socket)
    // 关闭房间
    close_room(socket)
})

function connect_socket(){
    let socket = io.connect(urlPath+room);
    // 获取房间id
    var href_list = location.href.split("/")
    var room_id = href_list[href_list.length - 1]
    socket.emit("join", {"room_id": room_id});
    socket.on("status", function(data){
        room = data.room
    })
    return socket;
};

function disconnect_socket(socket){
    socket.on("close_status", function(data){
        if(data == "该房间已关闭"){
            alert("该房间已关闭")
            window.location.href = urlPath;
        }
    })
}

function close_room(socket){
    $(".close_room").click(function(){
        var href_list = location.href.split("/")
        var room_id = href_list[href_list.length - 1]
        socket.emit("close room", {"room_id": room_id});
    })
}