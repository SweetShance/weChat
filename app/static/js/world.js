
$(document).ready(function(){
    var socket = connect_socket();
    $(".send").click(function(){
        send_message(socket);
    })
    // 接受消息
    receive_json(socket);
})

function connect_socket(){
    let socket = io.connect(urlPath+world);
    socket.on("connect",function(data){
        console.log(data)
    });
    return socket;
};






