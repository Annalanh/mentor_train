
let song_container = document.getElementById('song_container')
let song = document.getElementsByClassName('song')

//Trong file JS vừa nhúng, dùng DOM để tìm và in ra thẻ div có id là “song_container”
console.log(song_container)
//Từ thẻ div có id là “song_container”, tìm và in ra tất cả các thẻ div có class là “song"
for(let i = 0; i < song.length; i++){
    console.log(song[i])
}
//Từ tất cả các thẻ div có class là “song", in ra nội dung “Title" và “Artist" của từng thẻ
for(let i = 0; i < song.length; i++){
    console.log(document.getElementsByClassName('title')[i].innerText)
    console.log(document.getElementsByClassName('artist')[i].innerText)
}
//Lập trình sự kiện để khi người dùng click và thẻ có chữ “Delete”, thẻ div (và tất nhiên là các con của nó) với class là “song" có chưa thẻ Delete này bị xoá đi
song[0].getElementsByTagName('i')[0].addEventListener('click', function(){
    song[0].innerText = '';
})
song[1].getElementsByTagName('i')[0].addEventListener('click', function(){
    song[1].innerText = '';
})
song[2].getElementsByTagName('i')[0].addEventListener('click', function(){
    song[2].innerText = '';
})
//Lập trình sự kiện để khi người dùng click vào thẻ có chữ “Edit", tìm và in ra được trường “song_id" của thẻ div chứa thẻ “Edit" được click này
for(let i = 0; i < song.length; i++){
    song[i].getElementsByTagName('i')[1].addEventListener('click', function(){
        console.log(song[i].getAttribute('song_id'));
    })
}
//Lập trình sự kiện để khi người dùng click vào thẻ có chữ “More", in ra được các thông tin “Song"  “Artist" và “song_id" của các thẻ liên quan đến thẻ More này
for(let i = 0; i < song.length; i++){
    song[i].getElementsByTagName('i')[2].addEventListener('click', function(){
        console.log("Title:" + document.getElementsByClassName('title')[i].innerText);
        console.log("Artist: "+ document.getElementsByClassName('artist')[i].innerText);
        console.log("Song id: " + song[i].getAttribute('song_id'));
    })
}
//[OPTIONAL] Thêm 1 nút có chữ “Add" vào file HTML của bài số 7, mỗi khi người dùng bấm Add thì thêm vào 1 nhóm thẻ có cấu trúc như 1 thẻ div với class là song

let btn = document.getElementById('btn')
btn.addEventListener('click', () => {
    $("#song_container").append(`
        <hr>
        <div class="song" song_id="46456">
            <h4 class="title">A title</h4>
            <h5 class="artist">An artist</h5>
            <i>Delete</i>
            <i>Edit</i>
            <i>More</i>
        </div>
    `)
})


